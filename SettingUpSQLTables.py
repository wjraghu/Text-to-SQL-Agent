#  Setting Up SQL Tables

# First, we need to set up the SQL tables that the agent will query. Here is an example of creating a table named receipts using SQLAlchemy:

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, insert, text
engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()
# Create receipts table
receipts = Table(
   "receipts",
   metadata_obj,
   Column("receipt_id", Integer, primary_key=True),
   Column("customer_name", String(16), primary_key=True),
   Column("price", Float),
   Column("tip", Float),
)
metadata_obj.create_all(engine)
# Insert rows into receipts table
rows = [
   {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
   {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
   {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
   {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]
for row in rows:
   stmt = insert(receipts).values(**row)
   with engine.begin() as connection:
       connection.execute(stmt)
