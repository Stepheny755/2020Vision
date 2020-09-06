from google.cloud import storage

#Need to use actual inputs instead of placeholders
def upload_file(sourceFile, index):
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./smiling-audio-288604-bfa5f98402cd.json"

    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    bucket_name = "letter-clips"
    source = convert(sourceFile, index)

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(str(index) + ".mp3")

    blob.upload_from_filename(source)

    print("done upload")

def convert(sourceFile, index):
    import pydub
    import os

    os.environ["PATH"] = "../ffmpeg/bin"

    sound = pydub.AudioSegment.from_wav(sourceFile)
    exportPath = "./audio/" + str(index) + ".mp3"
    sound.export(exportPath, format="mp3")
    return exportPath