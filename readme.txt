Transfer files in a directory and it's sub directory to AWS S3 and Google cloud storage

Install as a package using: python -m pip install git+https://github.com/py-geek/cloud_file_transfer.git

Usage instructions:
1. Copy the env.example file in repo to your system and rename it to .env
2. Populate the .env file with relevant values

Use below command to start uploading files: 
cloud_file_transfer /path/to/directory


Executing Unittests:
1. clone the repo
2. install the requirements from requirements.txt
3. Make sure the .env file is updated
4. Use this command to execute tests: python -m unittest cloud_file_transfer/tests/test.py