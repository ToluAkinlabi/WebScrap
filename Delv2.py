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

emptyAgeCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4")
strippedAgeCol = emptyAgeCol.text
print(strippedAgeCol)

ageRowOneValueOne = emptyAgeCol.find_next()
strippedAgeRowOneValueOne = ageRowOneValueOne.text
print(strippedAgeRowOneValueOne)

ageRowOneValueTwo = ageRowOneValueOne.find_next()
strippedAgeRowOneValueTwo = ageRowOneValueTwo.text
print(strippedAgeRowOneValueTwo)

ageRowOneValueThree = ageRowOneValueTwo.find_next()
strippedAgeRowOneValueThree = ageRowOneValueThree.text
print(strippedAgeRowOneValueThree)

ageRowOneValueFour = ageRowOneValueThree.find_next()
strippedAgeRowOneValueFour = ageRowOneValueFour.text
print(strippedAgeRowOneValueFour)

#Age Valued Row one
ageRowTwoValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="<=18 years")
strippedAgeRowTwoValueOne = ageRowTwoValueOne.text
print(strippedAgeRowTwoValueOne)

ageRowTwoValueTwo = ageRowTwoValueOne.find_next("div")
strippedAgeRowTwoValueTwo = ageRowTwoValueTwo.text
print(strippedAgeRowTwoValueTwo)

ageRowTwoValueThree = ageRowTwoValueOne.find_next("div").find_next("span")
strippedAgeRowTwoValueThree = ageRowTwoValueThree.text
print(strippedAgeRowTwoValueThree)

ageRowTwoValueFour = ageRowTwoValueThree.find_next("div")
strippedAgeRowTwoValueFour = ageRowTwoValueFour.text
print(strippedAgeRowTwoValueFour)

ageRowTwoValueFive = ageRowTwoValueThree.find_next("div").find_next("span")
strippedAgeRowTwoValueFive = ageRowTwoValueFive.text
print(strippedAgeRowTwoValueFive)

ageRowTwoValueSix = ageRowTwoValueFive.find_next("div")
strippedAgeRowTwoValueSix = ageRowTwoValueSix.text
print(strippedAgeRowTwoValueSix)

ageRowTwoValueSeven = ageRowTwoValueFive.find_next("div").find_next("span")
strippedAgeRowTwoValueSeven = ageRowTwoValueSeven.text
print(strippedAgeRowTwoValueSeven)

#Age Valued Row Two
ageRowThreeValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="Between 18 and 65 years")
strippedAgeRowThreeValueOne = ageRowThreeValueOne.text
print(strippedAgeRowThreeValueOne)

ageRowThreeValueTwo = ageRowThreeValueOne.find_next("div")
strippedAgeRowThreeValueTwo = ageRowThreeValueTwo.text
print(strippedAgeRowThreeValueTwo)

ageRowThreeValueThree = ageRowThreeValueOne.find_next("div").find_next("span")
strippedAgeRowThreeValueThree = ageRowThreeValueThree.text
print(strippedAgeRowThreeValueThree)

ageRowThreeValueFour = ageRowThreeValueThree.find_next("div")
strippedAgeRowThreeValueFour = ageRowThreeValueFour.text
print(strippedAgeRowThreeValueFour)

ageRowThreeValueFive = ageRowThreeValueThree.find_next("div").find_next("span")
strippedAgeRowThreeValueFive = ageRowThreeValueFive.text
print(strippedAgeRowThreeValueFive)

ageRowThreeValueSix = ageRowThreeValueFive.find_next("div")
strippedAgeRowThreeValueSix = ageRowThreeValueSix.text
print(strippedAgeRowThreeValueSix)

ageRowThreeValueSeven = ageRowThreeValueFive.find_next("div").find_next("span")
strippedAgeRowThreeValueSeven = ageRowThreeValueSeven.text
print(strippedAgeRowThreeValueSeven)

#Age Valued Row Three
ageRowFourValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string=">=65 years")
strippedAgeRowFourValueOne = ageRowFourValueOne.text
print(strippedAgeRowFourValueOne)

ageRowFourValueTwo = ageRowFourValueOne.find_next("div")
strippedAgeRowFourValueTwo = ageRowFourValueTwo.text
print(strippedAgeRowFourValueTwo)

ageRowFourValueThree = ageRowFourValueOne.find_next("div").find_next("span")
strippedAgeRowFourValueThree = ageRowFourValueThree.text
print(strippedAgeRowFourValueThree)

ageRowFourValueFour = ageRowFourValueThree.find_next("div")
strippedAgeRowFourValueFour = ageRowFourValueFour.text
print(strippedAgeRowFourValueFour)

ageRowFourValueFive = ageRowFourValueThree.find_next("div").find_next("span")
strippedAgeRowFourValueFive = ageRowFourValueFive.text
print(strippedAgeRowFourValueFive)

ageRowFourValueSix = ageRowFourValueFive.find_next("div")
strippedAgeRowFourValueSix = ageRowFourValueSix.text
print(strippedAgeRowFourValueSix)

ageRowFourValueSeven = ageRowFourValueFive.find_next("div").find_next("span")
strippedAgeRowFourValueSeven = ageRowFourValueSeven.text
print(strippedAgeRowFourValueSeven)


#Sex Category
sexCategory = ageRowFourValueSeven.find_next()
strippedSexCategory = sexCategory.text
print(strippedSexCategory)

sexCategoryOne = sexCategory.find("div", class_="labelSubtle")
strippedSexParameterOne = sexCategoryOne.text
print(strippedSexParameterOne)

sexCategoryTwo = sexCategoryOne.find_next()
strippedSexParameterTwo = sexCategoryTwo.text
print(strippedSexParameterTwo)

