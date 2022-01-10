from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time
from playsound import playsound

browser = webdriver.Chrome(ChromeDriverManager().install())


while True:
    try:
        browser.get("https://enabiz.gov.tr")  # burayı neden while içine aldıgımı hatırlamıyorum ama vardır bir şey :D 
        time.sleep(5)
        browser.find_element_by_name("TCKimlikNo").send_keys("tc") 
        time.sleep(5)
        browser.find_element_by_name("Sifre").send_keys("e nabiz sifresi")
        time.sleep(5)
        browser.find_element_by_id("btnGiris").click()
        time.sleep(10)
        browser.find_element_by_css_selector(".mobil-menu-item.bg4").click()
        time.sleep(10)
        browser.find_element_by_xpath("//*[text()='COVID-19 Test Sonucu']").click()
        time.sleep(10)
        # print(len(browser.find_elements_by_xpath("//*[text()='NEGATIF']")))
        if (
            len(browser.find_elements_by_xpath("//*[text()='NEGATIF']")) > 3
        ):  # önceden aldıgınız negatif test sonuclarının sayısı
            playsound("./xx.mp3")
            break
        elif browser.find_element_by_xpath("//*[text()='POZITIF']"):
            # elif len(browser.find_element_by_xpath("//*[text()='POZITIF']") > 1):  #önceden pozitif testiniz var ise üstteki elif i cıakrtıp buraya kaç pozitif sonucunuz oldugunu yazn pls
            playsound("./xx.mp3")
            break
    except:
        print("bişe yok bişe yok devam")
