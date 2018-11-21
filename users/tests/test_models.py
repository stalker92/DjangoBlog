from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth.models import User
from PIL import Image


class ProfileTest(TestCase):

    def setUp(self):
        user = User.objects.create_superuser(username='admin', email='admin@bogusemail.com', password='admin')
        self.profile = user.profile

    def test_str(self):
        self.assertEqual(str(self.profile), f'{self.profile.user.username} Profile')

    @patch('Image.open')
    def image_open_mock(self):
        return Image.new('RGB', (600, 600), 'white')

    def test_save(self):
        self.profile.save()
        self.assertEqual(self.profile.image.height, 300)
        self.assertEqual(self.profile.image.width, 300)
