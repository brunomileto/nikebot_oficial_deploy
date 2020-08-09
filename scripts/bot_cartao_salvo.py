import sys
import six

import logging.config
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
# from PyQt5 import QtWidgets, uic
from datetime import timedelta
import datetime
import sys
import time
import logging.config
from selenium import webdriver


logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [PID %(process)d] [Thread %(thread)d] [%(levelname)s] [%(name)s] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": [
            "console"
        ]
    }
})

NIKE_HOME_URL = "https://www.nike.com.br/"
LOGGER = logging.getLogger()


class Data:
    email = "brunomill3003@gmail.com"
    shoe_link = "https://www.nike.com.br/Snkrs/Produto/PG-4-PCG/153-169-211-256112"
    password = "Miletominarlz1"
    shoe_size = "43"
    card_number = "5328203212793353"
    sec_code = '001'
    card_name = 'BABA M D A'
    cpf = '123.456.789-10'
    card_month = '10'
    card_year = '2022'
    installment = '2'
    years_list = [2020, 2021, 2022, 2023, 2024, 2025, 2026,
                  2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034]
    for index in range(len(years_list)):
        if str(years_list[index]) == card_year:
            card_year_path = str(index+2)

    # -----> TIME < -------
    init_hour = '10'
    init_minute = '00'
    # ----------------------------------------------------
    login_time = '5'
    release_time = '5'
    screenshot_path = './bin/final.png'
    html_path = './bin/final.html'
    options = webdriver.ChromeOptions()

    options.headless = False

    chrome_prefs = {}
    options.experimental_options['prefs'] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    executable_path = "./chromedriver.exe"

    xpath_login = "//*[@id='anchor-acessar']"
    xpath_email = "/html/body/div[9]/div/div/div[2]/div[5]/form/div[2]/input"
    xpath_password = "/html/body/div[9]/div/div/div[2]/div[5]/form/div[3]/input"
    xpath_login_button = "/html/body/div[9]/div/div/div[2]/div[5]/form/div[6]/input"
    xpath_shoe_size = f"//label[@for='tamanho__id{shoe_size}']"
    xpath_add_to_cart = '//*[@id="btn-comprar"]'
    xpath_continue_payment = "//*[@id='carrinho']/div[4]/div/div[4]/a"
    xpath_proceed_to_payment = '/html/body/main/div/div[3]/div[4]/div[5]/button'
    xpath_confirm_n_proceed = '//button[text()="Confirmar e prosseguir"]'
    xpath_card_number = "//*[@id='ccard-number']"
    xpath_card_name = "//*[@id='ccard-owner']"
    xpath_cpf = "//*[@id='ccard-document']"
    xpath_card_month_field = '//*[@id="exp-month"]'
    xpath_card_month = f'//*[@id="exp-month"]/option[{card_month}]'
    xpath_card_year_field = '//*[@id="exp-year"]'
    xpath_card_year = f'//*[@id="exp-year"]/option[{card_year_path}]'
    xpath_security_code = "//*[@id='security-code']"
    xpath_installment_field = '//*[@id="installments"]'
    xpath_installment = f'//*[@id="installments"]/option[{installment}]'
    xpath_checkbox = "//*[@id='politica-trocas-label']"
    xpath_buy_button = "/html/body/main/div/div[3]/div[8]/div[2]/div[4]/button"

    xpath_saved_card = '//*[@id="cartoes-salvos"]/div/div[2]'
    xpath_card = '//*[@id="cartoes-salvos"]/ul/li/label/h4'
    xpath_installment_field_saved_card = '//*[@id="saved-card-installments"]'
    xpath_installment_saved_card = f'//*[@id="saved-card-installments"]/option[{installment}]'

    def start_driver(self):
        LOGGER.info('Iniciando Driver!')
        nike_shoe.driver = webdriver.Chrome(
            executable_path=nike_shoe.executable_path, options=nike_shoe.options)
        LOGGER.info('Maximizando Janela, se houver')
        nike_shoe.driver.maximize_window()
        nike_shoe.open_url(NIKE_HOME_URL)

    def login_time_func(self):
        if nike_shoe.login_time:
            LOGGER.info('Esperando tempo para login')
            time.sleep(float(nike_shoe.login_time))

    def release_time_func(self):
        if nike_shoe.release_time:
            LOGGER.info('Esperando tempo para finalizar login')
            time.sleep(float(nike_shoe.release_time))

    def start_time_calculation(self):
        hour_to_run = int(nike_shoe.init_hour)
        minute_to_run = int(nike_shoe.init_minute)
        nike_shoe.time_to_run = timedelta(
            hours=hour_to_run, minutes=minute_to_run)
        nike_shoe.time_to_run = (
            datetime.datetime.min + nike_shoe.time_to_run).time()

        LOGGER.info(
            f'Esperando até às {nike_shoe.time_to_run} horas, para iniciar o programa!')

    def start_time(self):
        while datetime.datetime.now().time().replace(microsecond=0) < nike_shoe.time_to_run:
            time.sleep(1)
        LOGGER.info('Iniciando....')
        nike_shoe.init_time = time.time()

    def refresh_page_info(self):
        LOGGER.info('Atualizando página, até tênis ficar disponível!')

    def check_if_shoe_available(self):
        while True:
            try:
                nike_shoe.click_element_xpath(
                    nike_shoe.xpath_shoe_size, 'Tênis Disponível?!')
                break
            except Exception:
                nike_shoe.open_url(nike_shoe.shoe_link)

    def end_time(self):
        nike_shoe.finit_time = time.time()
        LOGGER.info(
            f'Tênis Comprado! Operação durou {nike_shoe.finit_time - nike_shoe.init_time} segundos!')

    def save_screenshot_func(self):
        LOGGER.info('Salvando print da tela...')
        nike_shoe.driver.save_screenshot(nike_shoe.screenshot_path)

    def save_html_func(self):
        LOGGER.info('Salvando arquivo html da compra...')
        with open(nike_shoe.html_path, 'w') as f:
            f.write(nike_shoe.driver.page_source)

    # -------- Funções Gerais ----------
    def open_url(self, url):
        try:
            LOGGER.info('Tentando Abir: ' + url)
            nike_shoe.driver.get(url)
        except TimeoutException:
            LOGGER.info(
                'Página demorou muito para responder, continuando mesmo assim!')

    def click_element_xpath(self, xpath, log_name):
        try:
            LOGGER.info(f'Tentando clicar no elemento: {log_name}')
            nike_shoe.wait_until_visible(log_name, xpath, duration=3)
            element = nike_shoe.driver.find_element_by_xpath(xpath)
            nike_shoe.driver.execute_script('arguments[0].click();', element)
            LOGGER.info(f'Clicando em: {log_name}')
        except Exception as err:
            time.sleep(2)
            LOGGER.info(f'Exception no {log_name}. Tentando novamente')
            element = nike_shoe.driver.find_element_by_xpath(xpath)
            nike_shoe.driver.execute_script('arguments[0].click();', element)
            LOGGER.info(f'Clicando em: {log_name}')

    def wait_until_visible(self, elemento, xpath=None, class_name=None, duration=10000, frequency=0.01):
        LOGGER.info(f'Esperando {elemento}, ficar visível.')
        if xpath:
            WebDriverWait(nike_shoe.driver, duration, frequency).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        elif class_name:
            WebDriverWait(nike_shoe.driver, duration, frequency).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))

    def insert_data(self, xpath, data, name):
        LOGGER.info(f'Tentando inserir os dados: {name}')
        try:
            nike_shoe.wait_until_visible(name, xpath, duration=3)
            data_input = nike_shoe.driver.find_element_by_xpath(xpath)
            try:
                data_input.clear()
            except:
                pass
            data_input.send_keys(data)
            LOGGER.info('ESPEROU ATÉ FICAR VISÍVEL')
            LOGGER.info(f'Dados {name}, inseridos!')
        except Exception:
            time.sleep(2)
            data_input = nike_shoe.driver.find_element_by_xpath(xpath)
            try:
                data_input.clear()
            except:
                pass
            data_input.send_keys(data)
            LOGGER.info('ESPEROU OS 2 SEGUNDOS')
            LOGGER.info(f'Dados {name}, inseridos!')

    def function_try(self, function, *args):
        while True:
            try:
                function(*args)
                break
            except Exception as e:
                LOGGER.warning('Erro!!!!!!!!!!!!!')
                time.sleep(3)
                LOGGER.warning('Tentando Novamente')

    def select_dropdown_value(self, xpath_field, value, name):
        LOGGER.info(name)
        selector = nike_shoe.driver.find_element_by_xpath(xpath_field)
        nike_shoe.driver.execute_script("arguments[0].click();", selector)
        time.sleep(2)
        select_field = Select(
            nike_shoe.driver.find_element_by_xpath(xpath_field))
        select_field.select_by_value(value)

    def click_normal(self, xpath, log_name):
        try:
            LOGGER.info(f'Tentando clicar no elemento: {log_name}')
            nike_shoe.wait_until_visible(log_name, xpath, duration=3)
            nike_shoe.driver.find_element_by_xpath(xpath).click()
            LOGGER.info(f'Clicando em: {log_name}')
        except Exception as err:
            time.sleep(2)
            LOGGER.info(f'Exception no {log_name}. Tentando novamente')
            element = nike_shoe.driver.find_element_by_xpath(xpath)
            nike_shoe.driver.execute_script('arguments[0].click();', element)
            LOGGER.info(f'Clicando em: {log_name}')


