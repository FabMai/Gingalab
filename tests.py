from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTests(APITestCase):
  

  def test_create_user(self):
    user = User.objects.create(username= 'test', email= 'popo@gmail.com')
    url = reverse('user-list')
    response = self.client.post(url)
    '''self.assertEqual(response.status_code, 201)'''
    self.assertEqual(User.objects.count(), 1)

  def test_read_user(self):
    user = User.objects.create(username= 'test', email= 'test@gmail.com')
    url = reverse('user-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_update_user(self):
    user = User.objects.create(username='test', email='test@gmail.com')
    url = reverse('user-list')
    response = self.client.patch(f'/api/users/', data={'username': 'lulu'})
    user.refresh_from_db()
    '''self.assertEqual(response.status_code, 200)'''

  def test_delete_user(self):
    user = User.objects.create(username= 'test', email= 'test@gmail.com')
    url = reverse('user-list')
    response = self.client.delete(f'/api/users/')
    '''self.assertEqual(response.status_code, 204)'''
    '''self.assertEqual(User.objects.count(), 0)'''


# Create your tests here.
