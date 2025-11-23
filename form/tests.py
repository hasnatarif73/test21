from rest_framework.test import APITestCase
from rest_framework import status
from service.models import Jobs
from form.models import userForm

class UserFormAPITest(APITestCase):
    def setUp(self):
        self.job = Jobs.objects.create(
            job_title='Frontend Developer',
            job_description='React dev needed',
        )
        self.url = '/api/forms/user-forms/'  # ✅ correct URL

    def test_form_submission(self):
        data = {
            'job': self.job.id,
            'name': 'Hasnat Arif',
            'email': 'hasnat@example.com',
            'phone': '03001234567',
            'message': 'I am interested in this job.',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(userForm.objects.count(), 1)
