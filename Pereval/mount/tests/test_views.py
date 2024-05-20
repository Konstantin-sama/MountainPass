# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from rest_framework.utils import json
#
# from mount.models import Pereval, Users, Coords, Level, Images
# from mount.serializers import PerevalSerializer
# from mount.tests.payloads import *
#
#
# class BaseTestCase(APITestCase):
#     def setUp(self):
#         self.pereval1 = Pereval.objects.create(
#             beauty_title='Beauty title 1',
#             title='Title 1',
#             other_titles='Other titles 1',
#             connect='',
#             tourist_id=Users.objects.create(
#                 email='user1@mail.ru',
#                 last_name='Фамилия 1',
#                 first_name='Имя 1',
#                 patronymic='Отчество 1',
#                 phone='+11111111111'
#             ),
#             coord_id=Coords.objects.create(
#                 latitude=11.11111,
#                 longtitude=22.22222,
#                 height=1111
#             ),
#             level=Level.objects.create(
#                 winter='1A',
#                 summer='1A',
#                 autumn='1A',
#                 spring='1A'
#             )
#         )
#         Images.objects.bulk_create([
#             Images(image='https://images.com/image1.jpg', title='Title 1'),
#             Images(image='https://images.com/image2.jpg', title='Title 2'),
#         ])
#
#         self.pereval2 = Pereval.objects.create(
#             beauty_title='Beauty title 2',
#             title='Title 2',
#             other_titles='Other titles 2',
#             connect='',
#             tourist_id=Users.objects.create(
#                 email='user2@mail.ru',
#                 last_name='Фамилия 2',
#                 first_name='Имя 2',
#                 patronymic='Отчество 2',
#                 phone='+22222222222'
#             ),
#             coord_id=Coords.objects.create(
#                 latitude=33.33333,
#                 longtitude=44.44444,
#                 height=2222
#             ),
#             level=Level.objects.create(
#                 winter='',
#                 summer='1A',
#                 autumn='1A',
#                 spring='1A'
#             )
#         )
#         Images.objects.bulk_create([
#             Images(image='https://images.com/image3.jpg', title='Title 3'),
#             Images(image='https://images.com/image4.jpg', title='Title 4'),
#         ])
#
#         self.pereval3 = Pereval.objects.create(
#             status='PN',
#             beauty_title='Beauty title 3',
#             title='Title 3',
#             other_titles='Other titles 3',
#             connect='',
#             tourist_id=Users.objects.create(
#                 email='user3@mail.ru',
#                 last_name='Фамилия 3',
#                 first_name='Имя 3',
#                 patronymic='Отчество 3',
#                 phone='+33333333333'
#             ),
#             coord_id=Coords.objects.create(
#                 latitude=55.55555,
#                 longtitude=66.66666,
#                 height=3333
#             ),
#             level=Level.objects.create(
#                 winter='',
#                 summer='1A',
#                 autumn='1A',
#                 spring=''
#             )
#         )
#         Images.objects.bulk_create([
#             Images(image='https://images.com/image5.jpg', title='Title 5'),
#             Images(image='https://images.com/image6.jpg', title='Title 6'),
#         ])
#
#
# class GetAllPeravalsTest(BaseTestCase):
#     """ Test module for GET all perevals API """
#
#     def setUp(self):
#         super().setUp()
#
#     def test_get_all_perevals(self):
#         response = self.client.get(reverse('create-list'))
#         perevals = Pereval.objects.all()
#         serializer = PerevalSerializer(perevals, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class GetSinglePerevalTest(BaseTestCase):
#     """ Test module for GET single pereval API """
#
#     def setUp(self):
#         super().setUp()
#
#     def test_get_valid_single_pereval(self):
#         response = self.client.get(
#             reverse('partial_update', kwargs={'pk': self.pereval1.pk}))
#         pereval = Pereval.objects.get(pk=self.pereval1.pk)
#         serializer = PerevalSerializer(pereval)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_pereval(self):
#         response = self.client.get(
#             reverse('partial_update', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
# class CreateNewPerevalTest(APITestCase):
#     """ Test module for inserting a new pereval """
#
#     def setUp(self):
#         self.valid_payload = valid_pereval_test_data
#         self.missing_tourist_id = missing_tourist_id_test_data
#         self.missing_coord_id = missing_coord_id_test_data
#         self.missing_level = missing_level_test_data
#         self.missing_images = missing_images_test_data
#
#     def test_create_valid_pereval(self):
#         response = self.client.post(
#             reverse('create-list'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_create_missing_tourist_id_pereval(self):
#         response = self.client.post(
#             reverse('create-list'),
#             data=json.dumps(self.missing_tourist_id),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_create_missing_coord_id_pereval(self):
#         response = self.client.post(
#             reverse('create-list'),
#             data=json.dumps(self.missing_coord_id),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_create_missing_level_pereval(self):
#         response = self.client.post(
#             reverse('create-list'),
#             data=json.dumps(self.missing_level),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_create_missing_images_pereval(self):
#         response = self.client.post(
#             reverse('create-list'),
#             data=json.dumps(self.missing_images),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#
# class PatchSinglePerevalTest(BaseTestCase):
#     """ Test module for patching a single pereval """
#
#     def setUp(self):
#         super().setUp()
#
#     def test_valid_patch_pereval(self):
#         response = self.client.patch(path=reverse('partial_update',
#                                                   kwargs={'pk': self.pereval1.pk}),
#                                      data=patch_valid_payload,
#                                      format='json')
#         self.assertEqual(response.data, {'state': 1, 'message': 'Success'})
#
#     def test_changed_tourist_id_patch_pereval(self):
#         response = self.client.patch(path=reverse('partial_update',
#                                                   kwargs={'pk': self.pereval1.pk}),
#                                      data=patch_changed_tourist_id_payload,
#                                      format='json')
#         pereval = Pereval.objects.get(pk=self.pereval1.pk)
#         serializer = PerevalSerializer(instance=pereval,
#                                        data=patch_changed_tourist_id_payload,
#                                        partial=True)
#         serializer.is_valid()
#         self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})
#
#     def test_invalid_coord_id_pereval(self):
#         response = self.client.patch(path=reverse('partial_update',
#                                                   kwargs={'pk': self.pereval1.pk}),
#                                      data=patch_invalid_coord_id_payload,
#                                      format='json')
#         pereval = Pereval.objects.get(pk=self.pereval1.pk)
#         serializer = PerevalSerializer(instance=pereval,
#                                        data=patch_invalid_coord_id_payload,
#                                        partial=True)
#         serializer.is_valid()
#         self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})
#
#     def test_non_new_status_pereval(self):
#         response = self.client.patch(path=reverse('partial_update',
#                                                   kwargs={'pk': self.pereval3.pk}),
#                                      data=patch_non_new_status_payload,
#                                      format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#
# class GetPerevalByEmailTest(BaseTestCase):
#     def setUp(self):
#         super().setUp()
#
#     def test_get_data_by_email(self):
#         response = self.client.get("/submitData/", {"tourist_is__email": "user2@mail.ru"})
#         self.assertEqual(len(response.data), 1)
