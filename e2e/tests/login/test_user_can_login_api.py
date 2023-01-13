from api.login import LoginApi


def test_user_can_login_with_correct_data():
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'
    reference_token = 'QpwL5tke4Pnpja7X4'
    actual_token = LoginApi().login_as_user(email, password)['token']
    assert actual_token == reference_token, 'Tokens is not match'
    return actual_token
