from django.test import TestCase
from django.contrib.auth import get_user_model

from todos.models import Task


class TaskModelTests(TestCase):

    def test_create_task(self):
        """Test if creating a task is successful"""
        user = get_user_model().objects.create_user(
            'testuser@example.com',
            'testitest'
        )

        task = Task(user=user, title='Sample task', priority='red',
                    description='sampledescription', completed=True)

        self.assertEqual(str(task), task.title)
