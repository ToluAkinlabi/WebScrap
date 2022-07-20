import sys
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

df = pd.DataFrame()

# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05059366?rslt=With&cntry=US&draw=2&rank=7")
studyPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05059366?rslt=With&cntry=US&draw=2&rank=7")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")
parseStudyPage = BeautifulSoup(studyPage.content, "html.parser")

#Baseline Table Scrap
#Table header

baselineHeading = parseClinicPage.find_all('span', class_="ct-header2")[1]
strippedBaselineHeading = baselineHeading.text.strip()

#Table Title
tableTitle = parseClinicPage.find("td", class_="de-baselineLabelCell", colspan="2")
strippedtableTitle = tableTitle.text

standardSurgery = tableTitle.find_next()
strippedStandardSurgery = standardSurgery.text

standardSurgeryWithOOC = standardSurgery.find_next()
strippedStandardSurgeryWithOOC = standardSurgeryWithOOC.text

total = standardSurgeryWithOOC.find_next()
strippedTotal = total.text

#Table Title Content
tableTitleContent = parseClinicPage.find("tr", id="EXPAND-armGroupDescriptionRow-baseline").find("span", class_="COLLAPSE de-showAndHide").find("span")
strippedTitleContent = tableTitleContent.text.strip()

standardSurgeryContent = tableTitleContent.find_next()
strippedStandardSurgeryContent = standardSurgeryContent.text

standardSurgeryWithOOContent = standardSurgeryContent.find_next()
strippedStandardSurgeryWithOOContent = standardSurgeryWithOOContent.text

totalContent = standardSurgeryWithOOContent.find_next()
strippedTotalContent = totalContent.text


#Overall Participant
overallParticipants = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="2")
strippedOverallParticipants = ''.join([i if ord(i) < 128 else '' for i in overallParticipants.text])

#Overall Participant Values
overallValueOne = overallParticipants.find_next()
strippedOverallValueOne = overallValueOne.text

overallValueTwo = overallValueOne.find_next()
strippedOverallValueTwo = overallValueTwo.text

overallValueThree = overallValueTwo.find_next()
strippedOverallValueThree = overallValueThree.text

#Analysis Description
analysisDesc = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("span")
strippedAnalysisDesc = analysisDesc.text.strip()

#Analysis Description value
analysisDescValue = parseClinicPage.find("tr", id="EXPAND-analysisPop-baseline").find("div")
strippedAnalysisDescValue = analysisDescValue.text

#Age Category
ageCategory = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="1")
strippedAgeCategory = ''.join([i if ord(i) < 128 else '' for i in ageCategory.text])

ageParameterOne = parseClinicPage.find("th", class_="de-baselineLabelCell", colspan="1").find("div", class_="labelSubtle")
strippedAgeParameterOne = ageParameterOne.text

ageParameterTwo = ageParameterOne.find_next()
strippedAgeParameterTwo = ageParameterTwo.text

emptyAgeRowOne = ageParameterTwo.find_next()
strippedEmptyAgeRowOne = emptyAgeRowOne.text

emptyAgeRowTwo = emptyAgeRowOne.find_next()
strippedEmptyAgeRowTwo = emptyAgeRowOne.text

emptyAgeRowThree = emptyAgeRowTwo.find_next()
strippedEmptyAgeRowThree = emptyAgeRowThree.text

emptyAgeRowFour = emptyAgeRowThree.find_next()
strippedEmptyAgeRowFour = emptyAgeRowFour.text

emptyAgeCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="4")
strippedAgeCol = emptyAgeCol.text

ageRowOneValueOne = emptyAgeCol.find_next()
strippedAgeRowOneValueOne = ageRowOneValueOne.text

ageRowOneValueTwo = ageRowOneValueOne.find_next()
strippedAgeRowOneValueTwo = ageRowOneValueTwo.text

ageRowOneValueThree = ageRowOneValueTwo.find_next()
strippedAgeRowOneValueThree = ageRowOneValueThree.text

