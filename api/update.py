from api.api_base import ApiBase


class UpdateApi(ApiBase):
    def update_put_item(self, id: int, name: str, job: str):
        url = f'https://reqres.in/api/users/{id}'
        params = {
            "name": name,
            "job": job
        }
        response = self.put(url, params).json()
        return response

    def update_patch_item(self, id: int, name: str, job: str):
        url = f'https://reqres.in/api/users/{id}'
        params = {
            "name": name,
            "job": job
        }
        response = self.patch(url, params).json()
        return response
