from api.api_base import ApiBase


class RegisterApi(ApiBase):
    def register_as_user(self, email, password):
        url = 'https://reqres.in/api/register'
        params = {'email': email, 'password': password}
        response = self.post(url, params).json()
        return response
