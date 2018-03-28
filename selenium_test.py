from selenium import webdriver
import time


driver = webdriver.Firefox()
# Get the address
driver.get("http://www.mail.yahoo.com")

# username
username_field = driver.find_element_by_id("login-username")
username_field.send_keys("sreekanth_19")
next_button = driver.find_element_by_id("login-signin")
next_button.click()
time.sleep(5)

# Password
pwdtxt = driver.find_element_by_name("password")
# Enter your password
pwdtxt.send_keys("PASSWORD")
login_button = driver.find_element_by_id("login-signin")
login_button.click()
time.sleep(5)

# Compose Mail
compose_button = driver.find_element_by_class_name("btn-compose")
compose_button.click()
time.sleep(5)

# Enter to field and body message
to_field = driver.find_element_by_class_name("cm-to-field")
to_field.send_keys("ksree19181@gmail.com")
subject = driver.find_element_by_id("subject-field")
subject.send_keys("test_mail")
body = driver.find_element_by_id("rtetext")
body.send_keys("Hello, How are you")
driver.find_element_by_class_name("default").click()
