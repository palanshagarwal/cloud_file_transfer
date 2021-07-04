import argparse

from utils import CloudUpload

parser = argparse.ArgumentParser(description='Upload files to cloud')
parser.add_argument('indir', type=str, help='Input dir for files')
parser.add_argument('env_file', type=str, help='Environment config file path')

# Execute parse_args()
args = parser.parse_args()

cp = CloudUpload(args.indir, args.env_file)
cp.process_dir()