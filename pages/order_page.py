import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators as Order


class OrderPage(BasePage):
    @allure.step('Скролл до кнопки Заказать')
    def scroll(self, button):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(button))
        element = self.driver.find_element(*button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver

    @allure.step('Нажимаем кнопку Заказать')
    def click_on_button_order(self, button):
        return self.find_element(button).click()

    @allure.step('Заполняем форму заказа')
    def filling_form_order(self, name, surname, adress, phone):
        self.find_element(Order.NAME).send_keys(name)
        self.find_element(Order.SURNAME).send_keys(surname)
        self.find_element(Order.ADRESS).send_keys(adress)
        self.find_element(Order.METRO).click()
        self.find_element(Order.METRO_VALUE).click()
        self.find_element(Order.PHONE).send_keys(phone)
        self.find_element(Order.NEXT).click()
        self.find_element(Order.DATE).click()
        self.find_element(Order.OCT21).click()
        self.find_element(Order.TIME).click()
        self.find_element(Order.DAY).click()
        self.find_element(Order.BLACK).click()
        self.find_element(Order.ORDER_BUTTON).click()
        self.find_element(Order.YES).click()

