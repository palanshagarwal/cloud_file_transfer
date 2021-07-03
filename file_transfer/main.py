import argparse

from utils import process_dir

parser = argparse.ArgumentParser(description='Upload files to cloud')
parser.add_argument('indir', type=str, help='Input dir for files')

# Execute parse_args()
args = parser.parse_args()

process_dir(args.indir)