#!/usr/bin/python
#
# Script for rotate big logfiles

import os
import gzip
import time

logdir = '/var/log/HOSTS/'
ext = '.log'
maxsize = 1000000000


def collector(path, extension, maxsize):
    # TODO: remove archive directory from search path

    bigfiles = []

    for root, dirs, files in os.walk(path):
        for logfile in files:
            if logfile.endswith(extension):
                if os.path.getsize(os.path.join(root, logfile)) > maxsize:
                    bigfiles.append(os.path.join(root, logfile))
    return bigfiles


def compress(fullpath):
    # Default value of gzip compresslevel is 9 (slowest, but max compress)

    arch_dir = '/tmp/archive/' + fullpath.split('/')[-3]
    filename = fullpath.split('/')[-1]

    if not os.path.exists(arch_dir):
        os.makedirs(arch_dir)

    file_in = open(fullpath, 'rb')
    file_out = gzip.open(
        arch_dir + filename + '_' + str(int(time.time())) + '.gz', 'wb')
    file_out.writelines(file_in)
    file_out.close()
    file_in.close()

for i in collector(logdir, ext, maxsize):
    print "Start compression of", str(i)
    compress(i)
    print "End compression of", str(i)
