from Interfaces.IDataVerificator import IDataVerificator
from csv import DictReader
from typing import List, Dict

# class verifies input data
class DataVerificator(IDataVerificator):

    # verifies data
    def verifyData(self, filename):
        file_handle = open(filename, mode="r", encoding="utf-8-sig")
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
                    file_handle.close()
                    return False

        file_handle.close()

        return True