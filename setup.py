from setuptools import setup

setup(
    name='cloud_file_transfer',
    version='0.1.0',    
    description='Upload files based on extensions to S3 and GCS',
    url='https://github.com/py-geek/cloud_file_transfer',
    author='Palansh Agarwal',
    author_email='palanshagarwal@gmail.com',
    license='BSD',
    packages=['cloud_file_transfer'],
    install_requires=['boto3==1.16.63',
                      'google-cloud-storage==1.32.0',
                      'python-dotenv==0.18.0',                
                      ],

    classifiers=[],
)