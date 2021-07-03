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

def get_file_path(dirpath, file_name):
    return dirpath + file_name

def process_files(dirpath, file_list):
    for file in file_list:
        print('Uploading ' + get_file_path(dirpath, file))

def process_dir(path):
    # read all the files from the directory and its subdirectory
    # dirpath, dirnames, filenames = os.walk(path)
    for (dirpath, dirnames, filenames) in os.walk(path):
        if filenames:
            print('Uploading files in ' + dirpath)
            process_files(dirpath, filenames)
            print('*'*72)