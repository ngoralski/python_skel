#!/usr/bin/env python3

import sys
import argparse
import json

version = "0.1"

parser = argparse.ArgumentParser(description='My beautiful program')
parser.add_argument('--conf', type=str, help='configuration file to use', dest="conf")
parser.add_argument('--dryrun', help='do not create snow ticket just add a comment', dest="dryrun", action="store_true")
parser.add_argument('--debug', help='display more info', dest="debug", action="store_true")
parser.add_argument('--version', help='display software info', dest="version", action="store_true")

args, unknown = parser.parse_known_args()

with open('../conf/' + args.conf) as fconfig:
    config = json.load(fconfig)


if args.debug:
    print("Configuration file: %s." % args.conf)

if args.version:
    print("Version: %s." % version)


jconf = json.loads(args.conf)


