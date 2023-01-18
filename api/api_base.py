import requests
from requests import Response, HTTPError


class ApiBase:
    DEFAULT_STATUS_CODE = (200, 201, 202, 204)

    # TODO: Need add session(learn requests documentation)
    def handle_status(self, response: Response):
        if response.status_code not in self.DEFAULT_STATUS_CODE:
            raise HTTPError(f'{response.status_code} not in {self.DEFAULT_STATUS_CODE}')

    def session(self, url):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        token = requests.get(url, headers=headers).json()['token']
        p = requests.Session
        return p

    def request(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)
        except ConnectionError as e:
            raise ConnectionError(f'{method} request to {url}, throws exception {e}') from e
        self.handle_status(response)
        return response

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, params, **kwargs):
        return self.request('POST', url, data=params, **kwargs)

    def patch(self, url, params, **kwargs):
        return self.request('PATCH', url, params=params, **kwargs)

    def put(self, url, params, **kwargs):
        return self.request('PUT', url, params=params, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)
