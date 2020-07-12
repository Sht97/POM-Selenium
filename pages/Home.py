from selenium.webdriver.common.by import By
class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.sigin_button = driver.find_element(By.LINK_TEXT, "Sign in")
        self.input_search=driver.find_element(By.NAME,'q')
        self.input_username=driver.find_element(By.ID,'user[login]')
        self.input_email=driver.find_element(By.ID,'user[email]')
        self.input_password=driver.find_element(By.ID,'user[password]')

# home page locators defining

    def to_login(self):
        self.sigin_button.click()

    def fill_username(self,username):
        self.input_username.clear()
        self.input_username.send_keys(username)

    def register(self):
        print()
        #Aquí va el método para dar click en el botón de crear nuevo usuario