nike_shoe = Data()
# nike_shoe.start_driver()
# nike_shoe.login_time_func()
# # nike_shoe.login()
# LOGGER.warning('VOCE POSSUI 45 SEGUNDOS PARA FAZER O LOGIN MANUALMENTE!')
# time.sleep(60)
# nike_shoe.release_time_func()
# nike_shoe.start_time_calculation()
# nike_shoe.start_time()
# nike_shoe.open_url(nike_shoe.shoe_link)
# nike_shoe.refresh_page_info()
# nike_shoe.check_if_shoe_available()
# nike_shoe.function_try(nike_shoe.click_element_xpath,
#                        nike_shoe.xpath_shoe_size, "Tamanho Tênis")
# nike_shoe.function_try(nike_shoe.click_element_xpath,
#                        nike_shoe.xpath_add_to_cart, "Botão Enviar para Carrinho")
# nike_shoe.function_try(nike_shoe.click_element_xpath,
#                        nike_shoe.xpath_continue_payment, "Botão Continuar")

# time.sleep(1)
# nike_shoe.function_try(nike_shoe.click_element_xpath,
#                        nike_shoe.xpath_proceed_to_payment, "Botão prosseguir para pagamento")

# time.sleep(1)
# nike_shoe.function_try(nike_shoe.click_element_xpath,
#                        nike_shoe.xpath_confirm_n_proceed, "Botão confirmar e prosseguir")

