from selenium.webdriver import Remote as _Remote, Chrome as _Chrome, Firefox as _Firefox, Ie as _Ie

from .parts.webdriver import WebDriverMixin

class Remote(WebDriverMixin, _Remote):
    pass

class Firefox(WebDriverMixin, _Firefox):
    pass

class Chrome(WebDriverMixin, _Chrome):
    pass

class Ie(WebDriverMixin, _Ie):
    pass

