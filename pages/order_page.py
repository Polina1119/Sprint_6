import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Order


class OrderPage(BasePage):
    @allure.step('Скролл до кнопки Заказать')
    def scroll(self, button):
        self.find_element(button)
        element = self.find_element(button)
        return self.execute_script(element)

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

