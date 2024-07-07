import os
from dotenv import load_dotenv

load_dotenv()


# Keys Connection
kaggle_user_name = os.getenv('KAGGLE_USERNAME')
kaggle_user_key = os.getenv('KAGGLE_KEY')
azure_connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


# Kaggle ENV Setup
os.environ['KAGGLE_USERNAME'] = kaggle_user_name
os.environ['KAGGLE_KEY'] = kaggle_user_key
