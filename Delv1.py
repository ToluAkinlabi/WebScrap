import requests
from bs4 import BeautifulSoup

# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05167370?rslt=With&cntry=US&draw=2&rank=1&view=results")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

#Baseline Table Scrap
#Table header

baselineHeading = parseClinicPage.find_all('span', class_="ct-header2")[1]
strippedBaselineHeading = baselineHeading.text.strip()
print(strippedBaselineHeading)

#Table data content

#Title
tableRowTitle = parseClinicPage.find_all("td", class_="de-baselineLabelCell")[0]
strippedTableRowTitle = tableRowTitle.text.strip()
print(strippedTableRowTitle)

#Title Content
tableRowTitleContent = parseClinicPage.find("th", class_="de-baselineLabelCell")
strippedTableRowTitleContent = tableRowTitleContent.text.strip()
print(strippedTableRowTitleContent)

#Description
tableRowDesc = parseClinicPage.find("span", class_="COLLAPSE de-showAndHide")
strippedTableRowDesc = tableRowDesc.text.strip()
print(strippedTableRowDesc)

#Description Content
tableRowDescContent = parseClinicPage.find("tr", class_="EXPAND").find_all("td", class_="de-popFlowLabelCell")[1]
strippedTableRowDescContent = tableRowDescContent.text.strip()
print(strippedTableRowDescContent)

#baseline participant
overallBaseline = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[1]
strippedOverallBaseline = overallBaseline.text.strip()
print(strippedOverallBaseline)

#baseline participant value
overallPartValue = parseClinicPage.find("td", class_="de-numValue_baselineDataCell")
strippedOverallPartValue = overallPartValue.text.strip()
print(strippedOverallPartValue)

#Analysis Description
analysisDesc = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("span")
strippedAnalysisDesc = analysisDesc.text.strip()
print(strippedAnalysisDesc)

#Analysis Description value
analysisDescValue = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("div")
strippedAnalysisDescValue = analysisDescValue.text.strip()
print(strippedAnalysisDescValue)

#Age category
ageCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2]
strippedAgeCategory = ageCategory.text
print(strippedAgeCategory)

ageParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2].find_all("div", class_="labelSubtle")[0]
strippedAgeParameter = ageParameters.text
print(strippedAgeParameter)

ageUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2].find_all("div", class_="labelSubtle")[1]
strippedAgeUnitParameter = ageUnitParameters.text
print(strippedAgeUnitParameter)

emptyAgeOne = parseClinicPage.find("th", class_="de-baselineLabelCell", style="border-top-color:black")
strippedEmptyAgeOne = emptyAgeOne.text
print(strippedEmptyAgeOne)

emptyAgeTwo = parseClinicPage.find("th", class_="de-baselineLabelCell", style="border-top-color:black").find_next()
strippedEmptyAgeTwo = emptyAgeTwo.text
print(strippedEmptyAgeTwo)

emptyAgeCol = parseClinicPage.find_all("td", class_="de-baselineLabelCell", rowspan="4")[0]
strippedEmptyAgeCol = emptyAgeCol.text
print(strippedEmptyAgeCol)

ageRowOneWithValueOne = parseClinicPage.find_all("td", class_="de-baselineLabelCell", rowspan="4")[0].find_next()
strippedAgeRowOneWithValueOne = ageRowOneWithValueOne.text
print(strippedAgeRowOneWithValueOne)

ageRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4").find_next().find_next()
strippedAgeRowOneWithValueTwo = ageRowOneWithValueTwo.text
print(strippedAgeRowOneWithValueTwo)

ageRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[4]
strippedAgeRowTwoWithValueOne = ageRowTwoWithValueOne.text
print(strippedAgeRowTwoWithValueOne)

ageRowTwoWithValueTwo = parseClinicPage.find_all("div", string="2")[0]
strippedAgeRowTwoWithValueTwo = ageRowTwoWithValueTwo.text
print(strippedAgeRowTwoWithValueTwo)

ageRowTwoWithValueThree = parseClinicPage.find_all("div", string="2")[0].find_next()
strippedAgeRowTwoWithValueThree = ageRowTwoWithValueThree.text
print(strippedAgeRowTwoWithValueThree)

ageRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[5]
strippedAgeRowThreeWithValueOne = ageRowThreeWithValueOne.text
print(strippedAgeRowThreeWithValueOne)

ageRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[0]
strippedAgeRowThreeWithValueTwo = ageRowThreeWithValueTwo.text
print(strippedAgeRowThreeWithValueTwo)

ageRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[0].find_next()
strippedAgeRowThreeWithValueThree = ageRowThreeWithValueThree.text
print(strippedAgeRowThreeWithValueThree)

ageRowFourWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[6]
strippedAgeRowFourWithValueOne = ageRowFourWithValueOne.text
print(strippedAgeRowFourWithValueOne)

ageRowFourWithValueTwo = parseClinicPage.find_all("div", string="0")[1]
strippedAgeRowFourWithValueTwo = ageRowFourWithValueTwo.text
print(strippedAgeRowFourWithValueTwo)

ageRowFourWithValueThree = parseClinicPage.find_all("div", string="0")[1].find_next()
strippedAgeRowFourWithValueThree = ageRowFourWithValueThree.text
print(strippedAgeRowFourWithValueThree)


#Sex Category
sexCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4]
strippedSexCategory = sexCategory.text
print(strippedSexCategory)

sexParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4].find_all("div", class_="labelSubtle")[0]
strippedsexParameters = sexParameters.text
print(strippedsexParameters)

sexUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4].find_all("div", class_="labelSubtle")[1]
strippedsexUnitParameter = sexUnitParameters.text
print(strippedsexUnitParameter)

emptySexOne = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1]
strippedEmptySexOne = emptySexOne.text
print(strippedEmptySexOne)

emptySexTwo = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1].find_next()
strippedEmptySexTwo = emptySexTwo.text
print(strippedEmptySexTwo)

emptySexCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3")
strippedEmptySexCol = emptySexCol.text
print(strippedEmptySexCol)

sexRowOneWithValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3").find_next()
strippedSexRowOneWithValueOne = sexRowOneWithValueOne.text
print(strippedSexRowOneWithValueOne)

sexRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3").find_next().find_next()
strippedSexRowOneWithValueTwo = sexRowOneWithValueTwo.text
print(strippedSexRowOneWithValueTwo)

sexRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[9]
strippedSexRowTwoWithValueOne = sexRowTwoWithValueOne.text
print(strippedSexRowTwoWithValueOne)

sexRowTwoWithValueTwo = parseClinicPage.find_all("div", string="2")[1]
strippedSexRowTwoWithValueTwo = sexRowTwoWithValueTwo.text
print(strippedSexRowTwoWithValueTwo)

sexRowTwoWithValueThree = parseClinicPage.find_all("div", string="2")[1].find_next()
strippedSexRowTwoWithValueThree = sexRowTwoWithValueThree.text
print(strippedSexRowTwoWithValueThree)

sexRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[10]
strippedSexRowThreeWithValueOne = sexRowThreeWithValueOne.text
print(strippedSexRowThreeWithValueOne)

sexRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[2]
strippedSexRowThreeWithValueTwo = sexRowThreeWithValueTwo.text
print(strippedSexRowThreeWithValueTwo)

sexRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[2].find_next()
strippedSexRowThreeWithValueThree = sexRowThreeWithValueThree.text
print(strippedSexRowThreeWithValueThree)

#Race Category
raceCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6]
strippedRaceCategory = raceCategory.text
print(strippedRaceCategory)

raceParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6].find_all("div", class_="labelSubtle")[0]
strippedRaceParameters = raceParameters.text
print(strippedRaceParameters)

raceUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6].find_all("div", class_="labelSubtle")[1]
strippedRaceUnitParameter = raceUnitParameters.text
print(strippedRaceUnitParameter)

emptyRaceOne = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1]
strippedEmptyRaceOne = emptyRaceOne.text
print(strippedEmptyRaceOne)

emptyRaceTwo = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1].find_next()
strippedEmptyRaceTwo = emptyRaceTwo.text
print(strippedEmptyRaceTwo)

emptyRaceCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8")
strippedEmptyRaceCol = emptyRaceCol.text
print(strippedEmptyRaceCol)

raceRowOneWithValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8").find_next()
strippedRaceRowOneWithValueOne = raceRowOneWithValueOne.text
print(strippedRaceRowOneWithValueOne)

raceRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8").find_next().find_next()
strippedRaceRowOneWithValueTwo = raceRowOneWithValueTwo.text
print(strippedRaceRowOneWithValueTwo)

sexRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[10]
strippedSexRowThreeWithValueOne = sexRowThreeWithValueOne.text
print(strippedSexRowThreeWithValueOne)

sexRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[2]
strippedSexRowThreeWithValueTwo = sexRowThreeWithValueTwo.text
print(strippedSexRowThreeWithValueTwo)

sexRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[2].find_next()
strippedSexRowThreeWithValueThree = sexRowThreeWithValueThree.text
print(strippedSexRowThreeWithValueThree)