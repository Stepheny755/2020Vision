from google.cloud import storage

def upload_file(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    bucket_name = "letter-clips"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob("1.mp3")

    blob.upload_from_filename("C:/Users/abhay/Documents/Projects/Medhacks2020/Medhacks2020/api/audio/AMP3.mp3")

    print("done upload")