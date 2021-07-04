from constants import *

import os

def get_image_list():
    return DEFAULT_IMAGES

def get_media_list():
    return DEFAULT_MEDIA

def get_document_list():
    return DEFAULT_DOCUMENT

def get_aws_s3_upload_list():
    return DEFAULT_UPLOAD_TO_AWS_S3

def get_gcs_upload_list():
    return DEFAULT_UPLOAD_TO_GCS

def get_file_ext(file_path):
    filename, file_extension = os.path.splitext(file_path)

    # exclude '.' in extension name and return
    return file_extension.lower()[1:]

def get_file_path(dirpath, file_name):
    return dirpath + '/' + file_name

def upload_files(file_data, platform):
    def upload_file(file, platform):
        print('uploaded ' + file + ' to ' + platform)

    if isinstance(file_data, list):
        for file in file_data:
            upload_file(file, platform)
    else:
        upload_file(file, platform)     

def process_dir(path):
    # read all the files from the directory and its subdirectory
    # dirpath, dirnames, filenames = os.walk(path)
    _upload_aws_s3_list = []
    _upload_gcs_list = []

    upload_aws_s3_ext_set = set(get_aws_s3_upload_list())
    upload_gcs_ext_set = set(get_gcs_upload_list())

    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            file_path = get_file_path(dirpath, file)
            file_ext = get_file_ext(file_path)
            if file_ext in upload_aws_s3_ext_set:
                _upload_aws_s3_list.append(file_path)
            elif file_ext in upload_gcs_ext_set:
                _upload_gcs_list.append(file_path)

    if _upload_aws_s3_list:
        upload_files(_upload_aws_s3_list, AWS_S3)

    if _upload_gcs_list:
        upload_files(_upload_gcs_list, GCS)












