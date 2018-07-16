# coding: utf-8

import ex
import bb
import ZD

import cv2
import numpy as np

import os
import time
import glob

class flower:
    infolder = None
    outfolder = None
    outname = None
    P = 1.15
    alphafolder = None
    conv = None
    def __init__(self, infolder,outfolder,outname,conv,P = 1.15,alphafolder = None):
        self.infolder = infolder
        self.outfolder = outfolder
        self.outname = outname
        self.conv = conv
        self.P = P
        self.alphafolder = alphafolder
    def converts(self):
        i = 0
        converter = None
        gp = glob.glob(self.infolder)
        if self.conv == 0:
            print("ex")
            for p in gp:
                p = p.replace("\\","/")
                converter = ex.ex(p,self.outname+"%s"%i,P,self.outfolder)
                converter.convert()
                i += 1
        elif self.conv == 1:
            print("bb")
            ga = glob.glob(self.alphafolder)
            for p in gp:
                a = ga[i]
                p = p.replace("\\","/")
                converter = bb.bb(p,a,self.outname+"%s"%i,self.outfolder)
                converter.convert()
                i += 1
        elif self.conv == 2:
            print("ZD")