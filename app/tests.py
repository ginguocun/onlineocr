import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

from app.models import ImageUpload


user_data = {
    'username': 'test',
    'password': 'TestPass2020',
    'email': 'test@hotmail.com'
}

login_data = {
    'username': user_data['username'],
    'password': user_data['password'],
}

image_data = {
    'path': 'test/test01.png',
    'image': os.path.join(settings.MEDIA_ROOT, 'test/test01.png'),
    'file_name': 'test01.png',
    'letters': [
        'D', 'j', 'a', 'n', 'g', 'o', 'm', 'a', 'k', 'e', 's', 'i', 't', 'e', 'a', 's', 'i', 'e', 'r', 't', 'o', 'b',
        'u', 'i', 'l', 'd', 'b', 'e', 't', 't', 'e', 'r', 'W', 'e', 'b', 'a', 'p', 'p', 's', 'm', 'o', 'r', 'e', 'q',
        'u', 'i', 'c', 'k', 'l', 'y', 'a', 'n', 'd', 'w', 'i', 't', 'h', 'l', 'e', 's', 's', 'c', 'o', 'd', 'e'],
    'count': 65,
    'created_by': None
}

url_data = {
    'token_obtain_url': '/api/token_obtain_pair/',
    'token_refresh_url': '/api/token_refresh/',
    'ocr_url': '/api/ocr/',
    'history_url': '/api/history/'
}


class LoginTest(TestCase):

    def setUp(self):
        self.user_data = user_data

    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(**self.user_data)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_login(self):
        is_login = self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        self.assertFalse(is_login, False)
        user_model = get_user_model()
        user_model.objects.create_user(**self.user_data)
        is_login = self.client.login(username=self.user_data['username'], password=self.user_data['password'])
        self.assertTrue(is_login, True)


class ImageUploadModelTest(TestCase):

    def setUp(self):
        self.image_data = image_data
        self.user_data = user_data

    def test_create_1(self):
        image_upload_record_1 = ImageUpload.objects.create(image=self.image_data['path'])
        self.assertEqual(image_upload_record_1.file_name, self.image_data['file_name'])
        print(image_upload_record_1.letters)
        self.assertEqual(image_upload_record_1.letters, self.image_data['letters'])
        self.assertEqual(image_upload_record_1.count, self.image_data['count'])
        self.assertEqual(image_upload_record_1.created_by, self.image_data['created_by'])

    def test_create_2(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(**self.user_data)
        user_id = user.id
        image_upload_record_2 = ImageUpload.objects.create(image=self.image_data['path'], created_by_id=user_id)
        self.assertEqual(image_upload_record_2.file_name, self.image_data['file_name'])
        self.assertEqual(image_upload_record_2.letters, self.image_data['letters'])
        self.assertEqual(image_upload_record_2.count, self.image_data['count'])
        self.assertEqual(image_upload_record_2.created_by, user)


class TokenObtainTest(TestCase):

    def setUp(self):
        self.user_data = user_data
        self.login_data = login_data
        self.url_data = url_data

    def test_token_obtain(self):
        response = self.client.post(path=self.url_data['token_obtain_url'], data=self.login_data)
        self.assertEqual(response.status_code, 401)
        # create a user
        user_model = get_user_model()
        user_model.objects.create_user(**self.user_data)
        response = self.client.post(path=self.url_data['token_obtain_url'], data=self.login_data)
        self.assertEqual(response.status_code, 200)

    def test_token_refresh(self):
        # create a user
        user_model = get_user_model()
        user_model.objects.create_user(**self.user_data)
        # get the refresh token
        token_obtain = self.client.post(path=self.url_data['token_obtain_url'], data=self.login_data)
        refresh = token_obtain.data['refresh']
        # obtain the access token by the refresh token
        response = self.client.post(path=self.url_data['token_refresh_url'], data={'refresh': refresh})
        self.assertEqual(response.status_code, 200)


class OcrAPIViewTest(TestCase):

    def setUp(self):
        self.user_data = user_data
        self.login_data = login_data
        self.image_data = image_data
        self.url_data = url_data

    def test_ocr_api_1(self):
        response = self.client.post(
            path=self.url_data['ocr_url'],
            data={'image': open(self.image_data['image'], 'rb')}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.data)
        history = self.client.get(path=self.url_data['history_url'])
        self.assertEqual(history.status_code, 401)

    def test_ocr_api_2(self):
        # create a user
        user_model = get_user_model()
        user = user_model.objects.create_user(**self.user_data)
        user_id = user.id
        # user login
        self.client.login(**self.login_data)
        # upload an image
        ocr = self.client.post(
            path=self.url_data['ocr_url'],
            data={'image': open(self.image_data['image'], 'rb')}
        )
        self.assertEqual(ocr.status_code, 200)
        self.assertIn('content', ocr.data)
        # check history
        history = self.client.get(path=self.url_data['history_url'])
        self.assertEqual(history.status_code, 200)
        self.assertIn('count', history.data)
        self.assertIn('results', history.data)
        self.assertEqual(len(history.data['results']), 1)
        self.assertEqual(history.data['results'][0]['created_by'], user_id)
        self.assertEqual(history.data['results'][0]['file_name'], self.image_data['file_name'])

