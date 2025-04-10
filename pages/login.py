from selenium.webdriver.common.by import By

from conftest import browser_invocation


class Login:
	name_field = (By.XPATH, "(//input[@name='name'])[1]")
	email_field = (By.CSS_SELECTOR, "input[name='email']")
	password_field = (By.CSS_SELECTOR, "#exampleInputPassword1")
	button = (By.ID, 'exampleCheck1')
	submit = (By.CSS_SELECTOR, "input[value='Submit']")

	def __init__(self, driver, data):
		self.driver = driver
		self.browser_data = data

	def input_name(self):
		self.driver.find_element(*Login.name_field).send_keys(self.browser_data[0])

	def input_email(self):
		self.driver.find_element(*Login.email_field).send_keys(self.browser_data[1])

	def input_password(self):
		self.driver.find_element(*Login.password_field).send_keys(self.browser_data[2])

	def click_button(self):
		self.driver.find_element(*Login.button).click()

	def click_submit(self):
		self.driver.find_element(*Login.submit).click()
