from .selectors import SelectorsMixin
from .waiters import WebDriverWaitersMixin
from .webelement import WebElement

class WebDriverMixin(WebDriverWaitersMixin, SelectorsMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_web_element(self, element_id):
        return WebElement(parent=self, id_=element_id)