ageRowOneValueFour = ageRowOneValueThree.find_next()
strippedAgeRowOneValueFour = ageRowOneValueFour.text

#Age Valued Row one
ageRowTwoValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="<=18 years")
strippedAgeRowTwoValueOne = ageRowTwoValueOne.text

ageRowTwoValueTwo = ageRowTwoValueOne.find_next("div")
strippedAgeRowTwoValueTwo = ageRowTwoValueTwo.text

ageRowTwoValueThree = ageRowTwoValueOne.find_next("div").find_next("span")
strippedAgeRowTwoValueThree = ''.join([i if ord(i) < 128 else '' for i in ageRowTwoValueThree.text])

ageRowTwoValueFour = ageRowTwoValueThree.find_next("div")
strippedAgeRowTwoValueFour = ageRowTwoValueFour.text

ageRowTwoValueFive = ageRowTwoValueThree.find_next("div").find_next("span")
strippedAgeRowTwoValueFive = ''.join([i if ord(i) < 128 else '' for i in ageRowTwoValueFive.text])

ageRowTwoValueSix = ageRowTwoValueFive.find_next("div")
strippedAgeRowTwoValueSix = ageRowTwoValueSix.text

ageRowTwoValueSeven = ageRowTwoValueFive.find_next("div").find_next("span")
strippedAgeRowTwoValueSeven = ''.join([i if ord(i) < 128 else '' for i in ageRowTwoValueSeven.text])

#Age Valued Row Two
ageRowThreeValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="Between 18 and 65 years")
strippedAgeRowThreeValueOne = ageRowThreeValueOne.text

ageRowThreeValueTwo = ageRowThreeValueOne.find_next("div")
strippedAgeRowThreeValueTwo = ageRowThreeValueTwo.text

ageRowThreeValueThree = ageRowThreeValueOne.find_next("div").find_next("span")
strippedAgeRowThreeValueThree = ''.join([i if ord(i) < 128 else '' for i in ageRowThreeValueThree.text])

ageRowThreeValueFour = ageRowThreeValueThree.find_next("div")
strippedAgeRowThreeValueFour = ageRowThreeValueFour.text

ageRowThreeValueFive = ageRowThreeValueThree.find_next("div").find_next("span")
strippedAgeRowThreeValueFive = ''.join([i if ord(i) < 128 else '' for i in ageRowThreeValueFive.text])

ageRowThreeValueSix = ageRowThreeValueFive.find_next("div")
strippedAgeRowThreeValueSix = ageRowThreeValueSix.text

ageRowThreeValueSeven = ageRowThreeValueFive.find_next("div").find_next("span")
strippedAgeRowThreeValueSeven = ''.join([i if ord(i) < 128 else '' for i in ageRowThreeValueSeven.text])

#Age Valued Row Three
ageRowFourValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string=">=65 years")
strippedAgeRowFourValueOne = ageRowFourValueOne.text

ageRowFourValueTwo = ageRowFourValueOne.find_next("div")
strippedAgeRowFourValueTwo = ageRowFourValueTwo.text

ageRowFourValueThree = ageRowFourValueOne.find_next("div").find_next("span")
strippedAgeRowFourValueThree = ''.join([i if ord(i) < 128 else '' for i in ageRowFourValueThree.text])

ageRowFourValueFour = ageRowFourValueThree.find_next("div")
strippedAgeRowFourValueFour = ageRowFourValueFour.text

ageRowFourValueFive = ageRowFourValueThree.find_next("div").find_next("span")
strippedAgeRowFourValueFive = ''.join([i if ord(i) < 128 else '' for i in ageRowFourValueFive.text])

ageRowFourValueSix = ageRowFourValueFive.find_next("div")
strippedAgeRowFourValueSix = ageRowFourValueSix.text

ageRowFourValueSeven = ageRowFourValueFive.find_next("div").find_next("span")
strippedAgeRowFourValueSeven = ''.join([i if ord(i) < 128 else '' for i in ageRowFourValueSeven.text])


