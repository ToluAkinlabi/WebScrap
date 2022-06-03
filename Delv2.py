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

standardSurgery = tableTitle.find_next()
strippedStandardSurgery = standardSurgery.text
print(strippedStandardSurgery)

standardSurgeryWithOOC = standardSurgery.find_next()
strippedStandardSurgeryWithOOC = standardSurgeryWithOOC.text
print(strippedStandardSurgeryWithOOC)

total = standardSurgeryWithOOC.find_next()
strippedTotal = total.text
print(strippedTotal)

#Table Title Content
tableTitleContent = parseClinicPage.find("span", class_="COLLAPSE de-showAndHide").find("span")
strippedTitleContent = tableTitleContent.text.strip()
print(strippedTitleContent)

standardSurgeryContent = tableTitleContent.find_next()
strippedStandardSurgeryContent = standardSurgeryContent.text
print(strippedStandardSurgeryContent)

standardSurgeryWithOOContent = standardSurgeryContent.find_next()
strippedStandardSurgeryWithOOContent = standardSurgeryWithOOContent.text
print(strippedStandardSurgeryWithOOContent)

totalContent = standardSurgeryWithOOContent.find_next()
strippedTotalContent = totalContent.text
print(strippedTotalContent)


#Analysis Description
analysisDesc = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("span")
strippedAnalysisDesc = analysisDesc.text.strip()
print(strippedAnalysisDesc)

#Analysis Description value
analysisDescValue = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("div")
strippedAnalysisDescValue = analysisDescValue.text.strip()
print(strippedAnalysisDescValue)

#Table Title
tableTitle = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2")
strippedtableTitle = tableTitle.text
print(strippedtableTitle)