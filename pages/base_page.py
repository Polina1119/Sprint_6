import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://qa-scooter.praktikum-services.ru/'
        self.url_order = 'https://qa-scooter.praktikum-services.ru/order'

    @allure.step('Открываем страницу Яндекс.Самокат')
    def go_to_site(self):
        self.driver.set_window_size(1280, 1024)
        return self.driver.get(self.url)

    @allure.step('Переходим на страницу оформления заказа')
    def go_to_order_page(self):
        return self.driver.get(self.url_order)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not find {locator}')

    @allure.step('Переходим на последнюю открытую вкладку')
    def switch_to(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    def execute_script(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def current_url(self):
        return self.driver.current_url

