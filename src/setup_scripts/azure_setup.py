import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def getBlobServiceClient(connection_string):
    return BlobServiceClient.from_connection_string(connection_string)  

def touchLabeledImgsContainer(container_name, connection_string):
    """ 
        Setups up a new blob container for labeled blobs with given {container_name}.
        Returns the container if it already exists.
        
        Returns instanced container_client class /w given container_name:
        For details, see: https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python
        
    """

    # Sets up blob service client object
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)   
    # Ensures a acceptable name for the container
    container_name = str(container_name).lower()
    # Create the container and keep container client open / if exists just get the container_client
    try: 
        blob_service_client.create_container(container_name)
    except Exception:
        pass
    
    container_client = blob_service_client.get_container_client(container_name)

    return container_client