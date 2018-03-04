# Import your newly installed selenium package
from selenium import webdriver

# Now create an 'instance' of your driver
# This path should be to wherever you downloaded the driver
driver = webdriver.Chrome(executable_path="/home/ujjwal/chromedriver")
# A new Chrome (or other browser) window should open up

# Now just tell it wherever you want it to go
driver.get("https://medium.com/@dalewahl")