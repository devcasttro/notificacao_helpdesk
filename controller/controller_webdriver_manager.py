from selenium import webdriver


class WebDriverManager:
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        if self.driver is None:
            self.driver = webdriver.Chrome()  # Inicia o WebDriver do Chrome
        return self.driver
    
    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
