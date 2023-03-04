from rest_framework import serializers
from django.contrib.auth import (get_user_model, authenticate)
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType

from users.models import UserProfile


# Serializers define the API representation.

class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        read_only=False,
    )
    last_name = serializers.CharField(
        read_only=False,
    )
    image = serializers.CharField(
        read_only=False,
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image',
                  'facebook_profile', 'linkedin_profile', 'website']
        extra_kwargs = {'user': {'required': False, 'default': None}, }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer(many=False, required=False)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'userprofile')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        normaluser_group, created = Group.objects.get_or_create(
            name="normaluser")

        content_type = ContentType.objects.get_for_model(User)

        user_permission = Permission.objects.filter(content_type=content_type)
        # print([perm.codename for perm in user_permission])
        # # => ['add_post', 'change_post', 'delete_post', 'view_post']

        for perm in user_permission:
            if perm.codename == "add_user":
                normaluser_group.permissions.add(perm)

            elif perm.codename == "change_user":
                normaluser_group.permissions.add(perm)
            # elif perm.codename == "view_user":
            #     normaluser_group.permissions.add(perm)

        profile_data = validated_data.pop('userprofile', None)
        user_instance = get_user_model().objects.create_user(**validated_data)

        # Create user profile with blank attributes and associate with the user
        profile_instance = UserProfile.objects.create(
            user=user_instance,
            first_name='',
            last_name='',
            image='',
            facebook_profile='',
            linkedin_profile='',
            website=''
        )

        if profile_data:
            # add user id to the profile_data dictionary via update function
            profile_data.update({"user_id": user_instance.id})
            profile_instance, created = UserProfile.objects.get_or_create(
                user_id=user_instance.id)
            profile_instance.__dict__.update(profile_data)
            profile_instance.save()

        # Add the user to the normaluser group
        user_instance.groups.add(normaluser_group)

        return user_instance

    def update(self, instance, validated_data):
        userprofile_data = validated_data.pop('userprofile', None)
        if userprofile_data:
            userprofile_serializer = self.fields['userprofile']
            userprofile = instance.userprofile
            userprofile = userprofile_serializer.update(
                userprofile, userprofile_data)
            validated_data['userprofile'] = userprofile
        return super().update(instance, validated_data)

        # remove pw (pop) from validated_data and update calling the superclasses update method
        # password = validated_data.pop('password', None)
        # user = super().update(instance, validated_data)

        # if password:
        #     user.set_password(password)
        #     user.save()

        # return user


class AuthTokenSerializer(serializers.Serializer):
    """User auth token serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type', 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = 'Can´t authenticate user with provided credentials'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            # 12 characters are more than enough.
            file_name = str(uuid.uuid4())[:12]
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
