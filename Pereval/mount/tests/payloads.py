valid_pereval_test_data = {
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
}

missing_tourist_id_test_data = {
    'beauty_title': '���. ',
    'title': '����',
    'other_titles': '�����',
    'connect': '',
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
}

missing_coord_id_test_data = {
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
}

missing_level_test_data = {
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
    'images': [
        {
            'image': 'https://images.com/image1.jpg', 'title': '���������'
        },
        {
            'image': 'https://images.com/image2.jpg', 'title': '������'
        }
    ]
}

missing_images_test_data = {
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
    }
}

patch_valid_payload = {
    "title": "Changed Title",
    "tourist_id": {
        "email": "user1@mail.ru",
        "last_name": "������� 1",
        "first_name": "��� 1",
        "patronymic": "�������� 1",
        "phone": "+11111111111"
    }
}

patch_changed_tourist_id_payload = {
    "title": "Changed Title",
    "tourist_id": {
        "email": "user1@mail.ru",
        "last_name": "������� 0",
        "first_name": "��� 1",
        "patronymic": "�������� 1",
        "phone": "+11111111111"
    }
}

patch_invalid_coord_id_payload = {
    "tourist_id": {
        "email": "user1@mail.ru",
        "last_name": "������� 1",
        "first_name": "��� 1",
        "patronymic": "�������� 1",
        "phone": "+11111111111"
    },
    "coord_id": {
        "height": "abc",
        "latitude": "null",
        "longtitude": "null"
    }
}

patch_non_new_status_payload = {
    "title": "Changed Title",
    "tourist_id": {
        "email": "user3@mail.ru",
        "last_name": "������� 3",
        "first_name": "��� 3",
        "patronymic": "�������� 3",
        "phone": "+33333333333"
    }
}
