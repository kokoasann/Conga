#encoding: utf-8

import cv2
import numpy as np

class bb:
    def __init__(self,infile,alpha,outname,outfolder = None):
        self.infile = infile
        self.alphafile = alpha
        self.outname = outname
        self.outfolder = outfolder
    def convert(self):
        img = cv2.imread(self.infile,-1)
        alp = cv2.imread(self.alphafile,0)
        #alp = cv2.cvtColor(alp,cv2.COLOR_RGB2GRAY)
        out = img.copy()
        out = np.insert(out,3,255,axis = 2)
        out[:,:,3] = alp[:,:]
        if self.outfolder == None:
            cv2.imwrite(self.infile[:self.infile.rfind("/")]+self.outname+".png",out)
        elif self.outfolder.rfind("/") == len(self.outfolder):
            cv2.imwrite(self.outfolder+self.outname+".png",out)
        else:
            cv2.imwrite(self.outfolder+"/"+self.outname+".png",out)