"""MainDataset Python Script.

This script is responsible for calling the necessary functions and do the following tasks:
	* Call parseFunc to get the Dictionary
	* Call extract_table to get the DataFrame of a particular table
	* Call create_sqlite to create the SQLite3 File

Format:
	Change the File Location of the file at the fileLoc variable which will then fetch the File from the URL

Made By: Mayank Vachher
"""

from FirstLineParser import parsingFunc
import urllib2
from ExtractTable import extract_table
from CreateTable import create_sqlite

def main():
	fileLoc = "http://kurucz.harvard.edu/atoms/1401/gf1401.gam"
	response = urllib2.urlopen(fileLoc)
	line1 = response.readline()
	myDict = parsingFunc(line1)
	response.close()
	table = extract_table(fileLoc)
	print table.head()
	print table.tail()
	create_sqlite(table)
	
	
if( __name__ == "__main__"):
	main()
