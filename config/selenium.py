from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.webdriver import WebDriver

def _get_options_webdruver() -> ChromeOptions:
    """Возвращает ChromeOptions с настройками для WebDriver"""
    options = ChromeOptions()
    # драйвер работает без открытия самого браузера
    # options.add_argument('--headless')
    # для обхода блокировки селениума браузером
    options.add_argument("--disable-blink-features=AutomationControlled")
    return options

def get_webdriver() -> WebDriver:
    options = _get_options_webdruver()
    driver = Chrome(options=options)
    return driver
