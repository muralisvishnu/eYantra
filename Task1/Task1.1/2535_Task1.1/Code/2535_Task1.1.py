# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.1
*  Filename: Task1.1.py
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
"""

import numpy
import cv2
import cv2.aruco as aruco
def aruco_gen(id_aruco, num_pixels):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)  #replace n with no. of bits per pixel and C with the no. of combinations
                                                                #select n and C from the list mentioned above

    img = cv2.cvtColor(aruco.drawMarker(aruco_dict, id_aruco, num_pixels),cv2.COLOR_GRAY2RGB)
    img_border=cv2.copyMakeBorder(img,25,25,25,25,cv2.BORDER_CONSTANT,value=[255,255,255])
    text="ArUco ID = "+str(id_aruco)
    textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
    textX = int((img.shape[1] - textsize[0]) / 2)
    textY = int(( textsize[1]+12) / 2)
    cv2.putText(img_border,text, (textX,textY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255)) 
    path=""
    cv2.imwrite(path+("ArUco"+str(id_aruco)+".jpg"),img_border)
    path="../Images/"
    cv2.imwrite(path+("ArUco"+str(id_aruco)+".jpg"),img_border)
    cv2.imshow('frame',img_border)
    cv2.waitKey(0)
    '''
        code here for saving the Aruco image as a "jpg" by following the steps below:
        1. save the image as a colour RGB image in OpenCV color image format
        2. embed a boundary of 25 pixels on all four sides and three channels of the image
        3. save the image as "ArUcoID.jpg" where ID is the digits of id_aruco i.e. if the ID is 26 the name should be: ArUco26.jpg
        4. APIs which are permitted to be used are:
        a. cvtColor
        b. imwrite
        and other OpenCV APIs.
        5. You are permitted to modify n, C and variables id_aruco and num_pixels
    '''

    cv2.destroyAllWindows()


if __name__ == "__main__":
    id_aruco=int(input())
    num_pixels=400
    aruco_gen(id_aruco, num_pixels)
