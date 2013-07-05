from selenium.webdriver.support.select import Select

class ActionsMixin(object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def click(self):
        self.waitUntilReady()
        super().click()

    def write(self, value, clear=True):
        self.waitUntilReady()
        # TODO add check fo element that checks if it can be cleared in other case it throws some shitty exception
        if clear: self.clear()
        self.send_keys(value)

    def _checkbox_handler(self, value):
        self.waitUntilReady()
        if (value == True and not self.is_selected()) or (value == False and self.is_selected()):
            self.click()

    def check(self):
        self._checkbox_handler(value=True)

    def uncheck(self):
        self._checkbox_handler(value=False)

    def select(self, text):
        self.waitUntilReady()
        Select(webelement=self).select_by_visible_text(text)
