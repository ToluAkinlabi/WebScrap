import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

def findFormat():

    clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
    parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")
    nextPage = parseClinicPage.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
    resultPage = str(nextPage['href'])
    slicedResultPage = resultPage[15:]  # slice the result page to allow edit to link to display result page
    storeNextPage = "https://clinicaltrials.gov" + resultPage
    storeNextResultPage = "https://clinicaltrials.gov/ct2/show/results" + slicedResultPage
    slicedResultLink = storeNextResultPage[:-1]  # slice the stored next result page to allow looping over each page

    #Looping through the pages
    pages = np.arange(1,5,1)
    for page in pages:
        clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/study/NCT05167370?rslt=With&cntry=US&draw=2&rank=1")
        parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

        pageGetter = requests.get("https://clinicaltrials.gov/ct2/show/results?rslt=With&cntry=US&draw=2&rank=" + str(page))
        pageSoup = BeautifulSoup(pageGetter.content, 'html.parser')
        nextPage = pageSoup.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
        resultPage = str(nextPage['href'])
        slicedResultPage = resultPage[17:]  # slice the result page to allow edit to link to display result page
        storeNextPage = "https://clinicaltrials.gov" + resultPage
        storeNextResultPage = "https://clinicaltrials.gov/ct2/show/results/" + slicedResultPage

        print (storeNextResultPage)


findFormat()
