from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_HEADER = (By.XPATH, "//div[contains(text(),'Для кого самокат')]") # заголовок Для кого самокат
    NAME = (By.XPATH, '(//input[@placeholder="* Имя"])') # поле Имя
    SURNAME = (By.XPATH, '(//input[@placeholder="* Фамилия"])') # поле Фамилия
    ADRESS = (By.XPATH, '(//input[@placeholder="* Адрес: куда привезти заказ"])') # поле Адрес
    METRO = (By.XPATH, '(//input[@placeholder="* Станция метро"])') # поле Метро
    METRO_VALUE = (By.XPATH, '//div/ul/li[@class="select-search__row"]') # значение метро
    PHONE = (By.XPATH, '(//input[@placeholder="* Телефон: на него позвонит курьер"])') # поле Телефон
    NEXT = (By.XPATH, '(//button[text() = "Далее"])') # кнопка Далее
    DATE = (By.XPATH, '(//input[@placeholder="* Когда привезти самокат"])')  # поле Даты
    OCT21 = (By.XPATH, '//div[contains(text(),"21")]') # 21 октября
    TIME = (By.XPATH, '//div[contains(text(),"* Срок аренды")]') # поле Срок аренды
    DAY = (By.XPATH, '//div[contains(text(),"сутки")]') # сутки
    BLACK = (By.ID, 'black') # чекбокс Черный жемчуг
    ORDER_BUTTON = (By.XPATH, '(//button[text() = "Заказать"])[2]') # кнопка заказать в форме заказа
    YES = (By.XPATH, '//button[contains(text(),"Да")]') # кнопка Да
    SUCCESS = (By.XPATH, '(//div[text() = "Заказ оформлен"])') # заголовок Заказ оформлен

