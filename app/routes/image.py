from uuid import uuid4

from fastapi import APIRouter, status, UploadFile, File
from google.cloud import storage

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_image(file: UploadFile = File(...)):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("top-trumps")
    blob = bucket.blob(str(uuid4()))
    blob.upload_from_file(file.file, content_type=file.content_type)
    return {"url": blob.public_url}
