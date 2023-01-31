from api.api_base import ApiBase


class DeleteApi(ApiBase):
    def delete_item(self):
        url = 'https://reqres.in/api/users/2'
        response = self.delete(url)
        return response
