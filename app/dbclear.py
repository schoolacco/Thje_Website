from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
# Assuming you have an engine and metadata object
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///'+ os.path.join(basedir, 'app.db')) # Replace with your database URI
metadata = MetaData()
metadata.reflect(bind=engine) # Reflect existing tables

Session = sessionmaker(bind=engine)
session = Session()

try:
    for table_name in metadata.tables:
        table = metadata.tables[table_name]
        session.execute(table.delete()) # Execute a DELETE statement for each table
    session.commit()
except Exception as e:
    session.rollback()
    print(f"Error clearing database: {e}")
finally:
    session.close()
'''NONE OF THIS IS MY OWN CODE, THIS WAS JUST TAKEN FROM ONLINE TO CLEAR THE DATABASE AFTER RECIEVING INVALID SUBMITTED DATA'''