from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTests(TestCase):
    username = 'myusername'
    email = 'myusername@gmail.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_from(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            self.username,
            self.email,

        )
        self.assertEqual(user_model.objects.all().count(), 1)
        self.assertEqual(user_model.objects.all()[0].username, self.username)
        self.assertEqual(user_model.objects.all()[0].email, self.email)
