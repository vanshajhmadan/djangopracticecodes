from django.test import TestCase
from .models import Post

from django.contrib.auth.models import User

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username = 'testuser1', 
            password = 'abc123'
        )
        testuser1.save()
        
        
    # create a blog post
        test_post = Post.objects.create(
            author = testuser1, 
            title = 'blog title',
            body = 'Body Content...',
        )
        test_post.save()
        
    def blog_test_content(self):
        post = Post.objects.get(id=1)
        author = f'{ post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'blog_title')
        self.assertEqual(body,'body content')
        