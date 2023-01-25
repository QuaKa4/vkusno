from requests import Response, HTTPError, Session


class ApiBase:
    DEFAULT_STATUS_CODE = (200, 201, 202, 204)

    def handle_status(self, response: Response):
        if response.status_code not in self.DEFAULT_STATUS_CODE:
            raise HTTPError(f'{response.status_code} not in {self.DEFAULT_STATUS_CODE}')

    def __init__(self, session: Session = None):
        self.session = session or Session()

    def request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
        except ConnectionError as e:
            raise ConnectionError(f'{method} request to {url}, throws exception {e}') from e
        self.handle_status(response)
        return response

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, data, **kwargs):
        return self.request('POST', url, data=data, **kwargs)

    def patch(self, url, data, **kwargs):
        return self.request('PATCH', url, data=data, **kwargs)

    def put(self, url, data, **kwargs):
        return self.request('PUT', url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)
