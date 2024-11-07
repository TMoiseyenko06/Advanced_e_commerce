from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'{DATABASE_URI}'
    DEBUG = True