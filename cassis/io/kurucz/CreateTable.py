"""CreateTable Module.

This module is responsible for holding the create_sqlite function. It also imports the necessary modules required for the execution of the function.

Format:
	Call the create_sqlite function with a DataFrame being passed as a Parameter.

Made By: Mayank Vachher
"""

from sqlalchemy import *
from pandas import DataFrame

def create_sqlite(table):
	engine = create_engine('sqlite:///pandastable.sqlite')
	metaData = MetaData()
	pandasTable = Table('PandasTable', metaData,
		Column('id', Integer, primary_key = True),
       		Column('ELEM', String(8), nullable = False),
       		Column('index(J)', Integer, nullable = False),
       		Column('E(cm-1)', Float, nullable = False),
       		Column('J', Float, nullable = False),
       		Column('label', String(10), nullable = False),
       		Column('gLande', Float, nullable = False)
       	)
       	metaData.create_all(engine)
	myConnection = engine.raw_connection()
	table.to_sql(name='PandasTable', con=myConnection, if_exists='replace', index=True)
	myConnection.close()
	
if(__name__ == "__main__"):
	print "Call function only from MainDataset File!"
