from selenium import webdriver
from xvfbwrapper import Xvfb

# applications
from blog import blog_tests
import dashboard

BASE_URL = "http://localhost:8000"

# setup Xvfb to run tests in headless mode
vdisplay = Xvfb(width=1280, height=740)

print("Opening virtual display...")
vdisplay.start()

print("Setting up Firefox browser...")
browser = webdriver.Firefox()

blog_tests.blog_tests(browser, BASE_URL)

print("Shutting down Firefox browser...")
browser.quit()

print("Shutting down virtual display...")
vdisplay.stop()
