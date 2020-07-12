from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Home import Home
from pages.Sign_in import Sigin
from pages.Dashboard import Dashboard
from pages.Repository import Repository

class Github_repository():

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_create_repository(self,name,description):
        driver = self.driver
        driver.get("http://www.github.com")
        self.driver.set_window_size(1920, 1080)

        home = Home(driver)
        home.to_login()

        login=Sigin(driver)
        login.write_mail("Danielf.r97@gmail.com")
        login.write_pass("Fe63b4366c140")
        login.login()
        dashboard=Dashboard(driver)
        dashboard.to_new_repo()

        repository=Repository(driver)
        repository.write_name(name)
        driver.implicitly_wait(5)
        repository.write_description(description)
        repository.create_repo()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    prueba=Github_repository()
    prueba.setUp()
    prueba.test_create_repository(name='Calidad de software',description='selenium')
    # prueba.tearDown()
