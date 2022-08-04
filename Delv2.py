import sys
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

df = pd.DataFrame()
firstRowContent = []
secondRowContent = []


# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05143801?rslt=With&cntry=US&draw=2&rank=2")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

#get length of row so we can use the value to iterate it
rowLength = parseClinicPage.find("div",id="tab-body").find("div", class_="tr-indent2").find_all("div",class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find("tr").find_next_siblings()
getRowLength = str(len(rowLength) + 1)
print(getRowLength)

# parse row one after the other to get contents
eachRow = parseClinicPage.find("div", id="tab-body").find("div", class_="tr-indent2").find_all("div", class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find("tr")
for child in eachRow.stripped_strings:
    firstRowContent.append(child)
print(firstRowContent)

secondRow = eachRow.find_next_sibling(id="EXPAND-armGroupDescriptionRow-baseline")
for child in secondRow.stripped_strings:
    secondRowContent.append(child)
print(secondRowContent)









