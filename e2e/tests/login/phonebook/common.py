from api.api_base import ApiBase


class Login(ApiBase):
    def as_user(self, email: str = 'test@gmail.com', password: str = 'test@gmail.com'):
        url = 'http://phonebook.telran-edu.de:8080/api/user/login'
        data = {
            'email': email,
            'password': password,
        }
        self.post(url, data=data)
        return self.session
