from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from news.models import News

class NewsAPITest(APITestCase):
    def setUp(self):
        # ✅ Create superuser for admin access
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpass',
            email='test@example.com'
        )

        # ✅ Generate JWT token for auth
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # ✅ Set JWT token in request headers
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # ✅ Clear all existing news items before each test
        News.objects.all().delete()

        # ✅ Endpoint for News
        self.url = '/api/news/news/'  # Make sure this matches your router

    def test_create_news(self):
        data = {
            'news_title': 'Breaking News',
            'news_desc': '<p>This is the latest update.</p>',
        }
        response = self.client.post(self.url, data, format='multipart')
        print("Create News Response:", response.status_code, response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 1)

    def test_list_news(self):
        News.objects.create(news_title='Test', news_desc='<p>Some content</p>')

        response = self.client.get(self.url)
        print("List News Response:", response.status_code)
        print("List News Response Data:", response.data)

        self.assertEqual(response.status_code, 200)

        # ✅ Check paginated results count
        self.assertEqual(len(response.data['results']), 1)
