from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://statistici.insse.ro:8077/tempo-online/#/pages/tables/insse-table")
# iau elementele finale(ex: 1, 2, 3, 4 ...)
ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "level2")))
elements = driver.find_elements(By.CLASS_NAME,"level2")
driver.execute_script("document.getElementsByTagName('nb-layout-header')[0].style.display = 'none';")

quotes = len(elements)
# parcurge prima pagina
for quote in range(quotes):
    # ia toate elementele din prima pagina
    elements = driver.find_elements(By.CLASS_NAME,"level2")
    # da click pe fiecare element in parte din prima pagina
    elements[quote].click()
    # asteapta sa se incarce pagina

    # cauta toate elementele de pe a doua pagina
    ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "pointerContext")))
    elements_2 = driver.find_elements(By.CLASS_NAME,"pointerContext")
    pag2Nr = len(elements_2)

    # pentru fiecare element de pe pagina a doua
    for index_2 in range(pag2Nr):
        ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "pointerContext")))
        # ia toate elemenetele de pe pagina a doua
        elements_2 = driver.find_elements(By.CLASS_NAME,"pointerContext")
        # click pe elementul corespunzator
        elements_2[index_2].click();
        # asteapta sa se incarce pagina 3
        ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//th[@ng2-st-checkbox-select-all]")))
        # ia toate select all-urile
        selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
        nrAllOption = len(selectAllOptions)
        index_3 = 1
        if nrAllOption > 2:
            selectAllOptions[2].click()
        selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
        for index_3 in range(nrAllOption):
            selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
            if index_3 != 2:
                selectAllOptions[index_3].click()

        # apasa buton search
        button_search = driver.find_elements(By.CLASS_NAME,"searchCard")
        button_search[0].click()
        # asteapta sa se incarce pagina cu fisierul final
        ok = 1;
        index_while = 0;
        while ok == 1:
            try:
                ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "exportButtons")))
                ok = 0;
            except:
                selectAllOptions = driver.find_elements(By.XPATH,"//th[@ng2-st-checkbox-select-all]")
                # daca pagina nu se poate incarca, presupunem ca sunt prea multe randuri selectate
                # deselectez toate optiunile din prima categorie de optiuni si apoi selectez totalul din prima optiune
                # deselectez o optiune principala
                selectAllOptions[index_while].click()
                time.sleep(1)
                # selectez o optiune de total
                selectAllSubOptions = driver.find_elements(By.CSS_SELECTOR,"table > tbody > tr > td");
                selectAllSubOptions[index_while].click()
                time.sleep(1)

                button_search = driver.find_elements(By.CLASS_NAME,"searchCard")
                button_search[0].click()
                time.sleep(1)
                index_while = index_while + 1;

        ele = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "exportButtons")))
        # descarca fisier CSV
        button_export = driver.find_elements(By.CLASS_NAME,"exportButtons")
        if button_export[2].is_enabled():
            button_export[2].click()
        time.sleep(3)

        # intoarce-te pe pagina 2
        elements_3 = driver.find_elements(By.CSS_SELECTOR,"nb-card-body > td > .historyBarButton > button > span")
        time.sleep(1)
        if elements_3[3].is_enabled():
            elements_3[3].click()

    driver.refresh();
    time.sleep(3)
    driver.execute_script("document.getElementsByTagName('nb-layout-header')[0].style.display = 'none';")
    time.sleep(1)

#driver.close()