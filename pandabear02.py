#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    # display first 5 entries of the ciscocsv dataframe
    print(ciscocsv.head())

    # display first 5 entries of the ciscojson dataframe            
    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)



    ## export to json
    ciscodf.to_json("combined_ciscodata.json")

    ## export to csv
    ciscodf.to_csv("combined_ciscodata.csv")

    ## export to Excel
    ciscodf.to_excel("combined_ciscodata.xlsx")


if __name__ == "__main__":
    main()

