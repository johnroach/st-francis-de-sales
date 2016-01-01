from selenium import webdriver
import sys


class blog_tests(object):
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.run_tests()

    def run_tests(self):
        tests = []

        tests.append({'test': self.check_home_page,'name': 'Home Page Check'})

        for test in tests:
            try:
                test["test"]()
            except:
                e = sys.exc_info()[0]
                print("ERROR: " + e.__name__ + " at " + test["name"])

    def check_home_page(self):
        self.browser.get(self.base_url)
        assert "John Roach" in self.browser.title

    def check_pages(self):
        self.browser.get(self.base_url)
        assert "John Roach" in self.browser.title
