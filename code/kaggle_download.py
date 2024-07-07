from azure_blob_connection import *

from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
import tempfile


"""
Dataset Link = 'https://www.kaggle.com/datasets/bwandowando/rotten-tomatoesall-time-best-super-hero-movies'

Here,
dataset = "<username>/<dataset>"
"""
dataset = 'bwandowando/rotten-tomatoesall-time-best-super-hero-movies'

def run_kaggle_etl():
    # Kaggle API Call
    api = KaggleApi()
    api.authenticate()

    # Download File in Temperory Directory
    with tempfile.TemporaryDirectory() as temp_dir:
        api.dataset_download_files(dataset, path=temp_dir, unzip=False)

        # Join Path with Temperory Directory
        zip_file_path = os.path.join(temp_dir, dataset.split('/')[-1] + '.zip')
        with ZipFile(zip_file_path) as z:
            for file_info in z.infolist():
                if file_info.is_dir():
                    continue
                with z.open(file_info) as file:
                    file_content = file.read()
                    blob_name = file_info.filename
                    
                    # Create Connection with Azure Blob and Upload Files
                    client = connect_azure_blob(blob_name)
                    client.upload_blob(file_content, overwrite=True)
                    
