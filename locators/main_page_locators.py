from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_UP = (By.XPATH, '(//button[text() = "Заказать"])[1]') # кнопка Заказать вверху страницы
    ORDER_DOWN = (By.XPATH, '(//button[text() = "Заказать"])[2]')#кнопка Заказать внизу страницы
    LOGO_YANDEX = (By.XPATH, '(//img[@alt="Yandex"])') # логотип Яндекс
    LOGO_SCOOTER = (By.XPATH, '(//img[@alt="Scooter"])') # логотип Самокат
    HEADER = (By.CLASS_NAME, 'Home_Header__iJKdX') # заголовок Самокат на пару дней
    FAQ = (By.XPATH, '//div[contains(text(),"Вопросы о важном")]') # заголовок Вопросы о важном
    ANSWER_1 = (By.ID, 'accordion__panel-0') # 1 ответ
    ANSWER_2 = (By.ID, 'accordion__panel-1') # 2 ответ
    ANSWER_3 = (By.ID, 'accordion__panel-2') # 3 ответ
    ANSWER_4 = (By.ID, 'accordion__panel-3') # 4 ответ
    ANSWER_5 = (By.ID, 'accordion__panel-4') # 5 ответ
    ANSWER_6 = (By.ID, 'accordion__panel-5') # 6 ответ
    ANSWER_7 = (By.ID, 'accordion__panel-6') # 7 ответ
    ANSWER_8 = (By.ID, 'accordion__panel-7') # 8 ответ
    QUESTION_1 = (By.ID, 'accordion__heading-0') # 1 вопрос
    QUESTION_2 = (By.ID, 'accordion__heading-1') # 2 вопрос
    QUESTION_3 = (By.ID, 'accordion__heading-2') # 3 вопрос
    QUESTION_4 = (By.ID, 'accordion__heading-3') # 4 вопрос
    QUESTION_5 = (By.ID, 'accordion__heading-4') # 5 вопрос
    QUESTION_6 = (By.ID, 'accordion__heading-5') # 6 вопрос
    QUESTION_7 = (By.ID, 'accordion__heading-6') # 7 вопрос
    QUESTION_8 = (By.ID, 'accordion__heading-7') # 8 вопрос