#ver2
#coding: utf-8

import numpy as np
import cv2

black = [0,0,0,255]
clear = [0,0,0,0]
def allC(px1,px2):
    tf = 0
    for i in range(4):
        if px1[i] == px2[i]:
            tf += 1
    if tf == 4:
        return True
    else:
        return False

def noiseDel(path,name,num = 0.2,falder = "e:/"):
    
    img = cv2.imread(path,-1)
    pre = img.copy()
    #縮小
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y][x][3] == 255:
                if y != 0:
                    if img[y-1][x][3] == 0:
                        pre[y][x] = clear
                if y != img.shape[0]-1:
                    if img[y+1][x][3] == 0:
                        pre[y][x] = clear
                if x != 0:
                    if img[y][x-1][3] == 0:
                        pre[y][x] = clear
                if x != img.shape[1]-1:
                    if img[y][x+1][3] == 0:
                        pre[y][x] = clear
    out = pre.copy()
    #拡大
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if allC(pre[y][x],black):
                if y != 0:
                    out[y-1][x] = black
                if x != 0:
                    out[y][x-1] = black
                if y != img.shape[0]-1:
                    out[y+1][x] = black
                if x != img.shape[1]-1:
                    out[y][x+1] = black
    if(num == 0.2):
        cv2.imwrite("c:/py/tesblack.png",out)
    else:
        cv2.imwrite("%s%s_%s.png"%(falder,name,num),out)
class zd:
    def __init__(self,infile,outname,outfolder = None,P = 1):
        self.infile = infile
        self.outname = outname
        self.outfolder = outfolder
        self.P = P
    def convert(self):
        img = cv2.imread(self.infile,-1)
        pre = img.copy()
        #縮小
        for i in range(self.P):
            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    if img[y][x][3] == 255:
                        if y != 0:
                            if img[y-1][x][3] == 0:
                                pre[y][x] = clear
                        if y != img.shape[0]-1:
                            if img[y+1][x][3] == 0:
                                pre[y][x] = clear
                        if x != 0:
                            if img[y][x-1][3] == 0:
                                pre[y][x] = clear
                        if x != img.shape[1]-1:
                            if img[y][x+1][3] == 0:
                                pre[y][x] = clear
        out = pre.copy()
        #拡大
        for i in range(self.P):
            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    if allC(pre[y][x],black):
                        if y != 0:
                            out[y-1][x] = black
                        if x != 0:
                            out[y][x-1] = black
                        if y != img.shape[0]-1:
                            out[y+1][x] = black
                        if x != img.shape[1]-1:
                            out[y][x+1] = black
        if self.outfolder == None:
            cv2.imwrite(self.infile[:self.infile.rfind("/")+1]+self.outname+".png",out)
        elif self.outfolder.rfind("/") == len(self.outfolder):
            cv2.imwrite(self.outfolder+self.outname+".png",out)
        else:
            cv2.imwrite(self.outfolder+"/"+self.outname+".png",out)


if __name__ == "__main__":
    black = [0,0,0,255]
    clear = [0,0,0,0]
    img = cv2.imread("e:/skr3.ex10.6.png",-1)
    #out = np.zeros((img.shape[0],img.shape[1],4))
    pre = img.copy()
    #縮小
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y][x][3] == 255:
                if y != 0:
                    if img[y-1][x][3] == 0:
                        pre[y][x] = clear
                if y != img.shape[0]-1:
                    if img[y+1][x][3] == 0:
                        pre[y][x] = clear
                if x != 0:
                    if img[y][x-1][3] == 0:
                        pre[y][x] = clear
                if x != img.shape[1]-1:
                    if img[y][x+1][3] == 0:
                        pre[y][x] = clear
    out = pre.copy()
    #拡大
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if allC(pre[y][x],black):
                if y != 0:
                    out[y-1][x] = black
                if x != 0:
                    out[y][x-1] = black
                if y != img.shape[0]-1:
                    out[y+1][x] = black
                if x != img.shape[1]-1:
                    out[y][x+1] = black
    cv2.imwrite("c:/py/tesblack.png",out)
    print("perfect")