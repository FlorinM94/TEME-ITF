'''Alege-ți unul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare)
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
chrome=webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.ID,'first-name').send_keys('Micle') #Selector by ID
chrome.find_element(By.ID,'last-name').send_keys('Florin') #Selector by ID
chrome.find_element(By.ID,'job-title').send_keys('Automation Software Tester') #Selector by ID
chrome.find_element(By.CSS_SELECTOR,'input#radio-button-1').click() # CSS Selector by ID
chrome.find_element(By.CSS_SELECTOR,'input[value="radio-button-2"]').click() # CSS Selector by atribute=value
input_list=chrome.find_elements(By.TAG_NAME,'input')
input_list[5].click() # Selector by TAG NAME
input_list[6].click() #Selector by TAG NAME
input_list[7].click() #Selector by TAG NAME
input_list[8].click() #Selector by TAG NAME
chrome.find_elements(By.CLASS_NAME,'form-control')[0].click()
selectVal=Select(chrome.find_elements(By.CLASS_NAME,'form-control')[3]) #Selector by CLASS NAME
chrome.find_elements(By.CLASS_NAME)
selectVal.select_by_value('1')
chrome.find_elements(By.CLASS_NAME,'form-control')[4].send_keys('01/02/2023') #Selector by CLASS NAME
chrome.find_element(By.LINK_TEXT,'Submit').click() #Selector by Link Text
sleep(3)
chrome.quit()
chrome=webdriver.Chrome()
chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT,'Redirect Link').click() #Selector by Link Text
chrome.find_element(By.LINK_TEXT,'here').click() #Selector by Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT,'30').click() #Selector by Partial Link Text
sleep(3)
chrome.quit()
chrome=webdriver.Chrome()
chrome.get('https://www.browserstack.com/guide/css-selectors-in-selenium')

element1 = chrome.find_element(By.CSS_SELECTOR, '#toc0') #css locator by ID
print(element1.text)

element2 = chrome.find_element(By.CSS_SELECTOR, '.guide-toc') #css locator by class
print(element2.text)

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

element3 = chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="first name"]').send_keys('Kylie')

chrome=webdriver.Chrome()
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.XPATH,"//input[@name='firstname']").send_keys('Micle') #Selector by XPATH -atribut=valoare
chrome.find_element(By.XPATH,"//input[@name='lastname']").send_keys('Florin ') #Selector by XPATH -atribut=valoare
chrome.find_elements(By.XPATH,"//input[@name='sex']")[0].click() #Selector by XPATH folosind o lista
chrome.find_element(By.XPATH,"//input[@id='exp-4']").click() #Selector by XPATH -atribut=valoare
chrome.find_element(By.XPATH,"//div/div/input[@id='datepicker']").send_keys('06/04/2023') #identificare prin xpath relativ catre copilul tagului specificat
chrome.find_element(By.XPATH,'//div/div/input[@id="profession-1"]').click()
chrome.find_elements(By.XPATH,'//input[@name="tool"]')[2].click()
chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').click() #XPATH by Partial Text
sleep(5)
chrome.quit()
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
def select_element(xpath_element):
    for i in range(1,7):
        chrome.find_element(By.XPATH,f'{xpath_element}{i}"]').click()
select_element('//input[@id="exp-')
sleep(10)

