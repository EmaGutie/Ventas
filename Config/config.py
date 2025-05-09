from dotenv import load_dotenv 
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


load_dotenv(dotenv_path="rutas/database.env")




user=os.getenv ('DB_USER')
password=os.getenv('DB_PASSWORD')
host=os.getenv('DB_HOST')
database=os.getenv('DB_NAME')


DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine= create_engine(DATABASE_CONNECTION_URI)
try:
    with engine.connect() as connection:
        print("la base de datos se conecto exitosamente ")
except SQLAlchemyError as error:
    print(f"la base de datos no se a podido conectar{error}")