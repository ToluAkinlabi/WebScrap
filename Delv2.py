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

#Overall Participant
overallParticipants = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="2")
strippedOverallParticipants = overallParticipants.text
print(strippedOverallParticipants)

#Overall Participant Values
overallValueOne = overallParticipants.find_next()
strippedOverallValueOne = overallValueOne.text
print(strippedOverallValueOne)

overallValueTwo = overallValueOne.find_next()
strippedOverallValueTwo = overallValueTwo.text
print(strippedOverallValueTwo)

overallValueThree = overallValueTwo.find_next()
strippedOverallValueThree = overallValueThree.text
print(strippedOverallValueThree)

#Analysis Description
analysisDesc = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("span")
strippedAnalysisDesc = analysisDesc.text.strip()
print(strippedAnalysisDesc)

#Analysis Description value
analysisDescValue = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("div")
strippedAnalysisDescValue = analysisDescValue.text
print(strippedAnalysisDescValue)

#Age Category
ageCategory = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="1")
strippedAgeCategory = ageCategory.text
print(strippedAgeCategory)

ageParameterOne = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="1").find("div", class_="labelSubtle")
strippedAgeParameterOne = ageParameterOne.text
print(strippedAgeParameterOne)

ageParameterTwo = ageParameterOne.find_next()
strippedAgeParameterTwo = ageParameterTwo.text
print(strippedAgeParameterTwo)

emptyAgeRowOne = ageParameterTwo.find_next()
strippedEmptyAgeRowOne = emptyAgeRowOne.text
print(strippedEmptyAgeRowOne)

emptyAgeRowTwo = emptyAgeRowOne.find_next()
strippedEmptyAgeRowTwo = emptyAgeRowOne.text
print(strippedEmptyAgeRowTwo)

emptyAgeRowThree = emptyAgeRowTwo.find_next()
strippedEmptyAgeRowThree = emptyAgeRowThree.text
print(strippedEmptyAgeRowThree)

emptyAgeRowFour = emptyAgeRowThree.find_next()
strippedEmptyAgeRowFour = emptyAgeRowFour.text
print(strippedEmptyAgeRowFour)