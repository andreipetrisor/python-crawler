from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
#driver.maximize_window()
driver.get("http://statistici.insse.ro:8077/tempo-online/#/pages/tables/insse-table")
# iau elementele finale(ex: 1, 2, 3, 4 ...)
ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "level2")))
elements = driver.find_elements(By.CLASS_NAME,"level2")
driver.execute_script("document.getElementsByTagName('nb-layout-header')[0].style.display = 'none';")

quotes = len(elements)
f = open("andrei.txt", "w");
# parcurge prima pagina
for quote in range(quotes):
    # ia toate elementele din prima pagina
    elements = driver.find_elements(By.CLASS_NAME,"level2")
    # da click pe fiecare element in parte din prima pagina
    path_first = '';
    path_first = elements[quote].get_attribute('innerHTML');
    
    if "COMPETENTE TIC SI CEREREA PENTRU CUNOSTINTE TIC IN INTREPRINDERI" in path_first:
        continue;
    if "CURSURI SI PROGRAME DE FORMARE TIC" in path_first:
        continue;
    if "E-COMERT" in path_first:
        continue;
    if "CONECTAREA LA INTERNET" in path_first:
        continue;
    if "WEBSITE SI UTILIZAREA RETELELOR SOCIALE" in path_first:
        continue;
    if "E-BUSINESS" in path_first:
        continue;
    if "SECURITATEA TIC" in path_first:
        continue;

    elements[quote].click()
    # asteapta sa se incarce pagina
    elements_2 = [];
    # cauta toate elementele de pe a doua pagina
    try:
        ele = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "pointerContext")))
        elements_2 = driver.find_elements(By.CLASS_NAME,"pointerContext")
    except:
        print('Pagina goala');
    pag2Nr = len(elements_2)
    
    # pentru fiecare element de pe pagina a doua
    for index_2 in range(pag2Nr):
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pointerContext")))
        # ia toate elemenetele de pe pagina a doua
        elements_2 = driver.find_elements(By.CLASS_NAME,"pointerContext")
        # click pe elementul corespunzator
        path_secound =  " - " + elements_2[index_2].get_attribute('innerHTML') + '\n';
        elements_2[index_2].click();
        time.sleep(0.5)
        # asteapta sa se incarce pagina 3
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//th[@ng2-st-checkbox-select-all]")))
        # ia toate select all-urile
        selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
        nrAllOption = len(selectAllOptions)
        selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
        for index_3 in range(nrAllOption):
            selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
            driver.execute_script("arguments[0].scrollIntoView();", selectAllOptions[index_3])
            time.sleep(0.5)
            selectAllOptions[index_3].click()

        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "searchCard")))
        # apasa buton search
        button_search = driver.find_elements(By.CLASS_NAME,"searchCard")
        button_search[0].click()

        try:
            ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "exportButtons")))
            # descarca fisier CSV
            button_export = driver.find_elements(By.CLASS_NAME,"exportButtons")
            if button_export[1].is_enabled():
                driver.execute_script("arguments[0].scrollIntoView();", button_export[1])
                time.sleep(0.5)
                button_export[1].click()
            time.sleep(3)
        except:
            f.write(path_first + path_secound)

        # intoarce-te pe pagina 2
        elements_3 = driver.find_elements(By.CSS_SELECTOR,"nb-card-body > td > .historyBarButton > button > span")
        time.sleep(0.5)
        
        driver.execute_script("arguments[0].scrollIntoView();", elements_3[3])
        time.sleep(0.5)
        if elements_3[3].is_enabled():
            elements_3[3].click()

    driver.refresh();
    time.sleep(3)
    driver.execute_script("document.getElementsByTagName('nb-layout-header')[0].style.display = 'none';")
    time.sleep(1)

f.close()
driver.close()