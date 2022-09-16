import sys
import re
import traceback
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def main():
    df = pd.DataFrame()
    lastPage = None
    finalRowArray = []
    initialRowArray = []

    # Looping through the pages
    pages = np.arange(1,2,1)
    for page in pages:
        while not lastPage:
            try:

                # downloads html page and parse page for readability.
                clinicPage = requests.get("https://clinicaltrials.gov/ct2/show/results?rslt=With&cntry=US&draw=2&rank=" + str(page))
                parseClinicPage = BeautifulSoup(clinicPage.content, "html.parser")

                # Test for last page if it exists
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
                rows = parseClinicPage.find("div", id="tab-body").find("div", class_="tr-indent2").find_all("div",class_
                        ="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find_all("tr")

                # create an empty list
                totalArray = []

                # Collecting data
                for row in rows:
                    # Find all data for the total column for each row
                    header = row.find('td').text.strip().replace(u'\xa0', u' ').replace('\n', ' ').replace('\r', ' ').replace('\u2007', ' ')
                    Total = row.find_all('td')[-1].text.strip().replace(u'\xa0', u' ').replace('\n', ' ').replace('\r', ' ').replace('\u2007', ' ')
                    totalArray.append({header : Total})

                print(totalArray)
            except :
                print("Error found!", sys.exc_info())
                #print(clinicPage)
                #print(page)
                traceback.print_exc()

        if lastPage:
            break
main()
