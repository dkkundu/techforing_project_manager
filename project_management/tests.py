from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.test import TestCase


class UserTests(TestCase):

    def setUp(self):
        """Set up a user for testing"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )

    def test_user_register(self):
        url = reverse('user-register')  # Adjust the URL name as needed
        data = {'username': 'newuser', 'password': 'password123', 'email': 'newuser@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'newuser')

    def test_user_login(self):
        url = reverse('user-login')  # Adjust the URL name as needed
        data = {'username': self.user.username, 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_get_user_details(self):
        url = reverse('user-detail', args=[self.user.id])  # Adjust the URL name as needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])  # Adjust the URL name as needed
        data = {'username': 'updateduser', 'email': 'updated@example.com'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'updateduser')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])  # Adjust the URL name as needed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProjectTests(TestCase):

    def setUp(self):
        """Set up a project for testing"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )
        self.client.login(username='testuser', password='password123')  # Login the user

    def test_create_project(self):
        url = reverse('project-list')
        data = {'name': 'New Project', 'description': 'A new test project'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Project')

    def test_get_project(self):
        # Create a project
        url_create = reverse('project-list')
        project_data = {'name': 'Existing Project', 'description': 'An existing project'}
        self.client.post(url_create, project_data, format='json')

        # Get the created project
        url = reverse('project-detail', args=[1])  # Adjust ID if needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Existing Project')

    def test_update_project(self):
        url_create = reverse('project-list')
        project_data = {'name': 'Existing Project', 'description': 'An existing project'}
        self.client.post(url_create, project_data, format='json')

        url = reverse('project-detail', args=[1])  # Adjust ID if needed
        data = {'name': 'Updated Project', 'description': 'An updated test project'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Project')

    def test_delete_project(self):
        url_create = reverse('project-list')
        project_data = {'name': 'Existing Project', 'description': 'An existing project'}
        self.client.post(url_create, project_data, format='json')

        url = reverse('project-detail', args=[1])  # Adjust ID if needed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskTests(TestCase):

    def setUp(self):
        """Set up a task for testing"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )
        self.client.login(username='testuser', password='password123')  # Login the user

        # Create a project for the task
        self.project = {
            'name': 'Test Project',
            'description': 'A test project',
        }
        self.client.post(reverse('project-list'), self.project, format='json')

    def test_create_task(self):
        project_id = 1  # Use the created project ID
        url = reverse('task-list', args=[project_id])
        data = {'title': 'New Task', 'description': 'A new test task', 'project': project_id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_get_task(self):
        project_id = 1
        self.client.post(reverse('task-list', args=[project_id]), {'title': 'Test Task', 'description': 'Task description'}, format='json')
        url = reverse('task-detail', args=[1])  # Use the created task ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        project_id = 1
        self.client.post(reverse('task-list', args=[project_id]), {'title': 'Test Task', 'description': 'Task description'}, format='json')
        url = reverse('task-detail', args=[1])  # Use the created task ID
        data = {'title': 'Updated Task', 'description': 'Updated task description'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        project_id = 1
        self.client.post(reverse('task-list', args=[project_id]), {'title': 'Test Task', 'description': 'Task description'}, format='json')
        url = reverse('task-detail', args=[1])  # Use the created task ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentTests(TestCase):

    def setUp(self):
        """Set up a comment for testing"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123', email='testuser@example.com'
        )
        self.client.login(username='testuser', password='password123')  # Login the user

        # Create a project for the task
        self.project = {
            'name': 'Test Project',
            'description': 'A test project',
        }
        self.client.post(reverse('project-list'), self.project, format='json')
        self.task = {'title': 'Test Task', 'description': 'Task description', 'project': 1}
        self.client.post(reverse('task-list', args=[1]), self.task, format='json')

    def test_create_comment(self):
        task_id = 1
        url = reverse('comment-list', args=[task_id])
        data = {'text': 'New comment', 'task': task_id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], 'New comment')

    def test_get_comment(self):
        task_id = 1
        self.client.post(reverse('comment-list', args=[task_id]), {'text': 'Test Comment'}, format='json')
        url = reverse('comment-detail', args=[1])  # Use the created comment ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('text', response.data)

    def test_update_comment(self):
        task_id = 1
        self.client.post(reverse('comment-list', args=[task_id]), {'text': 'Test Comment'}, format='json')
        url = reverse('comment-detail', args=[1])  # Use the created comment ID
        data = {'text': 'Updated comment'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Updated comment')

    def test_delete_comment(self):
        task_id = 1
        self.client.post(reverse('comment-list', args=[task_id]), {'text': 'Test Comment'}, format='json')
        url = reverse('comment-detail', args=[1])  # Use the created comment ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
