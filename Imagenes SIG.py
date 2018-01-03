#!/usr/bin/env python
# coding:latin-1
	
from pylab import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

import struct
class srtmParser(object):

    def parseFile(self,filename):
        # read 1,442,401 (1201x1201) high-endian
        # signed 16-bit words into self.z
        fi=open(filename,"rb")
        contents=fi.read()
        fi.close()
        self.z=struct.unpack(">1442401H", contents)

    def writeCSV(self,filename):
        if self.z :
            fo=open(filename,"w")
            for row in range(0,1201):
                offset=row*1201
                thisrow=self.z[offset:offset+1201]
                rowdump = ",".join([str(z) for z in thisrow])
                fo.write("%s\n" % rowdump)
            fo.close()
        else:
            return None

if __name__ == '__main__':

    f = srtmParser()
    f.parseFile(r"N19W099.hgt")
    f.writeCSV(r"N19W099.asc")
    zzz = np.zeros((1201,1201))
    for r in range(0,1201):
        for c in range(0,1201):
            va=f.z[(1201*r)+c]
            if (va==65535 or va<0 or va>2000):
                va=0.0
            zzz[r][c]=float(va)
    # logarithm color scale
    zz=np.log1p(zzz)
    imshow(zz, interpolation='bilinear',cmap=cm.gray,alpha=1.0)
    grid(False)
    show()
