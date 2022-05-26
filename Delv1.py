import requests
from bs4 import BeautifulSoup

# downloads html page and parse page for readability.
clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05167370?rslt=With&cntry=US&draw=2&rank=1&view=results")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

#Baseline Table Scrap
#Table Title

baselineHeading = parseClinicPage.find_all('span', class_="ct-header2")[1]
strippedBaselineHeading = baselineHeading.text.strip()
print(strippedBaselineHeading)

#Table data content
tableRowTitle = parseClinicPage.find_all("td", class_="de-baselineLabelCell")[0]
strippedTableRowTitle = tableRowTitle.text.strip()
print(strippedTableRowTitle)

tableRowTitleContent = parseClinicPage.find("th", class_="de-baselineLabelCell")
strippedTableRowTitleContent = tableRowTitleContent.text.strip()
print(strippedTableRowTitleContent)