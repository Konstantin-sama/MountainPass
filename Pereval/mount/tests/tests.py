from django.test import TestCase
from django.urls import reverse
from rest_framework import status, response
from rest_framework.test import APITestCase

from mount.models import Pereval, Users, Coords, Level, Images
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
                last_name='lastname1',
                first_name='firstname1',
                patronymic='patronymic1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height='1111'
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_1, image='https://images.com/image1.jpg', title='Title 1'),
            Images(pereval=self.pereval_1, image='https://images.com/image2.jpg', title='Title 2'),
        ])

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='lastname2',
                first_name='firstname2',
                patronymic='partonymic2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height='2222'
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_2, image='https://images.com/image3.jpg', title='Title 3'),
            Images(pereval=self.pereval_2, image='https://images.com/image4.jpg', title='Title 4'),
        ])

        self.pereval_3 = Pereval.objects.create(
            status='PN',
            beauty_title='Beauty title 3',
            title='Title 3',
            other_titles='Other titles 3',
            connect='',
            tourist_id=Users.objects.create(
                email='user3@mail.ru',
                last_name='lastname3',
                first_name='firstname3',
                patronymic='patronymic3',
                phone='+33333333333'
            ),
            coord_id=Coords.objects.create(
                latitude='55.55555',
                longitude='66.66666',
                height='3333'
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring=''
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_3, image='https://images.com/image5.jpg', title='Title 5'),
            Images(pereval=self.pereval_3, image='https://images.com/image6.jpg', title='Title 6'),
        ])

    def test_get(self):
        url = reverse('perevals')
        resource = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        # сравнивает serializer_data и resource.data
        self.assertEqual(serializer_data, response.data)
        # проверяет, что количество serializer_data = 3
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
                last_name='lastname1',
                first_name='firstname1',
                patronymic='patronymic1',
                phone='+11111111111'
            ),
            coord_id=Coords.objects.create(
                latitude='11.11111',
                longitude='22.22222',
                height='1111'
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_1, image='https://images.com/image1.jpg', title='Title 1'),
            Images(pereval=self.pereval_1, image='https://images.com/image2.jpg', title='Title 2'),
        ])

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Beauty title 2',
            title='Title 2',
            other_titles='Other titles 2',
            connect='',
            tourist_id=Users.objects.create(
                email='user2@mail.ru',
                last_name='lastname2',
                first_name='firstname2',
                patronymic='patronymic2',
                phone='+22222222222'
            ),
            coord_id=Coords.objects.create(
                latitude='33.33333',
                longitude='44.44444',
                height='2222'
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_2, image='https://images.com/image3.jpg', title='Title 3'),
            Images(pereval=self.pereval_2, image='https://images.com/image4.jpg', title='Title 4'),
        ])

        self.pereval3 = Pereval.objects.create(
            status='PN',
            beauty_title='Beauty title 3',
            title='Title 3',
            other_titles='Other titles 3',
            connect='',
            tourist_id=Users.objects.create(
                email='user3@mail.ru',
                last_name='lastname3',
                first_name='firstname3',
                patronymic='patronymic3',
                phone='+33333333333'
            ),
            coord_id=Coords.objects.create(
                latitude=55.55555,
                longitude=66.66666,
                height=3333
            ),
            level=Level.objects.create(
                winter='',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )
        Images.objects.create([
            Images(pereval=self.pereval_3, image='https://images.com/image5.jpg', title='Title 5'),
            Images(pereval=self.pereval_3, image='https://images.com/image6.jpg', title='Title 6'),
        ])

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        expected_data = [
            {
                'beauty_title': 'Beauty title 2',
                'title': 'Title 2',
                'other_titles': 'Other titles 2',
                'connect': '',
                'tourist_id': {
                    'email': 'user2@mail.ru',
                    'last_name': 'lastname2',
                    'first_name': 'firstname2',
                    'patronymic': 'patronymic2',
                    'phone': '+22222222222'
                },
                'coord_id': {
                    'height': '33.33333',
                    'latitude': '44.44444',
                    'longitude': '2222'
                },
                'level': {
                    'winter': '',
                    'summer': '1A',
                    'autumn': '1A',
                    'spring': '1A'
                },
                'images': [
                    {
                        'image': 'https://images.com/image3.jpg', 'title': 'Title 3'
                    },
                    {
                        'image': 'https://images.com/image4.jpg', 'title': 'Title 4'
                    }
                ]
            },
            {
                "beauty_title": "beauty_title 1",
                "title": "title 1",
                "other_titles": "other_titles 1",
                "connect": "",
                "tourist_id": {
                    "email": "user1@mail.ru",
                    "last_name": "lastname1",
                    "first_name": "firstname1",
                    "patronymic": "patronymic11",
                    "phone": "+11111111111"
                },
                "coord_id": {
                    "latitude": '11.11111',
                    "longitude": '22.22222',
                    "height": '1111'
                },
                "level": {"winter": "1A", "summer": "1A", "autumn": "1A", "spring": "1A"},
                "images": [{"image": "https://images.com/image1.jpg", "title": "Title 1"},
                           {"image": "https://images.com/image2.jpg", "title": "Title 1"}]
            }
        ]

        self.assertEqual(serializer_data, expected_data)
