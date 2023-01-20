import chromedriver_autoinstaller
import pytest as pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.set_window_position(0, 0)
    driver.implicitly_wait(5)
    return driver

# @pytest.fixture
# def driver(request, driver) -> WebDriver:
#     if request.config.getoption('--driver').lower() == 'remote':
#
#     else:
#         driver.maximize_window()
#     driver._is_video_enabled = request.getfixturevalue('capabilities').get('enableVideo', False)
#     yield driver
#
# @pytest.fixture
# def driver_path(request):
#     driver_path = request.config.getoption('driver_path')
#     if driver_path:
#         return driver_path
#
#     driver_type = request.config.getoption('--driver').lower()
#     if driver_type == 'chrome':
#         return ChromeDriverManager().install()
#     elif driver_type == 'remote':
#         return None
#     else:
#         raise ValueError(f'Unexpected option --driver {driver_type}. Please provide --driver-path for this browser'


# @pytest.fixture
# def capabilities(request, capabilities, browser_mob_proxy):
#     if request.config.getoption('--driver').lower() == 'remote':
#         capabilities['name'] = request.node.name
#     if request.config.getoption('--video') or 'video' in [i.name for i in request.node.own_markers]:
#         capabilities['enableVideo'] = True
#     if browser_mob_proxy:
#         browser_mob_proxy.new_har()
#         browser_mob_proxy.add_to_capabilities(capabilities)
#         capabilities['acceptSslCerts'] = True
#     return capabilities
#
