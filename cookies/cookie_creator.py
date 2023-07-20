from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class CookieCreator:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    def get_yandex_cookies(self):
        browser_driver = webdriver.Chrome(options=self.chrome_options)

        browser_driver.get('https://market.yandex.ru')

        time.sleep(10)

        elements = [
            '/html/body/div[1]/div/div/form/div[3]/div/div/div[1]/input',
            '/html/body/div[2]/header/div/div/div/noindex[2]/nav/ul/li[5]/div/div/div/div[1]/a',
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[2]/div[2]/div/div/span/input',
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div/form/div/div[3]/div[2]/button',
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[2]/div[2]/div[1]/span/input',
            '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/div[1]/button',
        ]

        for index, element_xpath in enumerate(elements):
            buttons = browser_driver.find_elements(By.XPATH, element_xpath)

            if len(buttons) > 0:
                if index == 0:
                    buttons[0].click()
                    time.sleep(7)
                    self.log_message('Капча найдена и уничтожена', 100)
                elif index == 1:
                    buttons[0].click()
                    time.sleep(7)
                    self.log_message('Кнопка Войти найдена и отжата', 100)
                elif index == 2:
                    buttons[0].send_keys('BotBotnikov')
                    time.sleep(2)
                    self.log_message('Логин введен', 100)
                elif index == 3:
                    buttons[0].click()
                    time.sleep(7)
                    self.log_message('Отжата кнопка Далее', 100)
                elif index == 4:
                    buttons[0].send_keys('Bot4Botnikov')
                    time.sleep(2)
                    self.log_message('Пароль введен', 100)
                elif index == 5:
                    buttons[0].click()
                    time.sleep(7)
                    self.log_message('Кнопка войти отжата', 100)
            else:
                print(f'Кнопка с xpath {element_xpath} не найдена.')

        cookies = {}
        for c in browser_driver.get_cookies():
            cookies.update({c['name']: c['value']})
        
        m_c = None
        if cookies.get('Session_id', None):
            m_c = {'Session_id': cookies.get('Session_id')}

        sk = None
        for request in browser_driver.requests:
            if 'sk' in request.headers:
                sk = request.headers['sk']
        m_h = None
        m_h = {
            'sk': sk,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        if sk and m_c:
            return m_c, m_h
        else:
            return None

    def log_message(self, message: str, row_length: int):
        print(message.ljust(row_length), end='\r')

