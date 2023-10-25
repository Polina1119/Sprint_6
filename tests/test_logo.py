from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestLogo:
    def test_logo_yandex(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_logo_yandex()
        main_page.go_to_dzen()
        base_page.find_element(Main.DZEN)

        assert base_page.current_url() == 'https://dzen.ru/?yredirect=true'

    def test_logo_scooter(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_order_page()
        main_page.click_logo_scooter()

        assert base_page.current_url() == 'https://qa-scooter.praktikum-services.ru/'