#Sex Category
sexCategory = ageRowFourValueSeven.find_next()
strippedSexCategory = sexCategory.text

sexCategoryOne = sexCategory.find("div", class_="labelSubtle")
strippedSexParameterOne = sexCategoryOne.text

sexCategoryTwo = sexCategoryOne.find_next()
strippedSexParameterTwo = sexCategoryTwo.text

emptySexRowOne = sexCategoryTwo.find_next()
strippedEmptySexRowOne = emptySexRowOne.text

emptySexRowTwo = emptySexRowOne.find_next()
strippedEmptySexRowTwo = emptySexRowTwo.text

emptySexRowThree = emptySexRowTwo.find_next()
strippedEmptySexRowThree = emptySexRowThree.text

emptySexRowFour = emptySexRowThree.find_next()
strippedEmptySexRowFour = emptySexRowFour.text

emptySexCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="3")
strippedSexCol = emptySexCol.text

sexRowOneValueOne = emptySexCol.find_next()
strippedSexRowOneValueOne = sexRowOneValueOne.text

sexRowOneValueTwo = sexRowOneValueOne.find_next()
strippedSexRowOneValueTwo = sexRowOneValueTwo.text

sexRowOneValueThree = sexRowOneValueTwo.find_next()
strippedSexRowOneValueThree = sexRowOneValueThree.text

sexRowOneValueFour = sexRowOneValueThree.find_next()
strippedSexRowOneValueFour = sexRowOneValueFour.text

#Valued Sex Row one
sexRowTwoValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="Female")
strippedSexRowTwoValueOne = sexRowTwoValueOne.text

sexRowTwoValueTwo = sexRowTwoValueOne.find_next("div")
strippedSexRowTwoValueTwo = sexRowTwoValueTwo.text

sexRowTwoValueThree = sexRowTwoValueOne.find_next("div").find_next("span")
strippedSexRowTwoValueThree = ''.join([i if ord(i) < 128 else '' for i in sexRowTwoValueThree.text])

sexRowTwoValueFour = sexRowTwoValueThree.find_next("div")
strippedSexRowTwoValueFour = sexRowTwoValueFour.text

sexRowTwoValueFive = sexRowTwoValueThree.find_next("div").find_next("span")
strippedSexRowTwoValueFive = ''.join([i if ord(i) < 128 else '' for i in sexRowTwoValueFive.text])

sexRowTwoValueSix = sexRowTwoValueFive.find_next("div")
strippedSexRowTwoValueSix = sexRowTwoValueSix.text

sexRowTwoValueSeven = sexRowTwoValueFive.find_next("div").find_next("span")
strippedSexRowTwoValueSeven = ''.join([i if ord(i) < 128 else '' for i in sexRowTwoValueSeven.text])

#Valued Sex Row Two
sexRowThreeValueOne = parseClinicPage.find("td", class_="de-baselineLabelCell", string="Male")
strippedSexRowThreeValueOne = sexRowThreeValueOne.text

sexRowThreeValueTwo = sexRowThreeValueOne.find_next("div")
strippedSexRowThreeValueTwo = sexRowThreeValueTwo.text

sexRowThreeValueThree = sexRowThreeValueOne.find_next("div").find_next("span")
strippedSexRowThreeValueThree = ''.join([i if ord(i) < 128 else '' for i in sexRowThreeValueThree.text])

sexRowThreeValueFour = sexRowThreeValueThree.find_next("div")
strippedSexRowThreeValueFour = sexRowThreeValueFour.text

sexRowThreeValueFive = sexRowThreeValueThree.find_next("div").find_next("span")
strippedSexRowThreeValueFive = ''.join([i if ord(i) < 128 else '' for i in sexRowThreeValueFive.text])

sexRowThreeValueSix = sexRowThreeValueFive.find_next("div")
strippedSexRowThreeValueSix = sexRowThreeValueSix.text

