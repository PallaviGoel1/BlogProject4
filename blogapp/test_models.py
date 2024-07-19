from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse


# Code to test models.py
class testModels(TestCase):

        def test_status_draft(self):
            test_user = User.objects.create(username='test_model', is_superuser=False, password='Test@Model', email='test@model.test')
            item = Post.objects.create(title='test Status', slug= 'test1-status', content='test',snippet='test', author=test_user)
            self.assertEqual(item.category,'coding','Category is defaulting to coding')

        def test_like_count(self):
            test_user = User.objects.create(username='test_model', is_superuser=False, password='Test@Model', email='test@model.test')
            item = Post.objects.create(title='test Status', slug= 'test1-status', content='test',snippet='test', author=test_user)
            self.assertEqual(int(item.likes.count()), 0)

        def test_title_and_author_string(self):
            test_user = User.objects.create(username='test_model', is_superuser=False, password='Test@Model', email='test@model.test')
            item = Post.objects.create(title='test Status', slug= 'test1-status', content='test',snippet='test', author=test_user)
            self.assertEqual(str(item.title + '|' + str(item.author)), 'test Status|test_model')

        def test_get_absolute_url_after_posting_blog(self):
            test_user = User.objects.create(username='test_model', is_superuser=False, password='Test@Model', email='test@model.test')
            item = Post.objects.create(title='test Status', slug= 'test1-status', content='test',snippet='test', author=test_user)
            url = self.client.get(reverse("home"))
            self.assertEqual(url.status_code, 200)


