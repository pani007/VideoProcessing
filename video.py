# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:20:54 2021

@author: panindra
"""
import cv2
import numpy as np




cap =  cv2.VideoCapture('../Desktop/eyantra/Set 10/Task 1B_Update/Video.mp4')

### Lists the properties of the video

### This prints all the properties of the frames present in the video

## We also print the shape of the current frame.



def countFrames(videoObj):
    frames = 0
    while(videoObj.isOpened()):
        ret, frame = videoObj.read();
        if ret == True:
            frames +=1
            # Lets print the current frame array
            print("Current Frame",frame)
            #Printing the shape of the current frame
            print("\n The shape of this frame is: ", frame.shape)
            cv2.imshow('frame',frame)
            #break
            ### Showing the frame 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else: 
            break
            
    
    # The number of frames in the video
    print("The number of frames are: ",frames)
    





    
def getContourProperties(cnt):
    M = cv2.moments(cnt)
    return M







    
## detect shape funtion

# it gives the shape of the object and returns the shape of the object present in an image
def detectShapes(cnt):
   
    #print("current no of contours are ", len(contours))
    
    
    area = cv2.contourArea(cnt)
    print("Area   ", area)
    epsilon = 0.01*cv2.arcLength(cnt,True)
    sides = cv2.approxPolyDP(cnt,epsilon,True)
    print(len(sides))
    
    if area < 80000:
        if len(sides) == 3:
            shapes ='Triangle'
        elif len(sides) == 4:
            shapes = "Quadrilateral"
        
        elif len(sides) == 5:
            shapes = "Pentagon"
                
        elif len(sides) == 6:
            shapes = "Hexagon"
                
        elif len(sides)>=15:
            shapes = "Circle"
                
        else:
            shapes = "undefined"
    return shapes               
    
                

## detect color
def detectColor(frame,cnt):
    x,y,w,h = cv2.boundingRect(cnt)
    print("The mean colour matrix is is " ,cv2.mean(frame[y:y+h,x:x+w]))
    bounding_rect = cv2.mean(frame[y:y+h,x:x+w])
    #cv2.imshow("img",frame[y:y+h,x:x+w])
    return "Blue" if max(bounding_rect) == bounding_rect[0] else 'Green' if max(bounding_rect) == bounding_rect[1] else 'Red'
  


### Finalize the shape and color:
def getContourShapeAndColor(frame,cnt):
    
    shape = detectShapes(cnt)
    color = detectColor(frame,cnt)
    return color +" - " + shape 


#This function draws the contours in figure
# It gives the colour and shapes of the figures present in the video
## We finally save the video of object detection with color and shape
def drawContursAndGiveResult(videoObj):
    
    ## Instanciatig video object 
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1280, 720))

    ### Video is a collection of frames
    ## For video processing we have to create frame images
    while(videoObj.isOpened()):
        ret, frame = videoObj.read();
        if ret == True:
          
            # Lets print the current frame array
            imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(imgray,127,255,0)
            contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            
            
            
            f = cv2.drawContours(frame,contours,-1,(0,200,200),3)
                
            #cv2.imshow("frame",f)
            #print("The current contour shape is ----------\n \n \n",np.array(contours))
            
            
            current_shapes = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area <80000:
                    
                    M = getContourProperties(cnt)
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    
                    res = getContourShapeAndColor(f,cnt)
                    print('ctx === ',cx,cy,res)
                    f = cv2.putText(f, res, (cx-30,cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
                    cv2.imshow("frame",f)
                    
                    ### Saving the shape detected video
                    
                    current_shapes.append(res)
            out.write(f)
            print(current_shapes)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else: 
            break
        print(frame.shape)
    
    cap.release()
    cv2.destroyAllWindows()
    
    
## calling the above function    
#countFrames(cap)
drawContursAndGiveResult(cap)



