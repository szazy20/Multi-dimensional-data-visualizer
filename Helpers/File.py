import pandas as pd
import os.path
from csv import DictReader
from typing import List, Dict

# performs operations on the file in order to get a data required to create a plot
class File:

    # non-parameter constructor
    def __init__(self, path):
        self.__path = path

    # gets data
    def getData(self):
        return self.__data

    # gets labels
    def getLabels(self):
        return self.__labels

    # sets labels (based on columns names)
    def __setLabels(self, data):
        self.__labels = data[0].keys()

    # reads chosen file
    def readCsvData(self):
        file_handle = open(self.__path, mode="r", encoding="utf-8-sig")
        csv_reader = DictReader(file_handle)

        # converting data to list excluding invalid values
        dataVerified: List[Dict[str, float]] = []
        for row in csv_reader:
            float_row: Dict[str, float] = {}
            error = False
            for column in row:
                # excluding unnamed columns
                if(column == ''):
                    continue

                # excluding wrong values
                try:
                    float_row[column] = float(row[column])
                except:
                    error = True
                    continue

            # in case of no error data row is added to a data list
            if error == False:
                dataVerified.append(float_row)

        file_handle.close()

        # setting labels names
        self.__setLabels(dataVerified)
        # converting prepared data to DataFrame
        self.__data = pd.DataFrame(dataVerified)
    
    # verifies file
    def verifyFile(self):
        if(self.__checkIfFileExists() != True):
            return "Input file does not exist!"
        elif (self.__checkIfCsvExtension() != True):
            return "Input file is not .csv file!"
        elif(self.__checkIfEmpty() == True):
            return "Input file is empty!"
        return None

    # checks if file exists
    def __checkIfFileExists(self):
        if(self.__path == None):
            return False
        elif(os.path.isfile(self.__path) != True):
            return False

        return True

    # checks if given file has .csv extension
    def __checkIfCsvExtension(self):
        name, extension = os.path.splitext(self.__path)

        if (extension == ".csv"):
            return True
        else:
            return False

    # checks if file is empty
    def __checkIfEmpty(self):
        #df = pd.read_csv(self.__path)
        #if(df.any() == True):
            return False
        #else:
         #   return True