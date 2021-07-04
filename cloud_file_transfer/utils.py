from cloud_file_transfer.constants import *

from dotenv import dotenv_values
from boto3.s3.transfer import S3Transfer
from google.cloud import storage

import boto3
import os
import multiprocessing as mp

class CloudUpload(object):
    config = {}

    def __init__(self, path):
        self.indir = path

    def get_aws_s3_upload_list(self):
        return self.config['DEFAULT_UPLOAD_TO_AWS_S3'].split(',')

    def get_gcs_upload_list(self):
        return self.config['DEFAULT_UPLOAD_TO_GCS'].split(',')

    def get_file_ext(self, file_path):
        filename, file_extension = os.path.splitext(file_path)

        # exclude '.' in extension name and return
        return file_extension.lower()[1:]

    def get_file_path(self, dirpath, file_name):
        return dirpath + '/' + file_name

    def upload_file(self, file_path, platform, file):
        if platform == AWS_S3:
            try:
                client = boto3.client('s3',
                                      aws_access_key_id=self.config['AWS_ACCESS_KEY_ID'],
                                      aws_secret_access_key=self.config['AWS_SECRET_ACCESS_KEY'])
                transfer = S3Transfer(client)
                transfer.upload_file(file_path, self.config['AWS_BUCKET_NAME'], file)

                print('upload succeeded for ' + file_path + ' to ' + platform)
            except Exception as e:
                print('upload failed for ' + file_path + ' to ' + platform + ' with message: ' + str(e))

            print(LINE_SEPERATOR)
        elif platform == GCS:
            try:
                client = storage.Client.from_service_account_json(json_credentials_path=self.config['GCS_JSON_CREDENTIALS_PATH'])
                bucket = client.get_bucket(self.config['GCS_BUCKET_NAME'])

                blob = bucket.blob(file)
                blob.upload_from_filename(filename=file_path)

                print('upload succeeded for ' + file_path + ' to ' + platform)
            except Exception as e:
                print('upload failed for ' + file_path + ' to ' + platform + ' with message: ' + str(e))
            print(LINE_SEPERATOR)

    def process_dir(self):
        # read all the files from the directory and its subdirectory

        self.config = dotenv_values()

        master_upload_list = []

        upload_aws_s3_ext_set = set([ext.lower() for ext in self.get_aws_s3_upload_list()])
        upload_gcs_ext_set = set([ext.lower() for ext in self.get_gcs_upload_list()])

        for (dirpath, dirnames, filenames) in os.walk(self.indir):
            for file in filenames:
                file_path = self.get_file_path(dirpath, file)
                file_ext = self.get_file_ext(file_path)
                if file_ext in upload_aws_s3_ext_set:
                    master_upload_list.append((file_path, AWS_S3, file))
                elif file_ext in upload_gcs_ext_set:
                    master_upload_list.append((file_path, GCS, file))

        if master_upload_list:
            print(LINE_SEPERATOR)
            pool = mp.Pool(mp.cpu_count())
            results = pool.starmap_async(self.upload_file, master_upload_list).get()
            pool.close()
            pool.join()