import requests

from api.register import RegisterApi


def test_user_can_register_with_correct_data():
    email = "eve.holt@reqres.in"
    password = "pistol"
    token = RegisterApi().register_as_user(email, password)['token']
    assert token == "QpwL5tke4Pnpja7X4"


def test_foo():
    url = 'https://reqres.in/api/register'
    email = "eve.holt@reqres.in"
    password = "pistol"
    data = {'email': email, 'password': password}
    response = requests.request('POST', url, data=data)
    assert response.json()['token'] == "QpwL5tke4Pnpja7X4"
    assert response.status_code == 200
