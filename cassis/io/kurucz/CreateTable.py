"""CreateTable Module.

This module is responsible for holding the create_sqlite function. It also imports the necessary modules required for the execution of the function.

Format:
	Call the create_sqlite function with a DataFrame being passed as a Parameter.

Made By: Mayank Vachher
"""

from sqlalchemy import create_engine
from pandas import DataFrame

def create_sqlite(table):
	engine = create_engine('sqlite:///pandastable.sqlite')
	myConnection = engine.raw_connection()
	table.to_sql(name='pandastable', con=myConnection, if_exists='replace', index=True)
	myConnection.close()
	
if(__name__ == "__main__"):
	print "Call function only from MainDataset File!"
