from django.test import TestCase
from django.urls import reverse
from rest_framework import status, response
from rest_framework.test import APITestCase

from mount.models import Pereval, Users, Coords, Level
from mount.serializers import PerevalSerializer


# pip install coverage
# coverage run --source='.' manage.py test .
# coverage report
# coverage html


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Beauty title 1',
            title='Title 1',
            other_titles='Other titles 1',
            connect='',
            tourist_id=Users.objects.create(
                email='user1@mail.ru',
                last_name='������� 1',
                first_name='��� 1',
                patronymic='�������� 1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude=11.11111,
                longtitude=22.22222,
                height=1111
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image1.jpg', title='Title 1'),
        #     Images(image='https://images.com/image2.jpg', title='Title 2'),
        # ])

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='������� 2',
                first_name='��� 2',
                patronymic='�������� 2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude=33.33333,
                longtitude=44.44444,
                height=2222
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image3.jpg', title='Title 3'),
        #     Images(image='https://images.com/image4.jpg', title='Title 4'),
        # ])

        self.pereval3 = Pereval.objects.create(
            status='PN',
            beauty_title='Beauty title 3',
            title='Title 3',
            other_titles='Other titles 3',
            connect='',
            tourist_id=Users.objects.create(
                email='user3@mail.ru',
                last_name='������� 3',
                first_name='��� 3',
                patronymic='�������� 3',
                phone='+33333333333'
            ),
            coord_id=Coords.objects.create(
                latitude=55.55555,
                longtitude=66.66666,
                height=3333
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring=''
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image5.jpg', title='Title 5'),
        #     Images(image='https://images.com/image6.jpg', title='Title 6'),
        # ])

    def test_get(self):
        url = reverse('perevals-list')
        resource = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        # ���������� serializer_data � resource.data
        self.assertEqual(serializer_data, response.data)
        # ���������, ��� ���������� serializer_data = 3
        self.assertEqual(len(serializer_data), 3)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PrevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Beauty title 1',
            title='Title 1',
            other_titles='Other titles 1',
            connect='',
            tourist_id=Users.objects.create(
                email='user1@mail.ru',
                last_name='������� 1',
                first_name='��� 1',
                patronymic='�������� 1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude=11.11111,
                longtitude=22.22222,
                height=1111
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image1.jpg', title='Title 1'),
        #     Images(image='https://images.com/image2.jpg', title='Title 2'),
        # ])

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='������� 2',
                first_name='��� 2',
                patronymic='�������� 2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude=33.33333,
                longtitude=44.44444,
                height=2222
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image3.jpg', title='Title 3'),
        #     Images(image='https://images.com/image4.jpg', title='Title 4'),
        # ])

        self.pereval3 = Pereval.objects.create(
            status='PN',
            beauty_title='Beauty title 3',
            title='Title 3',
            other_titles='Other titles 3',
            connect='',
            tourist_id=Users.objects.create(
                email='user3@mail.ru',
                last_name='������� 3',
                first_name='��� 3',
                patronymic='�������� 3',
                phone='+33333333333'
            ),
            coord_id=Coords.objects.create(
                latitude=55.55555,
                longtitude=66.66666,
                height=3333
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring=''
            )
        )
        # Images.objects.bulk_create([
        #     Images(image='https://images.com/image5.jpg', title='Title 5'),
        #     Images(image='https://images.com/image6.jpg', title='Title 6'),
        # ])

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        expected_data = [
            {
                'beauty_title': '���. ',
                'title': '����',
                'other_titles': '�����',
                'connect': '',
                'tourist_id': {
                    'email': 'qwerty@mail.ru',
                    'last_name': '������',
                    'first_name': '�������',
                    'patronymic': '��������',
                    'phone': '+7 555 55 55'
                },
                'coord_id': {
                    'height': 1200,
                    'latitude': 45.3842,
                    'longtitude': 7.1525
                },
                'level': {
                    'winter': '',
                    'summer': '1�',
                    'autumn': '1�',
                    'spring': ''
                },
                'images': [
                    {
                        'image': 'https://images.com/image1.jpg', 'title': '���������'
                    },
                    {
                        'image': 'https://images.com/image2.jpg', 'title': '������'
                    }
                ]
            },
            {
                "beauty_title": "beauty_title11",
                "title": "title11",
                "other_titles": "other_titles11",
                "connect": "connect11",
                "tourist_id": {
                    "email": "post@mail.ru",
                    "last_name": "�������11",
                    "first_name": "���11",
                    "patronymic": "��������11",
                    "phone": "89999900"
                },
                "coord_id": {
                    "latitude": 45.42,
                    "longitude": 77.15,
                    "height": 120
                },
                "level": {"winter_lev": "4A", "summer_lev": "4�", "autumn_lev": "4�", "spring_lev": "4A"},
                "images": [{"image": "https://images.jpg", "title": "�������"},
                           {"image": "https://avatars-images.jpg", "title": "������"}]
            }
        ]

        self.assertEqual(serializer_data, expected_data)
