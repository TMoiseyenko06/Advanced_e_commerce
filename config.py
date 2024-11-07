from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://e_commerce_db_se1i_user:bWFDskWNcjeSdQL8C1E8r35nO4CeG4HM@dpg-csmeg3rqf0us738176fg-a.oregon-postgres.render.com/e_commerce_db_se1i'
    DEBUG = True