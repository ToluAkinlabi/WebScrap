import pandas as pd
import requests
from bs4 import BeautifulSoup

# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT04993339?rslt=With&cntry=US&draw=20000&rank=7")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

#Baseline Table Scrap
#Table header

baselineHeading = parseClinicPage.find_all('span', class_="ct-header2")[1]
strippedBaselineHeading = baselineHeading.text.strip()
print(strippedBaselineHeading)

#Table Title
tableTitle = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2")
strippedtableTitle = tableTitle.text
print(strippedtableTitle)

standardSurgery = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2").find_next()
strippedStandardSurgery = standardSurgery.text
print(strippedStandardSurgery)

standardSurgeryWithOOC = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2").find_next().find_next()
strippedStandardSurgeryWithOOC = standardSurgeryWithOOC.text
print(strippedStandardSurgeryWithOOC)

total = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2").find_next().find_next().find_next()
strippedTotal = total.text
print(strippedTotal)

#Table Title Content
tableRowDesc = parseClinicPage.find("span", class_="COLLAPSE de-showAndHide")
strippedTableRowDesc = tableRowDesc.text.strip()
print(strippedTableRowDesc)