# nike_shoe.insert_data(nike_shoe.xpath_card_number,
#                       nike_shoe.card_number, "Número cartão")
# nike_shoe.insert_data(nike_shoe.xpath_card_name,
#                       nike_shoe.card_name, 'Nome Dono Cartão')
# nike_shoe.insert_data(nike_shoe.xpath_cpf, nike_shoe.cpf, 'CPF Dono Cartão')

# nike_shoe.click_normal(nike_shoe.xpath_card_month_field, 'Campo Mês Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_month, 'Mês Vencimento Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_year_field, 'Campo Ano Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_year, 'Ano Vencimento Cartão')

# # nike_shoe.select_dropdown_value(
# #     nike_shoe.xpath_card_month_field, nike_shoe.card_month, 'Mês Vencimento Cartão')
# # nike_shoe.select_dropdown_value(
# #     nike_shoe.xpath_card_year_field, nike_shoe.card_year, 'Mês Vencimento Cartão')

# nike_shoe.insert_data(nike_shoe.xpath_security_code,
#                       nike_shoe.sec_code, 'Cod Segurança Cartão')

# nike_shoe.click_normal(nike_shoe.xpath_installment_field, 'Campo Parcelas')
# nike_shoe.click_normal(nike_shoe.xpath_installment, 'Parcelamento')

