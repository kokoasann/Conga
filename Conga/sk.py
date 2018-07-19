# coding: utf-8

import cv2
import numpy as np
import time

class sk:
    def __init__(self,infile,outname,outfolder = None,P = 3):
        self.infile = infile
        self.outname = outname
        self.P = P
        self.outfolder = outfolder
    def convert(self):
        start = time.time()
        img = cv2.imread(self.infile)
        p3 =  np.ones((self.P,self.P,3),np.int)*255
        v = np.array([[p3 for i in range(int(img.shape[1]/self.P))] for j in range(int(img.shape[0]/self.P))])
        ix = 0
        iy = 0
        x2 = 0
        y2 = 0
        x = 0
        y = 0
        print("%s,%s,%s,%s"%(v.shape[0],v.shape[1],v.shape[2],v.shape[3]))
        while iy < v.shape[0]:
            #print("%s,%s,%s,%s[%s,%s]"%(iy,ix,y2,x2,y,x))
            v[iy][ix][y2][x2] = img[y][x]
            if x2 != 2:
                x2+=1
            else:
                x2 = 0
                ix+=1

            if ix >= v.shape[1]:
                ix = 0
                x2 = 0
                if y2 != 2:
                    y2+=1
                else:
                    y2 = 0
                    iy+=1
        
            if x < v.shape[1]*self.P-1:
                x+=1
            else:
                x = 0
                y+=1
        
        x = 0
        y = 0
        imap = np.ones((v.shape[0],v.shape[1],3),np.int)*255
        val = [0,0,0]
        for y in range(imap.shape[0]):
            for x in range(imap.shape[1]):
                val = [0,0,0]
                for v1 in v[y][x]:
                    for v2 in v1:
                        val += v2
                        #print(v2)
                for i in range(self.P):
                    #print(val[i])
                    imap[y][x][i] = int(val[i] / self.P*3)
        print(time.time()-start)
        if self.outfolder == None:
            cv2.imwrite(self.infile[:self.infile.rfind("/")+1]+self.outname+".png",imap)
        elif self.outfolder.rfind("/") == len(self.outfolder):
            cv2.imwrite(self.outfolder+self.outname+".png",imap)
        else:
            cv2.imwrite(self.outfolder+"/"+self.outname+".png",imap)

if __name__ == "__main__":
    start = time.time()
    img = cv2.imread("e:/car.JPG")
    p3 =  np.ones((3,3,3),np.int)*255
    v = np.array([[p3 for i in range(int(img.shape[1]/3))] for j in range(int(img.shape[0]/3))])
    ix = 0
    iy = 0
    x2 = 0
    y2 = 0
    x = 0
    y = 0
    print("%s,%s,%s,%s"%(v.shape[0],v.shape[1],v.shape[2],v.shape[3]))
    while iy < v.shape[0]:
        #print("%s,%s,%s,%s[%s,%s]"%(iy,ix,y2,x2,y,x))
        v[iy][ix][y2][x2] = img[y][x]
        if x2 != 2:
            x2+=1
        else:
            x2 = 0
            ix+=1

        if ix >= v.shape[1]:
            ix = 0
            x2 = 0
            if y2 != 2:
                y2+=1
            else:
                y2 = 0
                iy+=1
        if x < v.shape[1]*3-1:
            x+=1
        else:
            x = 0
            y+=1
        
    x = 0
    y = 0
    imap = np.ones((v.shape[0],v.shape[1],3),np.int)*255
    val = [0,0,0]
    for y in range(imap.shape[0]):
        for x in range(imap.shape[1]):
            val = [0,0,0]
            for v1 in v[y][x]:
                for v2 in v1:
                    val += v2
                    #print(v2)
            for i in range(3):
                #print(val[i])
                imap[y][x][i] = int(val[i] / 9)
    print(time.time()-start)
    cv2.imwrite("e:/carmini.png",imap)
