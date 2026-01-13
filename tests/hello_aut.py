import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        browser = sys.argv[2] if len(sys.argv) > 2 else "firefox"

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            server = "http://localhost:4445"
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            server = "http://localhost:4446"
        else:
            options = webdriver.FirefoxOptions()
            server = "http://localhost:4444"

        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"

        self.browser.get(url)
        self.browser.save_screenshot("screenshot.png")

        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