# # nike_shoe.select_dropdown_value(
# #     nike_shoe.xpath_installment_field, nike_shoe.installment, 'Modo de pagamento')

# nike_shoe.click_element_xpath(
#     nike_shoe.xpath_checkbox, 'Botão Confirma Políticas de Troca')
# nike_shoe.click_element_xpath(
#     nike_shoe.xpath_buy_button, 'Botão Finalizar Compra!')
# nike_shoe.end_time()
# nike_shoe.save_screenshot_func()
# nike_shoe.save_html_func()
# LOGGER.info('Finalizando Programa....')

nike_shoe.start_driver()
nike_shoe.login_time_func()
# nike_shoe.login()
LOGGER.warning(
    'VOCE POSSUI 45 SEGUNDOS PARA FAZER O LOGIN MANUALMENTE!')
time.sleep(60)
nike_shoe.release_time_func()
nike_shoe.start_time_calculation()
nike_shoe.start_time()
nike_shoe.open_url(nike_shoe.shoe_link)
nike_shoe.refresh_page_info()
nike_shoe.check_if_shoe_available()
nike_shoe.function_try(nike_shoe.click_element_xpath,
                       nike_shoe.xpath_shoe_size, "Tamanho Tênis")
nike_shoe.function_try(nike_shoe.click_element_xpath,
                       nike_shoe.xpath_add_to_cart, "Botão Enviar para Carrinho")
nike_shoe.function_try(nike_shoe.click_element_xpath,
                       nike_shoe.xpath_continue_payment, "Botão Continuar")

time.sleep(2)
nike_shoe.function_try(nike_shoe.click_element_xpath,
                       nike_shoe.xpath_proceed_to_payment, "Botão prosseguir para pagamento")

time.sleep(2)
nike_shoe.function_try(nike_shoe.click_element_xpath,
                       nike_shoe.xpath_confirm_n_proceed, "Botão confirmar e prosseguir")

nike_shoe.click_element_xpath(
    nike_shoe.xpath_saved_card, 'Cartões Salvos')
nike_shoe.click_element_xpath(nike_shoe.xpath_card, 'Cartão Salvo!')

# nike_shoe.insert_data(nike_shoe.xpath_card_number,
#                  nike_shoe.card_cnumber, "Número cartão")
# nike_shoe.insert_data(nike_shoe.xpath_card_name,
#                  nike_shoe.card_name, 'Nome Dono Cartão')
# nike_shoe.insert_data(nike_shoe.xpath_cpf, nike_shoe.cpf, 'CPF Dono Cartão')

# nike_shoe.click_normal(nike_shoe.xpath_card_month_field, 'Campo Mês Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_month, 'Mês Vencimento Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_year_field, 'Campo Ano Cartão')
# nike_shoe.click_normal(nike_shoe.xpath_card_year, 'Ano Vencimento Cartão')

# # nike_shoe.select_dropdown_value(
# #     nike_shoe.xpath_card_month_field, nike_shoe.card_month, 'Mês Vencimento Cartão')
# # nike_shoe.select_dropdown_value(
# #     nike_shoe.xpath_card_year_field, nike_shoe.card_year, 'Mês Vencimento Cartão')

# nike_shoe.insert_data(nike_shoe.xpath_security_code,
#                  nike_shoe.security_card_code, 'Cod Segurança Cartão')

nike_shoe.click_normal(
    nike_shoe.xpath_installment_field_saved_card, 'Campo Parcelas')
nike_shoe.click_normal(
    nike_shoe.xpath_installment_saved_card, 'Parcelamento')

# nike_shoe.select_dropdown_value(
#     nike_shoe.xpath_installment_field, nike_shoe.installment, 'Modo de pagamento')

nike_shoe.click_element_xpath(
    nike_shoe.xpath_checkbox, 'Botão Confirma Políticas de Troca')
nike_shoe.click_element_xpath(
    nike_shoe.xpath_buy_button, 'Botão Finalizar Compra!')
nike_shoe.end_time()
nike_shoe.save_screenshot_func()
nike_shoe.save_html_func()
LOGGER.info('Finalizando Programa....')
