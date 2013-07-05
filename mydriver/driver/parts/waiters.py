from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    visibility_of_element_located,
    invisibility_of_element_located,
)

TIMEOUT = 10
class WebDriverWaitersMixin(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO overwirte expected condition classes so they can use our built in functions
    def waitUntilElementIsPresent(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self, timeout).until(presence_of_element_located(self._parse_locator(locator)))

    def waitUntilElementIsNotPresent(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self, timeout).until_not(presence_of_element_located(self._parse_locator(locator)))

    def waitUntilElementIsVisible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self, timeout).until(visibility_of_element_located(self._parse_locator(locator)))

    def waitUntilElementIsNotVisible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self, timeout).until(invisibility_of_element_located(self._parse_locator(locator)))


class element_to_be_ready(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        if self.element.is_displayed() and self.element.is_enabled():
            print(self.element.is_displayed(), self.element.is_enabled())
            return True
        else:
            return False


class WebElementWaitersMixin(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def waitUntilReady(self, timeout=TIMEOUT):
        method = element_to_be_ready(element=self)
        return WebDriverWait(self, timeout).until(method)

    def waitUntilNotReady(self, timeout=TIMEOUT):
        method = element_to_be_ready(element=self)
        return WebDriverWait(self, timeout).until_not(method)

