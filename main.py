# Additional needed imports can be found in tbselenium or selenium's documentation
import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from os import path
import os

# Edit this to whatever website you need
websiteurl = "https://google.com"

# Obtains location of geckodriver and tor browser
torname = os.path.abspath("Tor Browser\Start Tor Browser.lnk")
torlocation = os.path.abspath("Tor Browser")
geckolocation = os.path.abspath("geckodriver")

# Launches first Tor, feel free to do whatever you want in this one.
os.startfile (torname)
sleep(10)
# Launches second Tor and contains whatever is going to be done in the script.
launch_tbb_tor_with_stem(torlocation)

with TorBrowserDriver(torlocation, tor_cfg=cm.USE_STEM, executable_path=geckolocation) as driver:
    driver.load_url(websiteurl, wait_for_page_body=True)
    # Below is what will be done in the launched Tor
    print("It works!") 
    sleep(30)

    # Will automatically close after the sleep if there's nothing else to do 