sexRowThreeValueSeven = sexRowThreeValueFive.find_next("div").find_next("span")
strippedSexRowThreeValueSeven = ''.join([i if ord(i) < 128 else '' for i in sexRowThreeValueSeven.text])

#Race Category
raceCategory = sexRowThreeValueSeven.find_next()
strippedRaceCategory = raceCategory.text

raceCategoryOne = raceCategory.find("div", class_="labelSubtle")
strippedRaceParameterOne = raceCategoryOne.text

raceCategoryTwo = raceCategoryOne.find_next()
strippedRaceParameterTwo = raceCategoryTwo.text

emptyRaceRowOne = raceCategoryTwo.find_next()
strippedEmptyRaceRowOne = emptyRaceRowOne.text

emptyRaceRowTwo = emptyRaceRowOne.find_next()
strippedEmptyRaceRowTwo = emptyRaceRowTwo.text

emptyRaceRowThree = emptyRaceRowTwo.find_next()
strippedEmptyRaceRowThree = emptyRaceRowThree.text

emptyRaceRowFour = emptyRaceRowThree.find_next()
strippedEmptyRaceRowFour = emptyRaceRowFour.text

emptyRaceCol = parseClinicPage.find("td", class_="de-baselineLabelCell", rowspan="2")
strippedRaceCol = emptyRaceCol.text

#Valued Race Row one
raceRowOneValueOne = emptyRaceCol.find_next()
strippedRaceRowOneValueOne = raceRowOneValueOne.text

raceRowOneValueTwo = raceRowOneValueOne.find_next()
strippedRaceRowOneValueTwo = raceRowOneValueTwo.text

raceRowOneValueThree = raceRowOneValueTwo.find_next()
strippedRaceRowOneValueThree = raceRowOneValueThree.text

raceRowOneValueFour = raceRowOneValueThree.find_next()
strippedRaceRowOneValueFour = raceRowOneValueFour.text

#Valued Race Row Two
raceRowTwoValueOne = raceRowOneValueFour.find_next("td", class_="de-baselineLabelCell", string="")
strippedRaceRowTwoValueOne = raceRowTwoValueOne.text

raceRowTwoValueTwo = raceRowTwoValueOne.find_next()
strippedRaceRowTwoValueTwo = raceRowTwoValueTwo.text

raceRowTwoValueThree = raceRowTwoValueTwo.find_next()
strippedRaceRowTwoValueThree = raceRowTwoValueThree.text

raceRowTwoValueFour = raceRowTwoValueThree.find_next()
strippedRaceRowTwoValueFour = raceRowTwoValueFour.text

#Valued Race Row Two
raceColThree = raceRowTwoValueFour.find_next(colspan="2")
strippedRaceColThree = raceColThree.text

raceColFour = raceColThree.find_next()
strippedRaceColFour = raceColFour.text

#location
locCountry = parseStudyPage.find("div", id="COLLAPSE-Locations").find("div", class_="tr-table_cover").find("td", class_="ct-header3")
strippedLocationCountry = locCountry.text

locDetails = parseStudyPage.find("div", id="COLLAPSE-Locations").find("div", class_="tr-table_cover").find("td", headers="locName")
strippedLocationDetails = locDetails.text

locCode = parseStudyPage.find("div", id="COLLAPSE-Locations").find("div", class_="tr-table_cover").find_all("td", colspan="2")[1]
strippedLocationCode = locCode.text


