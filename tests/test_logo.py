from time import sleep
from pages.main_page import MainPage, BasePage


class TestLogo:
    def test_logo_yandex(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site()
        main_page.click_logo_yandex()
        main_page.go_to_dzen()
        sleep(2)

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    def test_logo_scooter(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_order_page()
        main_page.click_logo_scooter()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

