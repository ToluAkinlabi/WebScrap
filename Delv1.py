import pandas as pd
import requests
from bs4 import BeautifulSoup

# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05167370?rslt=With&cntry=US&draw=2&rank=1&view=results")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

#Baseline Table Scrap
#Table header

baselineHeading = parseClinicPage.find_all('span', class_="ct-header2")[1]
strippedBaselineHeading = baselineHeading.text.strip()

#Table data content

#Title
tableRowTitle = parseClinicPage.find_all("td", class_="de-baselineLabelCell")[0]
strippedTableRowTitle = tableRowTitle.text.strip()

#Title Content
tableRowTitleContent = parseClinicPage.find("th", class_="de-baselineLabelCell")
strippedTableRowTitleContent = tableRowTitleContent.text.strip()

#Description
tableRowDesc = parseClinicPage.find("span", class_="COLLAPSE de-showAndHide")
strippedTableRowDesc = tableRowDesc.text.strip()

#Description Content
tableRowDescContent = parseClinicPage.find("tr", class_="EXPAND").find_all("td", class_="de-popFlowLabelCell")[1]
strippedTableRowDescContent = tableRowDescContent.text.strip()

#baseline participant
overallBaseline = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[1]
strippedOverallBaseline = overallBaseline.text.strip()

#baseline participant value
overallPartValue = parseClinicPage.find("td", class_="de-numValue_baselineDataCell")
strippedOverallPartValue = overallPartValue.text.strip()

#Analysis Description
analysisDesc = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("span")
strippedAnalysisDesc = analysisDesc.text.strip()

#Analysis Description value
analysisDescValue = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("div")
strippedAnalysisDescValue = analysisDescValue.text.strip()

#Age category
ageCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2]
strippedAgeCategory = ageCategory.text

ageParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2].find_all("div", class_="labelSubtle")[0]
strippedAgeParameter = ageParameters.text

ageUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[2].find_all("div", class_="labelSubtle")[1]
strippedAgeUnitParameter = ageUnitParameters.text

emptyAgeOne = parseClinicPage.find("th", class_="de-baselineLabelCell", style="border-top-color:black")
strippedEmptyAgeOne = emptyAgeOne.text

emptyAgeTwo = parseClinicPage.find("th", class_="de-baselineLabelCell", style="border-top-color:black").find_next()
strippedEmptyAgeTwo = emptyAgeTwo.text

emptyAgeCol = parseClinicPage.find_all("td", class_="de-baselineLabelCell", rowspan="4")[0]
strippedEmptyAgeCol = emptyAgeCol.text

ageRowOneWithValueOne = parseClinicPage.find_all("td", class_="de-baselineLabelCell", rowspan="4")[0].find_next()
strippedAgeRowOneWithValueOne = ageRowOneWithValueOne.text

ageRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4").find_next().find_next()
strippedAgeRowOneWithValueTwo = ageRowOneWithValueTwo.text

ageRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[4]
strippedAgeRowTwoWithValueOne = ageRowTwoWithValueOne.text

ageRowTwoWithValueTwo = parseClinicPage.find_all("div", string="2")[0]
strippedAgeRowTwoWithValueTwo = ageRowTwoWithValueTwo.text

ageRowTwoWithValueThree = parseClinicPage.find_all("div", string="2")[0].find_next()
strippedAgeRowTwoWithValueThree = ageRowTwoWithValueThree.text

ageRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[5]
strippedAgeRowThreeWithValueOne = ageRowThreeWithValueOne.text

ageRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[0]
strippedAgeRowThreeWithValueTwo = ageRowThreeWithValueTwo.text

ageRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[0].find_next()
strippedAgeRowThreeWithValueThree = ageRowThreeWithValueThree.text

ageRowFourWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[6]
strippedAgeRowFourWithValueOne = ageRowFourWithValueOne.text

ageRowFourWithValueTwo = parseClinicPage.find_all("div", string="0")[1]
strippedAgeRowFourWithValueTwo = ageRowFourWithValueTwo.text

ageRowFourWithValueThree = parseClinicPage.find_all("div", string="0")[1].find_next()
strippedAgeRowFourWithValueThree = ageRowFourWithValueThree.text

#Sex Category
sexCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4]
strippedSexCategory = sexCategory.text

sexParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4].find_all("div", class_="labelSubtle")[0]
strippedsexParameters = sexParameters.text

sexUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[4].find_all("div", class_="labelSubtle")[1]
strippedsexUnitParameter = sexUnitParameters.text

emptySexOne = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1]
strippedEmptySexOne = emptySexOne.text

emptySexTwo = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[1].find_next()
strippedEmptySexTwo = emptySexTwo.text

emptySexCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3")
strippedEmptySexCol = emptySexCol.text

sexRowOneWithValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3").find_next()
strippedSexRowOneWithValueOne = sexRowOneWithValueOne.text

sexRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3").find_next().find_next()
strippedSexRowOneWithValueTwo = sexRowOneWithValueTwo.text

sexRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[9]
strippedSexRowTwoWithValueOne = sexRowTwoWithValueOne.text

