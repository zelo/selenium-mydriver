from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

SELECTORS_DICT = {
    'id': lambda expression: (By.ID, expression),
    'xpath': lambda expression: (By.XPATH, expression),
    'name': lambda expression: (By.NAME, expression),
    'link': lambda expression: (By.LINK_TEXT, expression),
    'css': lambda expression: (By.CSS_SELECTOR, expression),
# TODO Extract this to another location
#     IMO THIS ONE LINK SELECTOR IS BETTER
#     'link': lambda expression: (By.XPATH, "//a[descendant-or-self::node()[text()='%s']]" % expression),
}


class SelectorsMixin(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _parse_selector(self, selector):
        """
        split selector in two parts
        method = everything before first '='
        expression = everything after first '='
        output contains parameters for webdriver/webelement finlocatord_element(s) function (by, value).
        """
        try:
            selector = selector.split('=')
            method = selector[0]
            expression = '='.join(selector[1:])
        except ValueError:
            message = "Invalid selector format. Valid selectors looks like 'method=expression'. ie. id=header or xpath=//node()[text()='abc']"
            raise ValueError(message)

        try:
            method, expression = SELECTORS_DICT[method](expression=expression)
        except KeyError:
            message = "Invalid selector method %s.\nAvailable methods are: %s." % (method, SELECTORS_DICT.keys())
            raise ValueError(message)

        return method, expression

    def _find_by(self, selector, eager, timeout):
        if eager:
            function = self.find_elements
        else:
            function = self.find_element

        method, expression = self._parse_selector(selector=selector)
        # TODO replace constant wait with configurable one
        timeout = timeout or 0
        result = WebDriverWait(self, timeout).until(lambda self: function(by=method, value=expression))
        return result

    def find_element_by(self, selector, timeout=None):
        return self._find_by(selector=selector, eager=False, timeout=timeout)

    def find_elements_by(self, selector, timeout=None):
        return self._find_by(selector=selector, eager=True, timeout=timeout)

    def add_or_change_selector(self, method, function):
        global SELECTORS_DICT
        SELECTORS_DICT[method] = function

    def add_or_change_selectors(self, selectors_dict):
        for key in selectors_dict.keys():
            self.add_or_change_selector(key, selectors_dict[key])