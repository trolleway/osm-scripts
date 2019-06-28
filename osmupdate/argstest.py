import argparse
import os


def get_args():
    p = argparse.ArgumentParser(description='Test arguments')
    p.add_argument('--url', help='pbf file url', type=str)
    return p.parse_args()
 
def process():

    args = get_args()
    
    directory='/data'
    filename = os.path.join(directory,'test.txt')
    f = open(filename, 'w' )
    f.write(args.url)
    f.close()
    
   
process()
