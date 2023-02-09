from rest_framework import serializers
from django.contrib.auth import (get_user_model, authenticate)
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType

from users.models import UserProfile


# Serializers define the API representation.

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image',
                  'facebook_profile', 'linkedin_profile', 'website']


# Will only return a single UserProfile object
# for the given user, and it will not allow for
# updates or creation of UserProfile objects
# through the serializer.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer(many=False, required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'userprofile')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        normaluser_group, created = Group.objects.get_or_create(
            name="normaluser")

        content_type = ContentType.objects.get_for_model(User)

        user_permission = Permission.objects.filter(content_type=content_type)
        print([perm.codename for perm in user_permission])
        # => ['add_post', 'change_post', 'delete_post', 'view_post']

        for perm in user_permission:
            if perm.codename == "add_user":
                normaluser_group.permissions.add(perm)

            elif perm.codename == "change_user":
                normaluser_group.permissions.add(perm)
            # elif perm.codename == "view_user":
            #     normaluser_group.permissions.add(perm)

        profile_data = validated_data.pop('userprofile')

        if profile_data:
            user_id = self.context['request'].user.id
            profile_instance, created = UserProfile.objects.get_or_create(
                user_id=user_id)
            profile_data.update({"user_id": user_id})
            if not created:
                profile_instance.__dict__.update(profile_data)
                profile_instance.save()
            user_instance = get_user_model().objects.create_user(
                userprofile=profile_instance, **validated_data)

        else:
            get_user_model().objects.create_user(**validated_data)
        # Add the user to the normaluser group
        user_instance.groups.add(normaluser_group)

        return user_instance

    def update(self, instance, validated_data):
        """Update and return user"""

        # remove pw (pop) from validated_data and update calling the superclasses update method
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


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
