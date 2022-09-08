import sys
import re
import traceback
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
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
                rows = parseClinicPage.find("div", id="tab-body").find("div", class_="tr-indent2").find_all("div",class_="tr-indent1 tr-squishScroll")[1].find("table", class_="de-lightBorder").find("tbody").find_all("tr")

                # combine all rows into a combined single list for later use
                for combined in rows:
                    combinedRowArray = []
                    for child in combined.find_all(['td', 'th']):
                        combinedRowArray.append(child.text.strip().replace(u'\xa0', u' ').replace('\n', ' ').replace('\r', ' ').replace('\u2007', ' '))
                    initialRowArray.append(combinedRowArray)

                # same method as above, but storing as a single array per row for easy transform into dictionary
                rowDictKey = None

                for eachRow in rows:
                    eachRowData = []
                    for child in eachRow.find_all(['td', 'th']):
                        eachRowData.append(child.text.strip().replace(u'\xa0', u' ').replace('\n', ' ').replace('\r', ' ').replace('\u2007', ' '))

                    # convert row to dictionary based on the {key : value} structure
                    if re.match("^(Arm|Baseline|Overall)", eachRowData[0]):
                        rowDict = {eachRowData[0]: eachRowData[1:]}
                        finalRowArray.append(rowDict)

                    #Check for keywords and print the equivalent and store in dictionary data type
                    if re.match("^(Age|Sex|Race|Region)", eachRowData[0]):
                        rowDictKey = eachRowData[0]
                        rowDict = {rowDictKey: []}
                        finalRowArray.append(rowDict)
                        continue

                    elif re.match("^(Sex|Race|Region|'')", eachRowData[0]):
                        finalRowArray.append(rowDict)
                        break

                    if rowDictKey:
                        rowDict[rowDictKey].append(eachRowData[1:])


                # Print result of appended data from dictionary
                for eachRow in finalRowArray:
                    print(eachRow)
                break

            except :
                print("Error found!", sys.exc_info())
                #print(clinicPage)
                #print(page)
                traceback.print_exc()

        if lastPage:
            break

main()
