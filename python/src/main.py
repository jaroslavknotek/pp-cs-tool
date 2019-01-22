import synchronizer
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("--dirpath", help="path to config file", type=str)
parser.add_argument("--archivepass", help="pass to archive to which data are archived", type=str)
parser.add_argument("--odsecret", help="one drive secret", type=str)
parser.add_argument("--odid", help="one drive id", type=str)
args = parser.parse_args()

logging.info("starting synchronizing folders")
synchronizer.sync(args.dirpath, args.archivepass, args.odid, args.odsecret)
logging.info("synchronization if finished")
