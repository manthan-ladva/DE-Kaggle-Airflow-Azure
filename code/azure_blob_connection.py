from credentials import *

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


# Container Name
container_name = "<Your Azure Storage's Container Name>"


# Azure Blob Connection
def connect_azure_blob(blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(azure_connect_str)
    return blob_service_client.get_blob_client(container=container_name, blob=blob_name)
