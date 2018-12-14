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

def aruco_detect(path_to_image):
    corners = []
    #comb = {50:0,100:1,250:2,1000:3}
    #num = (n-4)*4 + comb[c]
    img = cv2.imread(path_to_image)
    id_aruco_trace = 0
    arlist = aruco_lib.detect_Aruco(img)
    if arlist:
        img = aruco_lib.mark_Aruco(img,arlist)
        id_aruco_trace = aruco_lib.calculate_Robot_State(img,arlist)
        #cv2.imshow('k',img)
        #print(id_aruco_trace)
    org=cv2.imread(path_to_image)
    dup = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    lower_red =  np.array([110,50,50])
    upper_red = np.array([130,255,255])
    lower_green=np.array([33,80,40])
    upper_green=np.array([102,255,255])
    lower_blue=np.array([86,31,4])
    upper_blue=np.array([255,255,255])
    mask1 = cv2.inRange(dup, lower_red, upper_red)
    ret,thresh1 = cv2.threshold(mask1,127,255,1)
    im, contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    approx1= cv2.approxPolyDP(contours1[1],0.01*cv2.arcLength(contours1[1],True),True)
    if(len(approx1)==4):
        cv2.drawContours(img, contours1, 1, (0, 255, 0), 25)
    
    mask2 = cv2.inRange(dup, lower_green, upper_green)  
    ret,thresh2 = cv2.threshold(mask2,127,255,1)
    im, contours2, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    approx2= cv2.approxPolyDP(contours2[1],0.01*cv2.arcLength(contours2[1],True),True)
    if(len(approx2==3)):
        cv2.drawContours(img, contours2, 1, (255,0, 0), 25) 
    # mask3 = cv2.inRange(dup, lower_blue, upper_blue)    
    # ret,thresh3 = cv2.threshold(mask3,127,255,1)
    # cv2.imshow("fr",mask3)
    # cv2.waitKey(0)
    # im, contours3, hierarchy = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours3, 1, (0, 0,255), 25)
   # for cnt in contours1:
    #    print(contours1)
    
    # print(len(approx))
    #  #   cv2.drawContours(img,[cnt],0,255,25)
    # if len(approx)==3:
    #     print("triangle")
    #     #cv2.drawContours(img,[cnt],0,(0,255,0),25)
    # elif len(approx)==4:
    #     print("square")
    #     #cv2.drawContours(img,[cnt],0,(0,0,255),25)
    # elif len(approx) > 15:
    #     print("circle")
        #cv2.drawContours(img,[cnt],0,(0,255,255),25)


    
	#res = cv2.bitwise_or(mask1,mask2)
	#print(contours)
    
    # cv2.imshow("fra",img)
    # ret1,thresh1 = cv2.threshold(mask2,127,255,1)
    # im, contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours1, 1, (0, 0, 255), 25)
    cv2.imshow("fr",img)
    #cv2.imshow('k',mask1)
    #image3, contours, hierarchy = cv2.findContours(res,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #don't know why simple is not working only none seems to work and it does not deliver
    #the borders of the image have to be sharp, i'm seriously missing something
    #as i am not able to use the chain approx simple function to get the corners, i am also not able to calculate the values of the centroid
    #mask1 = cv2.cvtColor(mask1,cv2.COLOR_GRAY2RGB)
    #print(contours)
    #print(contours[2])
    '''
    for j in range(len(contours)):
        for i in contours[j]:
            cv2.circle(image,tuple(i[0]),1,(0,0,255),6)
    #cv2.imshow('final',image3)
    ''
    img = cv2.drawContours(img, contours[1], -1, (255,0,0), 25,cv2.LINE_AA)
    img = cv2.drawContours(img, contours[2], -1, (0,255,0), 25, cv2.LINE_AA)
    '''
    corners = cv2.goodFeaturesToTrack(mask1,5,0.01,10)
    mask1 = cv2.cvtColor(mask1,cv2.COLOR_GRAY2RGB)
    print(tuple(corners[1][0]))
    for j in range(len(corners)):
            cv2.circle(mask1,tuple(corners[j][0]),1,(0,0,255),6)
    #cv2.imshow('final',image3)
    #cv2.imshow('final.jpg',res)
    print(corners)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":    
    aruco_detect('C:/Users/Vishnu S Murali/Documents/eyantraAssignments/Task1/Task1.2/Task1.2/3. Images/Image1.jpg')

