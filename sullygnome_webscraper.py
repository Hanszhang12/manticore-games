from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

def scrape_name(name):
	driver.get("https://sullygnome.com/channel/{}/30".format(name))
	driver.find_element_by_xpath("//*[@id=\"divtoplinkcontainer\"]/div[2]").click()
	time.sleep(0.5)

	soup = BeautifulSoup(driver.page_source, "html.parser")
	results = soup.find_all("div",{"class":["InfoPanelCombinedRow","InfoPanelCombinedRowAlt"]})
	for r in results:
		hold_r = r.find("div",{"class":"InfoPanelCombinedRowCellMedium InfoPanelCombineFirst"})
		if (hold_r != None):
			if(hold_r.find("div",{"class":"InfoPanelCellImageText"}).text == "Core"):
				return (r.find_all("div",{"class":"InfoPanelCombinedRowCell"})[0].text), ((r.find_all("div",{"class":"InfoPanelCombinedRowCell"})[2].text)
	driver.find_element_by_xpath("//*[@id=\"combinedPanel\"]/div/div[3]/a").click()
    time.sleep(0.1)
    
    more_soup = BeautifulSoup(driver.page_source, "html.parser")
    table = more_soup.find("table", {"id":"tblControl"}).find("tbody").find_all("tr")
    for row in table:
        tds = row.find_all("td")
        if (tds[1].contents[0].contents[0]["data-gamename"]=="Core"):
            return (tds[2].text, tds[4].text)
		
		
def scrape_list(names_list):
	
	chromedriver = r"./chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(ChromeDriverManager().install())
	
	results = []
	for n in names_list:
		results.append(scrape_name(n))
	driver.close()
	return results