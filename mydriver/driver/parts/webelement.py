from selenium.webdriver.remote.webelement import WebElement as _WebElement

from .actions import ActionsMixin
from .selectors import SelectorsMixin
from .waiters import WebElementWaitersMixin

class WebElement(WebElementWaitersMixin, ActionsMixin, SelectorsMixin, _WebElement):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
