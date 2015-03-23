"""First Line Parser Module.

This module is responsible for Parsing a given String and extracting the Data according to the given format.
The needful is done with the help of parsingFunc, which returns a dictionary of data after a String is given as parameter.

Format:
	The Parsing Function follows the following format (to be read top to down):
		Version Number,
		Number of Lines Saved,
		"lines saved",
		Number of Positive Lines Saved,
		"positive lines saved",
		Number of Even Levels,
		"even",
		Number of Odd Levels,
		"odd levels",
		Unit Value,
		"ion pot cm-1 odd"

Keys:
	'vnum'     -> Version Number
	'lines'    -> Number of Lines Saved
	'poslines' -> Number of Positive Lines Saved
	'evenlvl'  -> Number of Even Levels
	'oddlvl'   -> Number of Odd Levels
	'unitval'  -> Value of ion pot cm-1 odd

Made By: Mayank Vachher
"""

from pyparsing import *

#For testing Purposes
toParse = "14.01     36508 lines saved      3006 positive lines saved    892 even    872 odd levels    131838 ion pot cm-1 odd"

def parsingFunc(toParse):
	"""Return a Dictionary after Parsing the 'toParse' String."""
	#Words/Values to find/Parse
	versionNum 		= Word(printables).setResultsName('vnum')
	linesSaved 		= Word(nums).setResultsName('lines').setParseAction(lambda x: int(x[0]))
	posLinesSaved 	= Word(nums).setResultsName('poslines').setParseAction(lambda x: int(x[0]))
	evenLevels 		= Word(nums).setResultsName('evenlvl').setParseAction(lambda x: int(x[0]))
	oddLevels 		= Word(nums).setResultsName('oddlvl').setParseAction(lambda x: int(x[0]))
	unit 			= Word(nums).setResultsName('unitval').setParseAction(lambda x: int(x[0]))
	
	#Literals to ignore
	lSavedLit 	= Literal("lines saved").suppress()
	pSavedLit 	= Literal("positive lines saved").suppress()
	evenLit 	= Literal("even").suppress()
	oddLit 		= Literal("odd levels").suppress()
	unitLit 	= Literal("ion pot cm-1 odd").suppress()
	
	#Order in which to input Line
	parseFunc = versionNum + linesSaved + lSavedLit + posLinesSaved + pSavedLit + evenLevels + evenLit + oddLevels + oddLit + unit + unitLit
				
	#Result stored as Dictionary
	result = parseFunc.parseString(toParse).asDict()
	
	#Function Check
	print "\nParsed as Dictionary:"
	print result
	return result

def main():
	result = parsingFunc(toParse)
	print "\nStatistics"
	print "---------------------"

	print "File Version Number: "+str(result['vnum'])
	print "Lines Saved: "+str(result['lines'])
	print "Positive Lines Saved: "+str(result['poslines'])
	print "Number of Even Levels: "+str(result['evenlvl'])
	print "Number of Odd Levels: "+str(result['oddlvl'])
	print "ion pot cm-1 odd: "+str(result['unitval'])
	print
	
if __name__ == "__main__":
	main()
