from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

chromedriver = r"./chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://sullygnome.com/channel/{}/30".format("thatjaxboxchick"))
driver.find_element_by_xpath("//*[@id=\"divtoplinkcontainer\"]/div[2]").click()
time.sleep(0.5)

soup = BeautifulSoup(driver.page_source, "html.parser")
results = soup.find_all("div",{"class":["InfoPanelCombinedRow","InfoPanelCombinedRowAlt"]})
for r in results:
	hold_r = r.find("div",{"class":"InfoPanelCombinedRowCellMedium InfoPanelCombineFirst"})
	if (hold_r != None):
		if(hold_r.find("div",{"class":"InfoPanelCellImageText"}).text == "Core"):
			print(r.find_all("div",{"class":"InfoPanelCombinedRowCell"})[0].text)
		