sexRowTwoWithValueTwo = parseClinicPage.find_all("div", string="2")[1]
strippedSexRowTwoWithValueTwo = sexRowTwoWithValueTwo.text

sexRowTwoWithValueThree = parseClinicPage.find_all("div", string="2")[1].find_next()
strippedSexRowTwoWithValueThree = sexRowTwoWithValueThree.text

sexRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[10]
strippedSexRowThreeWithValueOne = sexRowThreeWithValueOne.text

sexRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[2]
strippedSexRowThreeWithValueTwo = sexRowThreeWithValueTwo.text

sexRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[2].find_next()
strippedSexRowThreeWithValueThree = sexRowThreeWithValueThree.text

#Race Category
raceCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6]
strippedRaceCategory = raceCategory.text

raceParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6].find_all("div", class_="labelSubtle")[0]
strippedRaceParameters = raceParameters.text

raceUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[6].find_all("div", class_="labelSubtle")[1]
strippedRaceUnitParameter = raceUnitParameters.text

emptyRaceOne = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[2]
strippedEmptyRaceOne = emptyRaceOne.text

emptyRaceTwo = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[2].find_next()
strippedEmptyRaceTwo = emptyRaceTwo.text

emptyRaceCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8")
strippedEmptyRaceCol = emptyRaceCol.text

raceRowOneWithValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8").find_next()
strippedRaceRowOneWithValueOne = raceRowOneWithValueOne.text

raceRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="8").find_next().find_next()
strippedRaceRowOneWithValueTwo = raceRowOneWithValueTwo.text

raceRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[13]
strippedRaceRowTwoWithValueOne = raceRowTwoWithValueOne.text

raceRowTwoWithValueTwo = parseClinicPage.find_all("div", string="0")[3]
strippedRaceRowTwoWithValueTwo = raceRowTwoWithValueTwo.text

raceRowTwoWithValueThree = parseClinicPage.find_all("div", string="0")[3].find_next()
strippedRaceRowTwoWithValueThree = raceRowTwoWithValueThree.text

raceRowThreeWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[14]
strippedRaceRowThreeWithValueOne = raceRowThreeWithValueOne.text

raceRowThreeWithValueTwo = parseClinicPage.find_all("div", string="0")[4]
strippedRaceRowThreeWithValueTwo = raceRowThreeWithValueTwo.text

raceRowThreeWithValueThree = parseClinicPage.find_all("div", string="0")[4].find_next()
strippedRaceRowThreeWithValueThree = raceRowThreeWithValueThree.text

raceRowFourWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[15]
strippedRaceRowFourWithValueOne = raceRowFourWithValueOne.text

raceRowFourWithValueTwo = parseClinicPage.find_all("div", string="0")[5]
strippedRaceRowFourWithValueTwo = raceRowFourWithValueTwo.text

raceRowFourWithValueThree = parseClinicPage.find_all("div", string="0")[5].find_next()
strippedRaceRowFourWithValueThree = raceRowFourWithValueThree.text

raceRowFiveWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[16]
strippedRaceRowFiveWithValueOne = raceRowFiveWithValueOne.text

raceRowFiveWithValueTwo = parseClinicPage.find_all("div", string="0")[6]
strippedRaceRowFiveWithValueTwo = raceRowFiveWithValueTwo.text

raceRowFiveWithValueThree = parseClinicPage.find_all("div", string="0")[6].find_next()
strippedRaceRowFiveWithValueThree = raceRowFiveWithValueThree.text

raceRowSixWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[17]
strippedRaceRowSixWithValueOne = raceRowSixWithValueOne.text

raceRowSixWithValueTwo = parseClinicPage.find_all("div", string="2")[2]
strippedRaceRowSixWithValueTwo = raceRowSixWithValueTwo.text

raceRowSixWithValueThree = parseClinicPage.find_all("div", string="2")[2].find_next()
strippedRaceRowSixWithValueThree = raceRowSixWithValueThree.text

raceRowSevenWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[18]
strippedRaceRowSevenWithValueOne = raceRowSevenWithValueOne.text

raceRowSevenWithValueTwo = parseClinicPage.find_all("div", string="0")[7]
strippedRaceRowSevenWithValueTwo = raceRowSevenWithValueTwo.text

raceRowSevenWithValueThree = parseClinicPage.find_all("div", string="0")[7].find_next()
strippedRaceRowSevenWithValueThree = raceRowSevenWithValueThree.text

raceRowEightWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[19]
strippedRaceRowEightWithValueOne = raceRowEightWithValueOne.text

raceRowEightWithValueTwo = parseClinicPage.find_all("div", string="0")[8]
strippedRaceRowEightWithValueTwo = raceRowEightWithValueTwo.text

raceRowEightWithValueThree = parseClinicPage.find_all("div", string="0")[8].find_next()
strippedRaceRowEightWithValueThree = raceRowEightWithValueThree.text

#Region Category
regionCategory = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[8]
strippedRegionCategory = regionCategory.text

regionParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[8].find_all("div", class_="labelSubtle")[0]
strippedRegionParameters = regionParameters.text

