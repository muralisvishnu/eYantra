# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.2
*  Filename: Task1.2.py
*  Version: 1.0.0  
*  Date: October 31, 2018
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""

"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
DICT_7X7_1000	 
DICT_ARUCO_ORIGINAL

Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
Reference: https://docs.opencv.org/3.4.2/d9/d6a/group__aruco.html#gaf5d7e909fe8ff2ad2108e354669ecd17
"""

import numpy as np
import cv2
import cv2.aruco as aruco
import aruco_lib
import argparse
import csv
csvlist=[]
def csvfile(filename,ldata):
    with open(filename, "a") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(ldata)
    writeFile.close()

def centroid(contours):
	listc=[]
	m=[]
	for cnt in contours:
		m=cv2.moments(cnt)
		cx=int(m['m10']/m['m00'])
		cy=int(m['m01']/m['m00'])
		listc.append((cx,cy))
	return listc

def aruco_detect(path_to_image):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''
    img = cv2.imread(path_to_image)     #give the name of the image with the complete path
    id_aruco_trace = 0
    det_aruco_list = {}
    det_aruco_list = aruco_lib.detect_Aruco(img)
    
    if det_aruco_list:
	    img = aruco_lib.mark_Aruco(img,det_aruco_list)
	    id_aruco_trace = aruco_lib.calculate_Robot_State(img[0],det_aruco_list)
	    print(id_aruco_trace)        
	    cv2.imshow('image',img[0])
	    cv2.waitKey(0)
    csvlist.append("ArUco"+path_to_image[-5]+".jpg")
    csvlist.append(img[1])
    img8=color_detect(img[0])
    cv2.imwrite("../Images/ArUco"+path_to_image[-5]+".jpg",img8)
    #csvfile("Output.csv",['Image name','ArUco ID','(x,y)Object-1','(x,y)Object-2'])
    csvfile("../2535_Task1.2.csv",csvlist)

    cv2.destroyAllWindows()

def color_detect(img):
    org=img
    dup = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    '''
    Defining HSV Values Here
    '''
    lower_red =  np.array([110,50,50],dtype = "uint8")
    upper_red = np.array([130,255,255],dtype = "uint8")

    lower_green=np.array([33,80,40],dtype = "uint8")
    upper_green=np.array([102,255,220],dtype = "uint8")
    
    lower_blue=np.array([2,100,180],dtype="uint8")
    upper_blue=np.array([255,190,220],dtype="uint8")
    '''
    code to be taken as 3 cases for recognizing a color in each case
	  two cases to be taken at a time, with the third case commented
    '''
    '''
    1. recognising red objects
    '''
    mask1 = cv2.inRange(dup, lower_red, upper_red)
    ret,thresh1 = cv2.threshold(mask1,127,255,1)
    im, contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt1=[]
    for cnt in contours1:
        approx1= cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if((cv2.contourArea(cnt)>1000 and cv2.contourArea(cnt)<300000) and len(approx1)==4):# length of 3 indicates triangle,4 for square
            
            cnt1.append(cnt)
    cv2.drawContours(img, cnt1,-1, (0,255,0), 25)
    l1=centroid(cnt1)
    cv2.putText(img,str(l1[0]),l1[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    if(l1):
       csvlist.append(l1[0])
    else:
       csvlist.append("None") 

    '''
    2. recognising green objects
    '''

    mask2 = cv2.inRange(dup, lower_green, upper_green)  
    ret,thresh2 = cv2.threshold(mask2,127,255,1)
    im, contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt2=[]
    for cnt in contours2:
        approx2= cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if((cv2.contourArea(cnt)>1000 and cv2.contourArea(cnt)<300000) and len(approx2)==3):# length of 3 indicates triangle,4 for square
            cnt2.append(cnt)
    cv2.drawContours(img, cnt2,-1, (255,0,0), 25)
    l2=centroid(cnt2)
    cv2.putText(img,str(l2[0]),l2[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0)) 
    if(l2):
        csvlist.append(l2[0])
    else:
        csvlist.append("None") 

    '''
    3. recognising blue objects
    '''


    mask3 = cv2.inRange(dup, lower_blue, upper_blue)    
    ret,thresh3 = cv2.threshold(mask3,100,255,1)
    im, contours3, hierarchy = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt3=[]
    for cnt in contours3:
        approx3= cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if((cv2.contourArea(cnt)>1000 and cv2.contourArea(cnt)<300000) and len(approx3)>=10):
            cnt3.append(cnt)
    cv2.drawContours(img, cnt3,-1, (0,0,255), 25)
    l2=centroid(cnt3)
    cv2.putText(img,str(l2[0]),l2[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0)) 
    if(l2):
        csvlist.append(l2[0])
    else:
        csvlist.append("None") 

    
    cv2.imshow("fra",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img



if __name__ == "__main__":    
    path_to_image=input("Path to image")
    aruco_detect(path_to_image)
    

