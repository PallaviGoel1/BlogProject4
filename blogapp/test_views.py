from django.test import TestCase
from .views import LikeView


# Code to test views.py
class TestLikeView(TestCase):

    def Post_gets_added_with_ID(self):
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