regionUnitParameters = parseClinicPage.find_all("th", class_="de-baselineLabelCell")[8].find_all("div", class_="labelSubtle")[1]
strippedRegionUnitParameter = regionUnitParameters.text

emptyRegionOne = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[3]
strippedEmptyRegionOne = emptyRegionOne.text

emptyRegionTwo = parseClinicPage.find_all("th", class_="de-baselineLabelCell", style="border-top-color:black")[3].find_next()
strippedEmptyRegionTwo = emptyRegionTwo.text

regionCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="2")
strippedRegionCol = regionCol.text

regionRowOneWithValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="2").find_next()
strippedRegionRowOneWithValueOne = regionRowOneWithValueOne.text

regionRowOneWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="2").find_next().find_next()
strippedRegionRowOneWithValueTwo = regionRowOneWithValueTwo.text

regionRowTwoWithValueOne = parseClinicPage.find("td", class_="de-numValue_baselineDataCell").find_all_next("td", class_="de-baselineLabelCell")[22]
strippedRegionRowTwoWithValueOne = regionRowTwoWithValueOne.text

regionRowTwoWithValueTwo = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="2").find_next(string="2")
strippedRegionRowTwoWithValueTwo = regionRowTwoWithValueTwo.text


#Converting scrapped data to a csv file
#storing result as a dictionary of lists
tableResult = {
    " " : [strippedBaselineHeading,"","","","","","","","","","","",""],

    "Table Title" : ["",strippedTableRowTitle,strippedTableRowDesc,
                     strippedOverallBaseline,strippedAnalysisDesc,"","","","","","","",""],

    "Table Desc" : ["",strippedTableRowTitleContent,strippedTableRowDescContent,
                   strippedOverallPartValue,strippedAnalysisDescValue,"","","","","","","",""],

    "Age, Categorical" : ["","","","","",strippedAgeRowOneWithValueOne, strippedAgeRowTwoWithValueOne,
                          strippedAgeRowThreeWithValueOne,strippedAgeRowFourWithValueOne,"","","",""],

    "Measure Type:Count of Participants" : ["","","","","",strippedAgeRowOneWithValueTwo,strippedAgeRowTwoWithValueTwo,
                                            strippedAgeRowThreeWithValueTwo, strippedAgeRowFourWithValueTwo,"","","",""],

    "Unit of measure:  Participants": ["","","","","","",strippedAgeRowTwoWithValueThree,
                                       strippedAgeRowThreeWithValueThree, strippedAgeRowFourWithValueThree,"","","",""],

    "Sex, Categorical" : ["","","","","",strippedSexRowOneWithValueOne,strippedSexRowTwoWithValueOne ,strippedSexRowThreeWithValueOne,"","","","",""],

    "(S)Measure Type:Count of Participants": ["","","","","",strippedSexRowOneWithValueTwo,strippedSexRowTwoWithValueTwo,strippedSexRowThreeWithValueTwo,"","","","",""],

    "(S)Unit of measure:  Participants": ["","","","","","",strippedSexRowTwoWithValueTwo,strippedSexRowThreeWithValueTwo,"","","","",""],

    "Race, Categorical" : ["","","","","",strippedRaceRowOneWithValueOne,strippedRaceRowTwoWithValueOne,strippedRaceRowThreeWithValueOne,
                           strippedRaceRowFourWithValueOne,strippedRaceRowFiveWithValueOne,strippedRaceRowSixWithValueOne,strippedRaceRowSevenWithValueOne,
                           strippedRaceRowSevenWithValueOne ],
    "(Ra)Measure Type:Count of Participants" : ["","","","","",strippedRaceRowOneWithValueTwo,strippedRaceRowTwoWithValueTwo,strippedRaceRowThreeWithValueTwo,
                           strippedRaceRowFourWithValueTwo,strippedRaceRowFiveWithValueTwo,strippedRaceRowSixWithValueTwo,strippedRaceRowSevenWithValueTwo,
                           strippedRaceRowSevenWithValueTwo ],
    "(Ra)Unit of measure:  Participants" : ["","","","","","",strippedRaceRowTwoWithValueThree,strippedRaceRowThreeWithValueThree,
                           strippedRaceRowFourWithValueThree,strippedRaceRowFiveWithValueThree,strippedRaceRowSixWithValueThree,strippedRaceRowSevenWithValueThree,
                           strippedRaceRowSevenWithValueThree],

    "Region, Categorical" : ["","","","","",strippedRegionRowOneWithValueOne,
                             strippedRegionRowTwoWithValueOne,"","","","","",strippedRegionCol],

    "(Re)Measure Type:Count of Participants" : ["","","","","",strippedRegionRowOneWithValueTwo,
                             strippedRegionRowTwoWithValueTwo,"","","","","","" ],

    "(Re)Unit of measure:  Participants" : ["","","","","","","","","","","","","" ],
}

dataFrame = pd.DataFrame(tableResult)
#print("Converting data to csv file...")
print(dataFrame)
#dataFrame.to_csv("C:\\Users\\tolul\\OneDrive\\Documents\\GitHub\\scrap.csv")
#print("Done!")