import datetime
import pytz
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post


class PostTest(TestCase):

    def setUp(self):
        self.post = self.create_post()

    def create_post(self,
                    title='Test Title',
                    content='This is test content.',
                    date_posted=datetime.datetime(2015, 12, 11).astimezone(pytz.timezone('US/Pacific'))):
        user = User.objects.create_superuser(username='admin', email='admin@bogusemail.com', password='admin')
        return Post.objects.create(title=title, content=content, date_posted=date_posted, author=user)

    def test_str(self):
        self.assertEqual(str(self.post), self.post.title)
