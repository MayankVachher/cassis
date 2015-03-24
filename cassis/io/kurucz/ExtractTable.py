"""ExtractTable Module.

This module is responsible for holding the extract_table function. It also imports the necessary modules required for the execution of the function.

Format:
	* Call the extract_table function with a File Location being passed as a Parameter.
	* Customise the table Headers, the Column Widths and the read_fwf parameters as per your needs.
	

Made By: Mayank Vachher
"""

from pandas import read_fwf

def extract_table(fileLoc):
	tableHeaders = ['ELEM','index(J)','E(cm-1)','J','label','gLande']
	colwidths = [(0,8),(10,13),(13,26),(27,30),(30,42),(43,48)]
	datatypes={0: str, 1: int, 2: float, 3: float, 4: str, 5: float}
	return read_fwf(fileLoc, skiprows=38, names=tableHeaders,colspecs=colwidths,nrows=1802-38, converters=datatypes)
	
if(__name__ == "__main__"):
	print "Call function only from MainDataset File!"
