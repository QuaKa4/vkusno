from api.login import LoginApi


def test_user_cant_login_with_empty_password():
    email = 'eve.holt@reqres.in'
    error_with_wrong_data = LoginApi().unsuccessful_login_as_user(email)['error']
    assert error_with_wrong_data == 'Missing password'


def test_user_cant_login_with_wrong_email():
    email = 'wrong_password'
    password = 'cityslicka'
    error_with_wrong_data = LoginApi().unsuccessful_login_as_user(email, password)['error']
    assert error_with_wrong_data == 'user not found'


def test_user_cant_login_with_wrong_data():
    email = 'wrong_email'
    password = 'wrong_password'
    error_with_wrong_data = LoginApi().unsuccessful_login_as_user(email, password)['error']
    assert error_with_wrong_data == 'user not found'
