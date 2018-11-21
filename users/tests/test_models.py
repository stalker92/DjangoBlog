from unittest import mock
from PIL import Image
from django.test import TestCase
from django.contrib.auth.models import User


class ProfileTest(TestCase):

    def setUp(self):
        user = User.objects.create_superuser(username='admin', email='admin@bogusemail.com', password='admin')
        self.profile = user.profile
        self.new_image = Image.new('RGB', (600, 600), 'white')

    def test_str(self):
        self.assertEqual(str(self.profile), f'{self.profile.user.username} Profile')

    @mock.patch('PIL.Image.open')
    def test_save(self, mock_image_open):
        mock_image_open.return_value = self.new_image
        mock_image_open.return_value.save = lambda *args, **kwargs: None
        self.profile.save()
        self.assertEqual(self.new_image.height, 300)
        self.assertEqual(self.new_image.width, 300)


