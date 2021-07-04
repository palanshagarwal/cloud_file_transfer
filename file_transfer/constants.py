DEFAULT_IMAGES = ['jpg', 'png', 'svg', 'webp', 'jpeg']

DEFAULT_MEDIA = ['mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm']

DEFAULT_DOCUMENT = ['doc', 'docx', 'csv', 'pdf']

DEFAULT_UPLOAD_TO_AWS_S3 = DEFAULT_IMAGES + DEFAULT_MEDIA

DEFAULT_UPLOAD_TO_GCS = DEFAULT_DOCUMENT

AWS_S3 = 'aws_s3'
GCS = 'gcs'