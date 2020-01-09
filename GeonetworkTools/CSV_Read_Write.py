# Read/Write CSV file

import pandas as pd

csvFile = 'sample.csv'

save = 'newfile.csv'
# sample array of data
# mid = [1, 2, 3]
# uuid = ['abc', 'yxd', 'kfg']


# using pandas module to iterate through rows in csv file
def readCSV_pd(file):
    print('Reading CSV file...')
    df = pd.read_csv(file)
    return df


# Sample of iterating content of csv file
# csvData = readCSV_pd(csvFile)
#
# for index, row in csvData.iterrows():
#     print(row['Name'])

# Create csv file
def writeCSV_pd(argv, **kwargs):
    df = pd.DataFrame(kwargs)
    df.to_csv(argv, index=False)
    print("CSV file created...")


# Sample call method
# passing dictionary
# Search = {'Metadata ID': mid, 'UUID': uuid}
# writeCSV_pd(save, **Search)
