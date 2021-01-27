from django.utils.http import urlencode
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import status
from . import views
from .models import Osoba


class RentalTests(APITestCase):
    def post_osoba(self, _name, _surname, _adress, _age, _is_login, _username, _password, _email):
        user = User.objects.create_user(_username, _email, _password)
        if _is_login:
            self.client.login(username=_username, password=_password)
        url = reverse(views.OsobaViewSet.name)
        data = {
            'name': _name,
            'surname': _surname,
            '_adress': _adress,
            'age': _age,
            'user': user.id
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_count_objects(self):
        self.post_osoba('Adam', 'Lewandowski', 'Warszawa, Olsztynska 17', 45, True, 'alew', 'sadasd', 'test@test.com')
        self.post_osoba('Patryk', 'Piszczek', 'Bytom, Warszawska 15', 21, True, 'ppisz', 'fdfdas', 'test@test.com')
        self.post_osoba('Kinga', 'Olejniczak', 'Zabrze,Warszawska 34', 54, True, 'kolej', 'asdasd', 'test@test.com')
        self.post_osoba('Patrycja', 'Kubica', 'Olsztyn,Warszawska 8', 61, True, 'pkubi', 'asdas', 'test@test.com')
        self.post_osoba('Gabriela', 'Moder', 'Lublin, Warszawska 5', 25, True, 'gmode', 'dfdff', 'test@test.com')
        self.post_osoba('Gabriel', 'Karbownik', 'Lipniki, Warszawska 42', 72, True, 'gkarb', 'ererefsf',
                        'test@test.com')
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 6)

    def test_osoba_return_string(self):
        self.post_osoba('Gabriela', 'Moder', 'Lublin, Warszawska 5', 25, True, 'gmode', 'dfdff', 'test@test.com')
        osoba = Osoba.objects.all()[0]
        self.assertEqual(str(osoba), 'Gabriela Moder')

    def test_post_osoba_with_login(self):
        response = self.post_osoba('Alojzy', 'Rejtan', 'Olsztyn, Warszawska 17', 34, True, 'userAlojzy',
                                   'passwordAlojzy', 'test@wp.pl')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # log in

    def test_osoba_user(self):
        response = self.post_osoba('Alojzy', 'Rejtan', 'Warszawa, Olsztynska 17', 34, True, 'userAlojzy',
                                   'passwordAlojzy', 'wp@test.pl')
        user = User.objects.filter(id=response.data['user'])[0]
        self.assertEqual(user._surname, 'Rejtan')
        self.assertEqual(user._adress, 'Warszawa, Olsztynska 17')
        self.assertEqual(user._age, 34)

    def test_filter_adress(self):
        self.post_osoba('Piotr', 'Roter', 'Bytom, Warszawska 11', 21, True, 'prote', 'asdasd', 'test@test.com')
        self.post_osoba('Sylwia', 'Opalach', 'Kutno, Warszawska 5', 21, True, 'sopal', 'sadasd', 'test@test.com')
        self.post_osoba('Szymon', 'Gutowski', 'Bytom, Warszawska 15', 21, True, 'sguto', 'gdsgs', 'test@test.com')
        filter_by_adress = {'adress': 'Bytom, Warszawska 15'}
        url = '{0}?{1}'.format(reverse(views.OsobaViewSet.name), urlencode(filter_by_adress))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['adress'], 'Bytom, Warszawska 11')

