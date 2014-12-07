#!/usr/bin/python2.7
#
# Script for rotate big logfiles

import os
import gzip

logdir = '/var/log/'
ext = '.log'
maxsize = 1000000

def collector(path, extension, maxsize):
    bigfiles = []

    for root, dirs, files in os.walk(path):
        for logfile in files:
            if logfile.endswith(extension):
                if os.path.getsize(os.path.join(root, logfile)) > maxsize:
                    bigfiles.append(os.path.join(root, logfile))
    return bigfiles

def compress(fullpath):
    arch_dir = '/tmp/archive/'
    filename = fullpath.split('/')[-1]

    if not os.path.exists(arch_dir):
        os.makedirs(arch_dir)

    file_in = open(fullpath, 'rb')
    file_out = gzip.open(arch_dir+filename+'.gz', 'wb')
    file_out.writelines(file_in)
    file_out.close()
    file_in.close()


for file in collector(logdir, ext, maxsize):
    compress(file)
