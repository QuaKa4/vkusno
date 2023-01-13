from api.api_base import ApiBase


class LoginApi(ApiBase):
    email = 'eve.holt@reqres.in'
    password = '"cityslicka'
    wrong_email = 'wrong_email'
    wrong_password = 'wrong_password'

    def login_as_user(self, email, password):
        url = 'https://reqres.in/api/login'
        params = {
            "email": email,
            "password": password
        }
        r = self.post(url, params)
        return r.json()

    def unsuccessful_login_as_user(self, wrong_email, wrong_password=None):
        url = 'https://reqres.in/api/login'
        params = {
            "email": wrong_email,
            "password": wrong_password
        }
        r = self.post(url, params)
        return r.json()
