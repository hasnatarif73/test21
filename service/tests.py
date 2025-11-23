from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from service.models import Service, Jobs

class ServiceJobAPITest(APITestCase):
    def setUp(self):
        # ✅ Create a superuser to bypass IsAdminOrReadOnly
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpass',
            email='test@example.com'
        )

        # ✅ Generate JWT access token
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # ✅ Authenticate test client with JWT
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # ✅ Define your API endpoints
        self.service_url = '/api/service/services/'
        self.jobs_url = '/api/service/jobs/'

    def test_create_service(self):
        data = {
            'service_title': 'Web Development',
            'service_description': 'We build websites.',
        }
        response = self.client.post(self.service_url, data)
        print("Create Service Response:", response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)

    def test_list_services(self):
        Service.objects.all().delete()
        Service.objects.create(service_title='SEO', service_description='Ranking stuff')
        response = self.client.get(self.service_url)
        print("List Services Response:", response.status_code, response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Handle pagination if enabled
        if 'results' in response.data:
            self.assertEqual(len(response.data['results']), 1)
        else:
            self.assertEqual(len(response.data), 1)

    def test_create_job(self):
        data = {
            'job_title': 'React Developer',
            'job_description': 'Frontend role',
        }
        response = self.client.post(self.jobs_url, data)
        print("Create Job Response:", response.status_code, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Jobs.objects.count(), 1)
