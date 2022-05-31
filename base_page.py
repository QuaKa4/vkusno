class BasePage:
    base: str
    url: str

    def __init__(self, driver):
        self.driver = driver

    def make_url(self):
        self.driver.get(self.url)
        self.driver

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def make_url(self, **kwargs):
    #     if not hasattr(self, 'url'):
    #         raise AttributeError(f'Page "{self.__class__.__name__}" does not have "url" attribute, please declare it!')
    #     return urljoin(base=f'{self.base}', url=self.url, allow_fragments=False).format(**kwargs)
    #
    # def transfer(self, **kwargs):
    #     url = self.make_url(**kwargs)
    #     self.driver.get(url)


class ProductBasePage(BasePage):
    base = 'https://pythonru.com/'
