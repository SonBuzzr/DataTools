# Script to register DOI from CSV file with list of information
# Change Identifier and user credentials as require
# Required Module
# datacite==1.0.1
# pandas==0.25.3

from datacite import DataCiteMDSClient, schema41
import pandas as pd
import logging
import time
import config as cfg

# Input csv file for generating DOI
csvFile = 'Metadata Info.csv'

# Date and time for logging information
date_time = time.strftime('%Y%m%d_%H%M%S')

# Prefix for Datacite
prefix = cfg.Prefix['TEST']  # Change RDS or TEST

# User login
login_user = cfg.TestLogin['username']  # Change TestLogin to RDSLogin
login_pass = cfg.TestLogin['password']

# URL link to the Datacite
url = 'https://mds.test.datacite.org'  # Change to mds.datacite.org or mds.test.datacite.org

organization = 'ICIMOD'  # Change organization name


def generate_new_doi(*args):
    # If you want to generate XML for earlier versions, you need to use either the
    # schema31, schema40 or schema41 instead.

    data = {
        "identifier": {
            "identifier": prefix + "/RDS." + str(args[0]),
            "identifierType": "DOI"
        },
        "creators": [
            {
                "creatorName": organization
            }
        ],
        "titles": [
            {
                "title": args[1]
            }
        ],
        "publisher": organization,
        "publicationYear": args[2],
        "language": "en-us",
        "resourceType": {
            "resourceTypeGeneral": "Dataset"
        },
        "rightsList": [
            {
                "rights": "Creative Commons Attribution 4.0 International (CC-BY-4.0)",
                "rightsURI": "https://creativecommons.org/licenses/by/4.0",
                "lang": "en-us"
            }
        ],
        "descriptions": [
            {
                "descriptionType": "Abstract",
                "description": args[3]
            }
        ],
    }

    # Validate dictionary
    # assert schema41.validate(data)

    # Generate DataCite XML from dictionary.
    doc = schema41.tostring(data)
    # print(doc)

    # Initialize the MDS client.
    d = DataCiteMDSClient(
        username=login_user,
        password=login_pass,
        url=url,
        prefix=prefix,
    )

    # Set metadata for DOI
    d.metadata_post(doc)

    # Mint new DOI
    d.doi_post(prefix + '/RDS.' + str(args[0]), args[4])

    logging.basicConfig(filename='logs/DOI_generation_Log_' + date_time + '.log', filemode='w',
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO)
    logging.info("{} DOI Registration for id={} and title={}".format(args[5], args[0], args[1]))
    print(args[5], prefix + '/RDS.' + str(args[0]), args[4])


# using pandas module to iterate through rows in csv file
def readCSV_pd(file):
    df = pd.read_csv(file)
    df.index = df.index + 1
    print("Reading CSV file ...")
    for index, row in df.iterrows():
        Id = row['ID']
        title = row['Title']
        date = row['Date']
        abstract = row['Abstract']
        link = row['Link']
        print(Id, title, date[0:4], abstract, link, index)
        # generate_new_doi(Id, title, date[0:4], abstract, link, index)
    print("DOI Generation Completed...")


readCSV_pd(csvFile)
