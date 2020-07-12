from selenium.webdriver.common.by import By
class Repository(object):

    def __init__(self, driver):
        self.driver = driver
        self.input_name=driver.find_element(By.ID, "repository_name")
        self.input_description=driver.find_element(By.ID, "repository_description")
        self.btn_create=driver.find_element(By.CSS_SELECTOR, ".first-in-line")

    def fill_name(self,name):
        self.input_name.clear()
        self.input_name.send_keys(name)

    def fill_description(self,description):
        self.input_description.clear()
        self.input_description.send_keys(description)

    def create_repo(self):
        self.btn_create.click()