#Return result into Json
data = {

    # Column 1

    '(S) Arm/Group Title': [strippedStandardSurgery],
    '(S) Arm/Group Description': [strippedStandardSurgeryContent],
    '(S) Overall Participants': [strippedOverallValueOne],
    '(S) Baseline Analysis Population Description': [strippedAnalysisDescValue],
    '(S) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedAgeRowOneValueTwo],
         '<=18 years': [[strippedAgeRowTwoValueTwo], [strippedAgeRowTwoValueThree]],
         'Between 18 and 65 years': [[strippedAgeRowThreeValueTwo], [strippedAgeRowThreeValueThree]],
         '>=65 years': [[strippedAgeRowFourValueTwo], [strippedAgeRowFourValueThree]]
         }],
    '(S) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedSexRowOneValueTwo],
         'Female': [[strippedSexRowTwoValueTwo], [strippedSexRowTwoValueThree]],
         'Male': [[strippedSexRowThreeValueTwo], [strippedSexRowThreeValueThree]],
         }],
    '(S) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants': [{'Number Analyzed': [strippedRaceRowOneValueThree],
         'Empty': [strippedRaceRowTwoValueTwo]
         }],

    # Column 2

    '(SS) Arm/Group Title': [strippedStandardSurgeryWithOOC],
    '(SS) Arm/Group Description': [strippedStandardSurgeryWithOOContent],
    '(SS) Overall Participants': [strippedOverallValueTwo],
    '(SS) Baseline Analysis Population Description': [strippedAnalysisDescValue],
    '(SS) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedAgeRowOneValueThree],
         '<=18 years': [[strippedAgeRowTwoValueFour], [strippedAgeRowTwoValueFive]],
         'Between 18 and 65 years': [[strippedAgeRowThreeValueFour], [strippedAgeRowThreeValueFive]],
         '>=65 years': [[strippedAgeRowFourValueFour], [strippedAgeRowFourValueFive]]
         }],
    '(SS) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedSexRowOneValueThree],
         'Female': [[strippedSexRowTwoValueFour], [strippedSexRowTwoValueFive]],
         'Male': [[strippedSexRowThreeValueFour], [strippedSexRowThreeValueFive]],
         }],
    '(SS) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedRaceRowOneValueThree],
         'Empty': [strippedRaceRowTwoValueThree]
         }],

    # Column  3

    '(T) Arm/Group Title': [strippedTotal],
    '(T) Arm/Group Description': [strippedTotalContent],
    '(T) Overall Participants': [strippedOverallValueThree],
    '(T) Baseline Analysis Population Description': [strippedAnalysisDescValue],
    '(T) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedAgeRowOneValueFour],
         '<=18 years': [[strippedAgeRowTwoValueSix], [strippedAgeRowTwoValueSeven]],
         'Between 18 and 65 years': [[strippedAgeRowThreeValueSix], [strippedAgeRowThreeValueSeven]],
         '>=65 years': [[strippedAgeRowFourValueSix], [strippedAgeRowFourValueSeven]]
         }],
    '(T) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedSexRowOneValueFour],
         'Female': [[strippedSexRowTwoValueSix], [strippedSexRowTwoValueSeven]],
         'Male': [[strippedSexRowThreeValueSix], [strippedSexRowThreeValueSeven]],
         }],
    '(T) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants': [
        {'Number Analyzed': [strippedSexRowThreeValueSeven],
         'Empty': [strippedRaceRowTwoValueFour]
         }]

    }


df = df.append(DataFrame(data, columns = ['(S) Arm/Group Title', '(S) Arm/Group Description', '(S) Overall Participants','(S) Baseline Analysis Population Description',
                                        '(S) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(S) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(S) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants',
                                          
                                        '(SS) Arm/Group Title', '(SS) Arm/Group Description', '(SS) Overall Participants','(SS) Baseline Analysis Population Description',
                                        '(SS) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(SS) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(SS) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants',

                                        '(T) Arm/Group Title', '(T) Arm/Group Description', '(T) Overall Participants','(T) Baseline Analysis Population Description',
                                        '(T) Age, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(T) Sex, Categorical Measure Type: Count of Participants Unit of measure:  Participants',
                                        '(T) Race and Ethnicity Not Collected Measure Type: Count of Participants Unit of measure:  Participants',
                                        ]
                         ))

df.to_json(r'C:\Users\tolul\OneDrive\Documents\GitHub\WebScrap\delv2.json', orient='records')