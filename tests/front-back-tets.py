import time

from selenium import webdriver, common as se_common
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import webapp


def start_tg():
    options = Options()
    options.add_argument("--user-data-dir=C:\\PycharmProjects\\pythonProject4\\chrome_data")
    driver = webdriver.Chrome(options=options)
    driver.get('https://web.telegram.org/k/')
    return driver


def test_sender():
    driver_tg = start_tg()
    time.sleep(2)
    driver_webapp = webapp.go_to_chat_page()
    chats = driver_tg.find_elements(By.CLASS_NAME, 'chatlist-chat.rp')
    chats[0].click()
    time.sleep(2)
    messages = driver_tg.find_elements(By.CLASS_NAME, 'bubbles-group')
    try:
        assert messages[-1].find_element(By.CLASS_NAME, 'message').text.split('\n')[0] == 'Новый вопрос'
    except se_common.exceptions.NoSuchElementException:
        raise Exception('Sender bot did not send question to the group chat')
    except AssertionError:
        raise Exception('Sender bot send wrong question to the group chat')
    input_field = driver_tg.find_element(By.CLASS_NAME, 'input-message-input.scrollable.scrollable-y'
                                                        '.i18n.no-scrollbar')
    input_field.send_keys('@seemlessSupport_heh_bot /Получить вопрос')
    driver_tg.find_element(By.CLASS_NAME, 'btn-icon.tgico-none.btn-circle.z-depth-1.'
                                          'btn-send.animated-button-icon.rp.send').click()
    time.sleep(1)
    try:
        messages = driver_tg.find_elements(By.CLASS_NAME, 'bubbles-date-group')
        messages[-1].find_elements(By.CLASS_NAME, 'bubbles-group')[
            -1].find_elements(By.CLASS_NAME, 'reply-markup-row')[0].click()
    except se_common.exceptions.NoSuchElementException:
        raise Exception('Redirect bot does not working')
    time.sleep(1)
    chats[1].click()
    time.sleep(1)
    try:
        choice_buttons = driver_tg.find_elements(By.CLASS_NAME,
                                                 'bubbles-group')[-1].find_elements(By.CLASS_NAME, 'reply-markup-row')
        choice_buttons[0].click()
    except se_common.exceptions.NoSuchElementException:
        raise Exception('Question was not redirected or buttons did not appear')
    time.sleep(1)
    driver_tg.find_element(By.CLASS_NAME,
                           'input-message-input.scrollable.scrollable-y.i18n.no-scrollbar') \
        .send_keys('No')
    driver_tg.find_element(By.CLASS_NAME, 'btn-icon.tgico-none.btn-circle.z-depth-1.btn-send.'
                                          'animated-button-icon.rp.send').click()
    choice_buttons[1].click()
    time.sleep(5)
    assert driver_webapp.find_elements(By.CLASS_NAME, 'message')[1].text == 'No'
