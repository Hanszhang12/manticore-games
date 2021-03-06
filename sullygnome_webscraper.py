from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

def scrape_name(name, driver):
    driver.get(name + '/30')
    if (driver.current_url == "https://sullygnome.com/"):
        return "-1 hrs", "-1"
    driver.find_element_by_xpath("//*[@id=\"divtoplinkcontainer\"]/div[2]").click()
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all("div",{"class":["InfoPanelCombinedRow","InfoPanelCombinedRowAlt"]})
    for r in results:
        hold_r = r.find("div",{"class":"InfoPanelCombinedRowCellMedium InfoPanelCombineFirst"})
        if (hold_r != None and hold_r.find("div",{"class":"InfoPanelCellImageText"}) != None and hold_r.find("div",{"class":"InfoPanelCellImageText"}).text == "Core"):
            return (r.find_all("div",{"class":"InfoPanelCombinedRowCell"})[0].text), (r.find_all("div",{"class":"InfoPanelCombinedRowCell"})[2].text)
    
    driver.find_element_by_xpath("//*[@id=\"combinedPanel\"]/div/div[3]/a").click()
    time.sleep(0.1)
    
    more_soup = BeautifulSoup(driver.page_source, "html.parser")
    table = more_soup.find("table", {"id":"tblControl"}).find("tbody").find_all("tr")
    for row in table:
        tds = row.find_all("td")
        if (len(tds)>4 and tds[1].contents[0].contents[0]["data-gamename"]=="Core"):
            return (tds[2].text, tds[4].text)
    return "0 hrs", "0" 
        
def scrape_list(names_list):
    
    chromedriver = r"./chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    views, hours = [], []
    for n in names_list:
        v, h = scrape_name(n, driver)
        views.append(v)
        hours.append(h)
    driver.close()
    return views, hours
    
#print(scrape_list(["https://sullygnome.com/channel/owndoggames", "https://sullygnome.com/channel/mtgnerdgirl", "https://sullygnome.com/channel/lana_lux", "https://sullygnome.com/channel/thatjaxboxchick"]))