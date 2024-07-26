from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class which allows us to define classes that map to tables
Base = declarative_base()

# Define the class that maps to the table
class Customer(Base):
    __tablename__ = 'customers'  # Cambia a minúsculas
    __table_args__ = {'schema': 'ecommerce'}

    customer_id = Column(Integer, primary_key=True)
    customer_unique_id = Column(Integer)
    customer_zip_code_prefix= Column(Integer)
    customer_city= Column(String)
    customer_state = Column(String)

# Create an engine that connects to the PostgreSQL server
conn ='postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(conn)

# Create a session
conn_session = sessionmaker(bind=engine)
session = conn_session()

# Execute the query
customers = session.query(Customer).limit(10)

# Extract the data and create a list of tuples
data = [ (customer.customer_id,
          customer.customer_unique_id,
          customer.customer_zip_code_prefix,
          customer.customer_city,
          customer.customer_state)
    for customer in customers]