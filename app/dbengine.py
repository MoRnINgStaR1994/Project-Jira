from sqlalchemy import create_engine

engine = create_engine('postgresql://tapi-admin:mystrongpassword@localhost:5432/tapi-db')
