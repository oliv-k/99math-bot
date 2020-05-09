# impordime kõik vajalikud osad
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def nupud(nupp):
    # kõik nupud mida läheb vastuse sisestamiseks vaja
    if nupp == '1':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[1]').click()
    elif nupp == '2':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
    elif nupp == '3':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[3]').click()
    elif nupp == '4':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[1]').click()
    elif nupp == '5':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[2]').click()
    elif nupp == '6':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[3]').click()
    elif nupp == '7':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[1]').click()
    elif nupp == '8':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[2]').click()
    elif nupp == '9':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[3]').click()
    elif nupp == '-':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/button[1]').click()
    else:
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/button[2]').click()

def arvutus(tehe, arv1, arv2):
    # teeb tehte märgi jaärgi
    # kasutades kahte saadut arvu
    if tehe == '-':
        vastus = arv1 - arv2
    elif tehe == '+':
        vastus = arv1 + arv2
    elif tehe == 'x':
        vastus = arv1 * arv2
    else:
        vastus = arv1 // arv2
    # tagastame tehte vastuse
    return str(vastus)

def ootamine():
    # ootab kuni saab alustada tõõtamist
    oota.until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/button[2]')))
    sleep(5)
    põhiosa()

def põhiosa():
    # alustame tsükli
    while True:
        # saame tehte tekstina ja lõikame selle 3-ks jupiks
        try:
            tehe = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/h2').text
        except:
            ootamine()

        tehe = tehe.split(' ')

        # kutsume funktsiooni millega saame vastuse
        vastus = arvutus(tehe[1], int(tehe[0]), int(tehe[2]))

        # kui vastuses on rohkem kui 1 arv lõikame selle juppideks
        # ja vajutame nupp(e/u) vastavalt arvule
        for i in range(len(list(vastus))):
            try:
                nupud(vastus[i])
            except:
                ootamine()

        # kui vastus sisestatud vajutame edasi nupule
        try:
            driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/button[2]').click()
        except:
            ootamine()

# Küsime kasutajalt mängu koodi ja kasutajanime
kood = input('Sisestage mängu kood: ')
nimi = input('Sisestage oma nimi: ')

# Avame brauseri
driver = webdriver.Firefox()
driver.get('http://www.99math.com/join/' + kood)

# brauseri ootamise aeg
oota = WebDriverWait(driver, 30)

# Sisestame nime
driver.find_element_by_xpath('/html/body/div[1]/div/div/input').send_keys(nimi + '🤖')

# Vajutame nupule
driver.find_element_by_xpath('/html/body/div[1]/div/div/button').click()

# ootab ja siis alustab terve koodi
ootamine()
