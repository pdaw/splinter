# -*- coding: utf-8 -*-

# Copyright 2013 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement as BaseWebDriverElement
from splinter.driver.webdriver.cookie_manager import CookieManager


class WebDriver(BaseWebDriver):

    driver_name = "remote"
    # TODO: This constant belongs in selenium.webdriver.Remote
    DEFAULT_URL = 'http://127.0.0.1:4444/wd/hub'

    def __init__(self, url=DEFAULT_URL, browser='firefox', wait_time=2, **ability_args):
        browsername = browser.upper()
        # Handle case where user specifies IE with a space in it
        if browsername == 'INTERNET EXPLORER':
            browsername = 'INTERNETEXPLORER'
        abilities = getattr(DesiredCapabilities, browsername, {})
        abilities.update(ability_args)

        self.driver = Remote(url, abilities)

        self.element_class = WebDriverElement

        self._cookie_manager = CookieManager(self.driver)

        super(WebDriver, self).__init__(wait_time)


class WebDriverElement(BaseWebDriverElement):
    pass
