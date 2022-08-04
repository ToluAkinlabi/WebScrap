import sys
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

def sortParse():
    df = pd.DataFrame()
    format_set = set()
    column_set = set()
    row_set = set()
    lastPage = None
    failedUrl = []

    #Looping through the pages
    pages = np.arange(1,6,1)
    for page in pages:
        while not lastPage:
            try:
                #Request to fetch the whole page
                #clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
                #parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

                #Request to fetch the result page
                pageGetter = requests.get("https://clinicaltrials.gov/ct2/show/results?rslt=With&cntry=US&draw=2&rank=" + str(page))
                pageSoup = BeautifulSoup(pageGetter.content, 'html.parser')

                #Test for last page if it exists
                try:
                    nextPage = pageSoup.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
                    resultPage = str(nextPage['href']) # catches and stores the href to the next page

                    # slices the result page to allow edit to link to display result page
                    slicedResultPage = resultPage[17:]
                    storeNextPage = "https://clinicaltrials.gov/ct2/show/study/" + slicedResultPage  # this gives the full link to the next study page
                    storeNextResultPage = "https://clinicaltrials.gov" + resultPage  # this gives the full link to the next result page
                    # print(storeNextPage)
                    # print(storeNextResultPage)

                except:
                    try:
                        lastPage = pageSoup.find("div", class_="tr-results-nav").find("span", class_="grayed_fore_color", string="Next Study")
                    except:
                        continue



                break

            except :
                print("Error found!", sys.exc_info())
                print(pageGetter)
                print(page)
                #traceback.print_exc()

        if lastPage:
            break

sortParse()

