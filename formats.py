import sys
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

def findFormat():
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

                #get length of row and columns
                #columns
                colns = pageSoup.find("div",id="tab-body").find("div", class_="tr-indent2").find_all("div", class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find("tr").find().find_next_siblings()
                getColumnFormat = str(len(colns) + 1)

                #rows
                rows = pageSoup.find("div",id="tab-body").find("div", class_="tr-indent2").find_all("div", class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find("tr").find_next_siblings()
                getRowFormat = str(len(rows) + 1)

                print("The format for page " + str(page) + " is" + " " + getRowFormat + " rows by " + getColumnFormat + " columns")

                #stores column format and row format
                format_set.add(getRowFormat + "," + getColumnFormat)
                column_set.add(getColumnFormat)
                row_set.add(getRowFormat)

                data = {'Page': [page], 'Rows': [getRowFormat], 'Columns': [getColumnFormat]}
                df = df.append(DataFrame(data, columns=['Page', 'Rows', 'Columns']))
                df.to_json(r'C:\Users\tolul\OneDrive\Documents\GitHub\WebScrap\jsonresult.json', orient='records')

                break

            except :
                print("Error found!", sys.exc_info())
                print(pageGetter)
                print(page)
                #traceback.print_exc()

        if lastPage:
            break

    # gets the numbers of formats
    print(f'Length of format: {len(format_set)}')
    print(f'Format types : {format_set}')
    print(f'Columns : {column_set}')
   # print(f'Rows : {row_set}')


findFormat()

