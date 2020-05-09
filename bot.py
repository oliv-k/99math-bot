from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 99math's numpad
def buttons(button):
    if button == '1':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[1]').click()
    elif button == '2':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
    elif button == '3':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/button[3]').click()
    elif button == '4':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[1]').click()
    elif button == '5':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[2]').click()
    elif button == '6':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]/button[3]').click()
    elif button == '7':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[1]').click()
    elif button == '8':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[2]').click()
    elif button == '9':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[3]/button[3]').click()
    elif button == '-':
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/button[1]').click()
    else:
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]/button[2]').click()

# does a calculaton based on the symbol
def arvutus(tehe, arv1, arv2):
    if tehe == '-':
        vastus = arv1 - arv2
    elif tehe == '+':
        vastus = arv1 + arv2
    elif tehe == 'x':
        vastus = arv1 * arv2
    else:
        vastus = arv1 // arv2
    return str(vastus)

# waits until the answer button is clickable
# and also starts the main code
def ootamine():
    wait.until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/button[2]')))
    sleep(5)
    põhiosa()

# this part does all the main work
def põhiosa():
    while True:
        # get the operaton and split it to 3 parts
        try:
            tehe = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/h2').text
        except:
            wait()

        tehe = tehe.split(' ')

        # call the function to make the calculation
        vastus = arvutus(tehe[1], int(tehe[0]), int(tehe[2]))

        # click the buttons basedon the answer
        for i in range(len(list(vastus))):
            try:
                buttons(vastus[i])
            except:
                wait()

        # click on the answer button
        try:
            driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/button[2]').click()
        except:
            wait()

# asks the user for game code and username
code = input('Sisestage mängu kood: ')
name = input('Sisestage oma nimi: ')

# opening the browser
driver = webdriver.Firefox()
driver.get('http://www.99math.com/join/' + code)

# browsers wait time
wait = WebDriverWait(driver, 30)

# entering the username and joining the game
driver.find_element_by_xpath('/html/body/div[1]/div/div/input').send_keys(name + '🤖')
driver.find_element_by_xpath('/html/body/div[1]/div/div/button').click()

# waits and then starts the main code
wait()
