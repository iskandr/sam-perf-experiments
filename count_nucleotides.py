
import argparse
import sys
from collections import Counter
import time 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", default = None,
        help="SAM file to parse")
    
    args = parser.parse_args()

    counts = Counter() 
    print "Loading %s" % args.filename
    with open(args.filename) as f:

    	# skip the header 
    	while True:
    	  pos = f.tell()
          line = f.readline()
    	  if not line.startswith('@'):
            f.seek(pos)
            break

        t0 = time.time()
    	for i, line in enumerate(f):
    		if i % 100000 == 0: 
    			t1 = time.time()
    			print i, line 
    			delta = t1 - t0 
    			print "Lines per second: %0.2f" % (100000.0 / delta)
    			t0 = time.time()
    		parts = line.split('\t', 10)
    		counts.update(parts[9])
    print "Done!"
    print counts 
