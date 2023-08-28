from django.test import TestCase
from core.models import Post, Category, Tag, Comment
from django.contrib.auth.models import User


class PostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category = Category.objects.create(name='Django')
        self.tag = Tag.objects.create(name='programming')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test',
            author=self.user
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test')
        self.assertEqual(self.post.author, self.user)

    def test_post_categories(self):
        self.assertEqual(self.post.categories.first().name, 'Django')

    def test_post_tags(self):
        self.assertEqual(self.post.tags.first().name, 'programming')


class CommentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='12345')
        self.post = Post.objects.create(title='Test', content='content', author=self.user)
        self.comment = Comment.objects.create(
            author=self.user,
            content='Nice post!',
            post=self.post
        )

    def test_comment(self):
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.content, 'Nice post!')
        self.assertEqual(self.comment.post, self.post)