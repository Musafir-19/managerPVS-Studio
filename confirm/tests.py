from django.test import TestCase
from django.urls import reverse
from .models import PassSave


class PasswordCase(TestCase):
    def setUp(self) -> None:
        self.test_password = PassSave.objects.create(
            title = 'Facebook',
            email = 'facebook@mail.ru',
            password = 'facebook123'
        )

    def test_confirm_password(self):
        self.assertEqual(f'{self.test_password.title}', 'Facebook')
        self.assertEqual(f'{self.test_password.email}', 'facebook@mail.ru')
        self.assertEqual(f'{self.test_password.password}', 'facebook123')
        
    def test_password_view(self):
        # Обращаемся к страничке: name = 'manager'
        response = self.client.get(reverse('manager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Pass_Manager")