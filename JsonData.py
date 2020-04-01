import json
import Data

def json_write(filename): # Writes data from JSON file into the pdfMetaDataAdd function
    jsonName = filename[:-5]
    with open(filename) as f:
        json_array = json.load(f)
        for doc in json_array['Docs']:
            index_details = {"Id": None, "Reference Number": None, "Date Created": None, "Keywords": None, "Author": None}
            index_details['Id'] = doc['Id']
            index_details["Reference Number"] = doc['Reference']
            index_details["Date Created"] = doc['Created']
            index_details["Keywords"] = doc["Description"]
            index_details["Author"] = doc["Cabinet"]
            Data.pdfMetaDataAdd(index_details['Id'], index_details['Reference Number'], index_details["Author"], index_details["Date Created"] ,index_details['Keywords'], jsonName)




if __name__ == '__main__':
    json_write('Test json file')