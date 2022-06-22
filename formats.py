import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def findFormat():
    format_set = set()
    column_set = set()
    #Looping through the pages
    pages = np.arange(1,38029,1)
    for page in pages:
        clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
        parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

        pageGetter = requests.get("https://clinicaltrials.gov/ct2/show/results?rslt=With&cntry=US&draw=2&rank=" + str(page))
        pageSoup = BeautifulSoup(pageGetter.content, 'html.parser')
        nextPage = pageSoup.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
        resultPage = str(nextPage['href'])

        # slice the result page to allow edit to link to display result page
        slicedResultPage = resultPage[17:]
        storeNextPage = "https://clinicaltrials.gov/ct2/show/study/" + slicedResultPage  #this gives the full link to the next result page
        storeNextResultPage = "https://clinicaltrials.gov" + resultPage  # this gives the full link to the next result page
        #print(storeNextPage)
        #print(storeNextResultPage)

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

    try :
        #gets the numbers of formats
        print(f'Length of format: {len(format_set)}')
        print(f'Format types : {format_set}')
        print(f'Columns : {column_set}')
    except :
        print("Error found!")

findFormat()
