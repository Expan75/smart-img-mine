# # Config Imports
# from config import config

# Std. imports
import os

# Imports generated container_client 
from setup_scripts.azure_setup import getBlobServiceClient, touchLabeledImgsContainer

# Uploads utils
from file_upload.azure_utils import uploadBlob


# Test upload flow
label = "sealion"
file = "src/data/something.txt"

# CONSTS SETUP
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", None)
CONTAINER_NAME  = os.getenv("AZURE_STORAGE_CONTAINER_NAME", None)

# Get blob client
blob_service_client = getBlobServiceClient(CONNECTION_STRING)


# Error reporting TODO: de-vague-ify
try:
    container_client = touchLabeledImgsContainer(CONTAINER_NAME, CONNECTION_STRING)
except Exception as e:
    print("Container could not be generated, please see trace: /n %s" % e)
    pass


# Upload blob
uploadBlob(file, label, container_client, blob_service_client)

