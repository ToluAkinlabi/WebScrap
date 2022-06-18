import pandas as pd
import requests
from bs4 import BeautifulSoup

clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

nextPage = parseClinicPage.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
resultPage = str(nextPage['href'])
slicedResultPage = resultPage[15:]
storeNextPage = "https://clinicaltrials.gov" + resultPage
storeNextResultPage = "https://clinicaltrials.gov/ct2/show/results" + slicedResultPage
print(storeNextPage)
print(storeNextResultPage)

