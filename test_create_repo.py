import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Home import Home
from pages.Sign_in import Sigin
from pages.Dashboard import Dashboard
from pages.Repository import Repository

class Github_repository_test():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.mail='Danielf.r97@gmail.com'
        self.password='Fe63b4366c140'
        self.name='Calidad de software'
        self.description='Selenium'
        self.driver.maximize_window()
        self.driver.get("http://www.github.com")

    def test_login(self):
        driver=self.driver
        home = Home(driver)
        home.to_login()

        login=Sigin(driver)
        login.write_mail(self.mail)
        login.write_pass(self.password)
        login.login()

        if driver.title == "GitHub":
            print("SignIn github successfully")
        else:
            print("SignIn failed")

    def test_create_repository(self):
        driver=self.driver
        dashboard=Dashboard(driver)
        dashboard.to_new_repo()

        repository=Repository(driver)
        repository.fill_name(self.name)
        repository.fill_description(self.description)
        print('antes')
        driver.implicitly_wait(3)
        print('Después')
        # repository.create_repo()

    def exit(self):
        self.driver.close()

if __name__ == "__main__":
    test=Github_repository_test()
    test.test_login()
    test.test_create_repository()
    # test.exit()
    # prueba.tearDown()
