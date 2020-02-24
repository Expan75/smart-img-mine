import os, uuid, time
from datetime import datetime


def generateBlobName(label):
    """ Generates and returns blob name in the format {label}_{uuid()}_{unix_timestamp} """

    # Generates and formats a timestamped blob name
    timestamp = datetime.now().strftime("%s")
    blob_name = str(label).lower() + "_" + str(uuid.uuid4()) + "_" + timestamp

    return blob_name

print(generateBlobName("lion"))
