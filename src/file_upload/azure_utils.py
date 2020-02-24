# file_upload utils
from file_upload.utils import generateBlobName 


# files will be uploaded as blobs /w meaningful names [i.e. labels in name] 
def uploadBlob(file, label, container_client, blob_service_client):
    """ uploads a file as a blog upload via a container_client """

    # generates a unique, timestamped, name /w label info
    blob_name = generateBlobName(label)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_client, blob=blob_name)
    print("\nUploading to Azure Storage as blob:\n\t" + blob_name)

    # Upload file
    try:
        with open(file, "rb") as data:
            blob_client.upload_blob(data)
        return
    except Exception as e:
        print("File Upload for blog failed. /n Blobname: %s /n Please see trace: /n %s " % (blob_name, e))
