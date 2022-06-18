import pandas as pd
import requests
from bs4 import BeautifulSoup

clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

clinicResultPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
parseClinicResultPage = BeautifulSoup(clinicResultPage.content, "html.parser")

currentStudyPage = parseClinicPage.find("div", id="main-content").find("div", id="tabs").find("li", id="tabular").find("a",href=True)
storeCurrentStudyPage = "https://clinicaltrials.gov" + str(currentStudyPage['href'])
print(storeCurrentStudyPage)

nextPage = parseClinicPage.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
storeNextPage = "https://clinicaltrials.gov" + str(nextPage['href'])
print(storeNextPage)

nextResultPage = parseClinicResultPage.find("div", id="main-content").find("div", id="tabs").find("li", id="tabular").find("a",href=True)
storeNextResultPage = "https://clinicaltrials.gov" + str(nextResultPage['href'])
print(storeNextResultPage)

