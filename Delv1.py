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

unitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2].find_all("div", class_="labelSubtle")[1]
strippedUnitParameter = unitParameters.text
print(strippedUnitParameter)

emptyColOne = parseClinicPage.find("th", class_="de-baselineLabelCell", style="border-top-color:black")
strippedEmptyColOne = emptyColOne.text
print(strippedEmptyColOne)

emptyColTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4")
strippedEmptyColTwo = emptyColTwo.text
print(strippedEmptyColTwo)

emptyRowOneDeets = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4").find_next()
strippedEmptyRowOneDeets = emptyRowOneDeets.text
print(strippedEmptyRowOneDeets)

emptyRowOneSecondDeets = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4").find_next().find_next()
strippedEmptyRowOneSecondDeets = emptyRowOneSecondDeets.text
print(strippedEmptyRowOneSecondDeets)

emptyRowTwoDeets = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[4]
strippedEmptyRowTwoDeets = emptyRowTwoDeets.text
print(strippedEmptyRowTwoDeets)

emptyRowTwoSecondDeets = parseClinicPage.find_all("div", string="2")[0]
strippedEmptyRowTwoSecondDeets = emptyRowTwoSecondDeets.text
print(strippedEmptyRowTwoSecondDeets)

emptyRowTwoThirdDeets = parseClinicPage.find_all("div", string="2")[0].find_next()
strippedEmptyRowTwoThirdDeets = emptyRowTwoThirdDeets.text
print(strippedEmptyRowTwoThirdDeets)

emptyRowThreeDeets = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[5]
strippedEmptyRowThreeDeets = emptyRowThreeDeets.text
print(strippedEmptyRowThreeDeets)

emptyRowThreeSecondDeets = parseClinicPage.find_all("div", string="0")[0]
strippedEmptyRowThreeSecondDeets = emptyRowThreeSecondDeets.text
print(strippedEmptyRowThreeSecondDeets)

emptyRowThreeThirdDeets = parseClinicPage.find_all("div", string="0")[0].find_next()
strippedEmptyRowThreeThirdDeets = emptyRowThreeThirdDeets.text
print(strippedEmptyRowThreeThirdDeets)

emptyRowFourDeets = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[6]
strippedEmptyRowFourDeets = emptyRowFourDeets.text
print(strippedEmptyRowFourDeets)

emptyRowFourSecondDeets = parseClinicPage.find_all("div", string="0")[0]
strippedEmptyRowFourSecondDeets = emptyRowFourSecondDeets.text
print(strippedEmptyRowFourSecondDeets)

emptyRowFourThirdDeets = parseClinicPage.find_all("div", string="0")[0].find_next()
strippedEmptyRowFourThirdDeets = emptyRowFourThirdDeets.text
print(strippedEmptyRowFourThirdDeets)


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