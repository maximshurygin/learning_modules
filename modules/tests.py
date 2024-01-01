from django.test import TestCase
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.test import APITestCase

from modules.models import Module
from modules.serializers import ModuleSerializer
from modules.validators import TitleValidator


class ModuleTest(TestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            order_number=1,
            title='Module Test',
            description='Some module'
        )

    def test_module_title(self):
        """Тестирование названия модуля."""

        self.assertEqual(
            self.module.title,
            'Module Test'
        )

    def test_module_description(self):
        """Тестирование описания модуля."""

        self.assertEqual(
            self.module.description,
            'Some module'
        )


class ModuleSerializerTest(TestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            order_number=2,
            title='Serializer Test',
            description='Some description'
        )
        self.serializer = ModuleSerializer(instance=self.module)

    def test_serializer_data(self):
        """Тестирование данных сериализатора"""

        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            {'id', 'order_number', 'title', 'description'}
        )

        self.assertEqual(
            data['order_number'],
            2
        )

        self.assertEqual(
            data['title'],
            'Serializer Test')

        self.assertEqual(
            data['description'],
            'Some description')


class TitleValidatorTest(TestCase):

    def setUp(self):
        self.validator = TitleValidator('title')

    def test_valid_title(self):
        """Тестирование валидатора с правильным названием"""
        self.validator({'title': 'Valid Title'})

    def test_invalid_title(self):
        """Тестирование валидатора с неправильным названием"""
        with self.assertRaises(ValidationError):
            self.validator({'title': 'Invalid Title $$$'})

    def test_empty_title(self):
        """Тестирование валидатора с пустым названием"""
        with self.assertRaises(ValidationError):
            self.validator({'title': ''})

    def test_none_title(self):
        """Тестирование валидатора с отсутствующим названием"""
        with self.assertRaises(ValidationError):
            self.validator({'title': None})


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.module = Module.objects.create(
            order_number=3,
            title='test',
            description='some test'
        )

    def test_create_module(self):
        """Тест создания модуля"""

        data = {
            'order_number': 4,
            'title': 'Test1',
            'description': 'Some Test 1'
        }
        response = self.client.post(
            '/module/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Module.objects.count(),
            2
        )

    def test_list_module(self):
        """Тест просмотра списка модулей"""

        response = self.client.get(
            '/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Module.objects.count(),
            1
        )

    def test_retrieve_module(self):
        """Тест просмотра модуля"""

        response = self.client.get(
            f'/module/{self.module.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_module(self):
        """Тест обновления модуля"""

        response = self.client.patch(
            f'/module/update/{self.module.id}/',
            {'title': 'New test'}
        )
        response_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response_data['title'],
            'New test'
        )
        self.assertEqual(
            response_data['description'],
            'some test'
        )

    def test_destroy_module(self):
        """Тест удаления модуля"""

        response = self.client.delete(
            f'/module/delete/{self.module.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Module.objects.count(),
            0
        )


class HomepageTest(APITestCase):
    """Тест главной страницы"""

    def test_homepage_view(self):
        response = self.client.get('/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
