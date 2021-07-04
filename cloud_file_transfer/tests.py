import unittest
import uuid
import os
import boto3

from cloud_file_transfer.utils import CloudUpload
from dotenv import dotenv_values

class TestCloudUpload(unittest.TestCase):
    ENV_FILE_PATH = '/Users/pygeek/repos/ecodedash/cloud_file_transfer/.env'
    config = {}

    def head_object_s3(self, key):
        "check if a file exists on s3"
        client = boto3.client('s3',
                              aws_access_key_id=self.config['AWS_ACCESS_KEY_ID'],
                              aws_secret_access_key=self.config['AWS_SECRET_ACCESS_KEY'])
        try:
            res = client.head_object(Bucket=self.config['AWS_BUCKET_NAME'], Key=key)
        except Exception as e:
            if e.response['Error']['Code'] == '404':
                return False, e.response['Error']['Message']
        else:
            return True, res

    def delete_object_s3(self, key):
        client = boto3.client('s3',
                              aws_access_key_id=self.config['AWS_ACCESS_KEY_ID'],
                              aws_secret_access_key=self.config['AWS_SECRET_ACCESS_KEY'])

        client.delete_objects(Bucket=self.config['AWS_BUCKET_NAME'],
                              Delete={'Objects': [{'Key': key}]})

    def tttttest_gcs_upload_success(self):
        test_id = str(uuid.uuid4())
        self.config = dotenv_values(self.ENV_FILE_PATH)

        gcs_upload_ext = self.config['DEFAULT_UPLOAD_TO_GCS'].split(',')[0]
        # create a mock file to test GCS upload
        gcs_file_name = test_id + 'test_upload.' + gcs_upload_ext
        gcs_file_path = '/tmp/' + gcs_file_name
        with open(gcs_file_path, 'w') as document: pass

        # Delete the mock files from system
        print(s3_file_name)
        os.remove(gcs_file_path)

    def test_aws_upload_success(self):
        test_id = str(uuid.uuid4())
        self.config = dotenv_values(self.ENV_FILE_PATH)

        # get a extension for aws upload set in config
        s3_upload_ext = self.config['DEFAULT_UPLOAD_TO_AWS_S3'].split(',')[0]
        # create a mock file to test AWS upload
        s3_file_name = test_id + 'test_upload.' + s3_upload_ext
        s3_file_path = '/tmp/' + s3_file_name
        with open(s3_file_path, 'w') as document: pass

        cp = CloudUpload('/tmp', self.ENV_FILE_PATH)
        cp.process_dir()

        # Delete the mock files from system
        print(s3_file_name)
        os.remove(s3_file_path)

        # check uploaded file on AWS S3
        status, _ = self.head_object_s3(s3_file_name)

        # delete the file from s3
        self.delete_object_s3(s3_file_name)

        # actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        self.assertEqual(status, True)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         TestCloudUpload.ENV_FILE_PATH = sys.argv.pop()
#     unittest.main()