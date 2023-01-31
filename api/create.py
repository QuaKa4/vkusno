from api.api_base import ApiBase


class CreateApi(ApiBase):
    def create_item(self, id: str, name: str, job: str):
        url = f'https://reqres.in/api/users/{id}'
        params = {
            "name": name,
            "job": job
        }

        response = self.post(url, params)
        return response
