import sys
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np

def main():
    df = pd.DataFrame()
    lastPage = None
    rawArray = []
    secondRawArray = []
    thirdRawArray = []
    fourthRawArray = []
    finalArray = []

    #Looping through the pages
    pages = np.arange(1,4,1)
    for page in pages:
        while not lastPage:
            try:

                # downloads html page and parse page for readability.
                clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results?rslt=With&cntry=US&draw=2&rank=" + str(page))
                parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

                #Test for last page if it exists
                try:
                    nextPage = parseClinicPage.find("div", class_="tr-results-nav").find(class_="tr-next-link", href=True)
                    resultPage = str(nextPage['href']) # catches and stores the href to the next page

                    # slices the result page to allow edit to link to display result page
                    slicedResultPage = resultPage[17:]

                except:
                    try:
                        lastPage = parseClinicPage.find("div", class_="tr-results-nav").find("span", class_="grayed_fore_color", string="Next Study")
                    except:
                        continue

                # parse row one after the other to get contents
                rows = parseClinicPage.find("div", id="tab-body").find("div", class_="tr-indent2").find_all("div",class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find_all("tr")
                for eachRow in rows:
                    for child in eachRow.find_all(['td', 'th']):
                        rawArray.append(child.text.strip())

                # remove \xa0, \u2007, \n, \r from code
                for item in rawArray:
                    secondRawArray.append(item.replace(u'\xa0', u''))
                for item in secondRawArray:
                    thirdRawArray.append(item.replace('\n', ''))
                for item in thirdRawArray:
                    fourthRawArray.append(item.replace('\r', ''))
                for item in fourthRawArray:
                    finalArray.append(item.replace('\u2007', ''))

                print(finalArray)
                break


            except :
                print("Error found!", sys.exc_info())
                print(clinicPage)
                print(page)
                #traceback.print_exc()

        if lastPage:
            break

main()

