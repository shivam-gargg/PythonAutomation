import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class',params=[('shivam','sg@gmail.com','Admin@123'), ('shivam1','sg1@gmail.com','Admin@12345')])
def browser_invocation(request):
	# options = webdriver.ChromeOptions()
	# options.add_argument("headless")
	# driver = webdriver.Chrome(options=options)
	driver = webdriver.Chrome()
	driver.implicitly_wait(5)
	driver.maximize_window()
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	request.cls.driver = driver
	yield request.param
	driver.close()
