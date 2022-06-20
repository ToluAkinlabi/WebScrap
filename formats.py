import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def findFormat():

    #Looping through the pages
    pages = np.arange(1,20,1)
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

        #get length of row and columns
        #columns
        colns = pageSoup.find("div", class_="tr-indent1 tr-squishScroll").find_all("table", class_="de-lightBorder")[1].find("tbody").find("tr").find_all()
        getColumnFormat = str(len(colns))

        #rows
        rows = pageSoup.find("div", class_="tr-indent1 tr-squishScroll").find_all("table", class_="de-lightBorder")[1].find("tbody").find_all()
        getRowFormat = str(len(rows))

        print("The format for page " + str(page) + " is" + " " + getRowFormat + " rows by " + getColumnFormat + " columns")


#findFormat()

clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results/NCT05110014?rslt=With&cntry=US&draw=2&rank=3")
parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

colns = parseClinicPage.find_all("div", class_="tr-indent1 tr-squishScroll")[1].find("div", class_="tr-indent2").find("table", class_="de-lightBorder").find("tbody").find("tr").find_all()
print(colns)
getColumnFormat = str(len(colns))

rows = parseClinicPage.find_all("div", class_="tr-indent1 tr-squishScroll")[1].find("div", class_="tr-indent2").find("table", class_="de-lightBorder").find("tbody").find_all()
print(rows)
getRowFormat = str(len(rows))

print("The format is" + " " + getRowFormat + " rows by " + getColumnFormat + " columns")