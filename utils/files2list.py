'''Helper that lists files in src folders, used to copy/paste output
   in meson.build file'''
import argparse
import glob
import os

def pretty_print(items):
    for i in items:
        print('    \'{}\','.format(i))


def src(src):
    # List files in src
    cfiles = os.path.join(src, '*.c')
    #files = [os.path.basename(f) for f in glob.glob(cfiles)]
    files = glob.glob(cfiles)
    files.sort()
    #print(files)
    return files


parser = argparse.ArgumentParser()
parser.add_argument('--src', help='Path to folder')
args = parser.parse_args()
if args.src:
    #print('src: {}'.format(args.src))
    result = src(args.src)

pretty_print(result)