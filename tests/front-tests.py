import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def start_working():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get('http://127.0.0.1:8000/')
    except selenium.common.exceptions.WebDriverException:
        raise Exception('The page does not respond')
    try:
        input_field = driver.find_element(By.CLASS_NAME, 'question-box')
        input_field.send_keys('Registration')
        input_field.submit()
        time.sleep(2)
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There is no input field')
    return driver


def go_to_chat_page():
    driver = start_working()
    try:
        output_window = driver.find_element(By.CLASS_NAME, 'ask-volunteer')
        output_window.click()
        time.sleep(1)
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There are no "ask volunteer" field')
    return driver


def test_ans_from_db():
    driver = start_working()
    try:
        options = driver.find_elements(By.CLASS_NAME, 'option')
        options[0].click()
        time.sleep(1)
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There are no options')
    try:
        messages = driver.find_elements(By.CLASS_NAME, 'message')
        assert messages[0].text == "How to continue my registration?"
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There is no message window')
    except AssertionError:
        raise Exception('Different text is loaded from data base')


def test_ans_from_vol():
    driver = go_to_chat_page()
    try:
        input_field = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/form/input')
        send_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[3]/form/button')
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There is no input field or "send" button')
    try:  # check if an empty input field create an output window
        time.sleep(1)
        messages = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]')
        raise Exception('Has an empty message window')
    except selenium.common.exceptions.NoSuchElementException:
        pass
    # check if a nonempty input field create an output window
    input_field.send_keys('Is Israel a legitimate state?')
    send_button.click()
    try:
        output = driver.find_elements(By.CLASS_NAME, 'message')[-1]
        assert output.text == 'Is Israel a legitimate state?'
    except selenium.common.exceptions.NoSuchElementException:
        raise Exception('There is no output window')
    except AssertionError:
        raise Exception('Text in output window is different from the input')
    driver.quit()
