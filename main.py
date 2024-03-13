import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constantes do projeto
load_dotenv()
ru = os.getenv("RU")
senha = os.getenv("SENHA")

print('1 - FDS')
print('2 - MAC')
disciplina_INT = int(input('Digite qual disciplina você quer registrar presença.\n'))
if disciplina_INT == 1:
    disciplina = 'Fundamentos de Desenvolvimento de Software'
elif disciplina_INT == 2:
    disciplina = 'Matemática Aplicada à Computação'


def filtrar_curso(cursos):
    if cursos.text == 'GRAD - TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - TELEPRESENCIAL - EAD':
        return True
    else:
        return False


def filtrar_disciplina(disciplinas):
    if disciplinas.text == disciplina:
        return True
    else:
        return False


driver = webdriver.Chrome()

driver.get("https://univirtus.uninter.com/ava/web/")

# Busca pelo input de RU e insere o seu Registro Uninter.
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#ru"))
).send_keys(ru)

# Busca pelo input de senha e insere sua senha.
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input#senha"))
).send_keys(senha)

# Clica no botão de login.
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button#loginBtn"))
).click()

# Clica no linnk para o AVA.
# Tive que esperar 3 segundos pois existe um animação no elemento que as vezes dava um erro na busca do elemento.
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a#loginBoxAva"))
).click()

# Trata as notificações que aparecem quando logamos.
button_fechar_modal = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button#fecharModalPopup'))
)
while button_fechar_modal is not None:
    button_fechar_modal.click()
    driver.refresh()
    try:
        button_fechar_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button#fecharModalPopup'))
        )
    except TimeoutException:
        button_fechar_modal = None

# Seleciona o curo de ADS.
cursos = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "link-curso"))
)
curso_ads = list(filter(filtrar_curso, cursos))
curso_ads[0].click()

# Seleciona a disciplina que irá arcar presença.
disciplinas = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "link-disciplina"))
)
disciplina = list(filter(filtrar_disciplina, disciplinas))
disciplina[0].click()

# Clica no botão de frequencia.
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a#diarioClasseFrequenciaAluno>span"))
).click()

# Marca presença.
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button#marcarPresenca"))
).click()

driver.quit()

print("Presença comfirmada")
