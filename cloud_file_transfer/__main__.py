import sys
import argparse

from cloud_file_transfer.utils import CloudUpload

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Upload files to cloud')
    parser.add_argument('indir', type=str, help='Input dir for files')

    # Execute parse_args()
    args = parser.parse_args()

    cp = CloudUpload(args.indir)
    cp.process_dir()


if __name__ == "__main__":
    sys.exit(main())
