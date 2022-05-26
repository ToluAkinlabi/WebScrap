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

