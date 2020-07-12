from selenium.webdriver.common.by import By


class Sigin(object):

    def __init__(self, driver):
        self.driver = driver
        self.input_mail = self.driver.find_element(By.ID, "login_field")
        self.input_password = self.driver.find_element(By.ID, "password")
        self.send_btn = self.driver.find_element(By.XPATH,"/html/body/div[3]/main/div/form/div[4]/input[9]")

    def write_mail(self,mail):
        self.input_mail.clear()
        self.input_mail.send_keys(mail)

    def write_pass(self,password):
        self.input_password.clear()
        self.input_password.send_keys(password)

    def login(self):
        self.send_btn.click()

