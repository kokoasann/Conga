#ver10.6.2
# coding: utf-8

import cv2
import numpy as np
import sys
import time

class ex:
    img = None
    def __init__(self,infile,outname,P,outfolder = None):
        self.infile = infile
        self.outname = outname
        self.outfolder = outfolder
        self.P = P
    def dif(self,l1,l2):
        dif = 0
        if l1 != 0:
            dif = l2 / l1
        else:
            if(l2 == 0):
                dif = 1
            else:
                dif = l2
        return dif

    def ava(self,l1):
        #Ba = np.mean(l1)
        B = 0
        cnt = 0
        for l in l1:
            B += l
            cnt += 1
        if cnt != 0:
            Ba = B / cnt
        else:
            Ba = l1
        return Ba

    def x3(self,x,y):
        im = []
        if x < self.img.shape[1] and y < self.img.shape[0] and x > -1 and y > -1:
            if x < self.img.shape[1]-1 and y < self.img.shape[0]-1 and x > 0 and y > 0:
                im.append(self.img[y][x])
            if x > 0:
                im.append(self.img[y][x-1])
            if x > 0 and y > 0:
                im.append(self.img[y-1][x-1])
            if y > 0:
                im.append(self.img[y-1][x])
        return im
    def convert(self):
        gry = cv2.imread(self.infile)
        self.img = cv2.cvtColor(gry, cv2.COLOR_RGB2GRAY)
        #print("step1")
        total = self.img.shape[0]*self.img.shape[1]

        out = np.zeros((self.img.shape[0],self.img.shape[1],4))
        out[:,:,3] = 0
        for y in range(self.img.shape[0]):
            for x in range(self.img.shape[1]):
                co = 0
                BRG = []
                if x > 2 and y > 2:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x-2,y-2))))
                if y > 2:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x,y-2))))
                if x < self.img.shape[1]-3 and y > 2:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x+2,y-2))))
                if x > 2:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x-2,y))))
                if x < self.img.shape[0]-3:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x+2,y))))
                if x > 2 and y < self.img.shape[0]-3:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x-2,y+2))))
                if y < self.img.shape[0]-3:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x,y+2))))
                if y < self.img.shape[0]-3 and x < self.img.shape[1]-3:
                    BRG.append(self.dif(self.ava(self.x3(x,y)),self.ava(self.x3(x+2,y+2))))
                Bs = sorted(BRG, reverse=True)
                for G in BRG:
                    if Bs[0] == G or Bs[-1] == G or Bs[1] == G or Bs[-2] == G:
                        if G > self.P:
                            co+=1
                            if co >= 2:
                                out[y][x] = [0,0,0,255]
                                break;
        if self.outfolder == None:
            cv2.imwrite(self.infile[:self.infile.rfind("/")]+self.outname+".png",out)
        elif self.outfolder.rfind("/") == len(self.outfolder):
            cv2.imwrite(self.outfolder+self.outname+".png",out)
        else:
            cv2.imwrite(self.outfolder+"/"+self.outname+".png",out)

    

if "__main__" == __name__:
    path = input()
    path = path.replace("\\","/")
    Draw(path,"a",1.15)
