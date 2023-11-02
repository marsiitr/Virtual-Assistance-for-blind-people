import cv2
import matplotlib.pyplot as plt
import pyttsx3
import keyboard
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
config_file='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model='frozen_inference_graph.pb'
model=cv2.dnn_DetectionModel(frozen_model,config_file)
classLabels=[]
file_name='Labels.txt'
with open(file_name,'rt') as fpt:
    classLabels=fpt.read().rstrip('\n').split('\n')
file_name='factors.txt'
with open(file_name,'rt') as fpt:
    Mfactors=fpt.read().rstrip('\n').split('\n')
model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)
cap=cv2.VideoCapture(0)
font_scale=1
font=cv2.FONT_HERSHEY_SIMPLEX
s='Nothing enough close'
def on_press(event):
    print(event.name)
    engine.say(s)
    engine.runAndWait()
keyboard.on_press(on_press)
while True:
    ans=[1000,'Nothing close enough']
    ret,frame=cap.read()
    ClassIndex,confidece,bbox=model.detect(frame,confThreshold=0.55)
    if(len(ClassIndex)!=0):
        for ClassInd,conf,boxes in zip(ClassIndex.flatten(),confidece.flatten(),bbox):
            if(ClassInd<=80):
                cv2.rectangle(frame,boxes,(255,255,0),2)
                depth=int(int(Mfactors[ClassInd-1])/boxes[2])
                if ans[0]>depth:
                    ans[0]=depth
                    ans[1]=classLabels[ClassInd-1]
                s=classLabels[ClassInd-1]+": "+str(depth)
                cv2.putText(frame,s,(boxes[0]+10,boxes[1]+40),font,fontScale=font_scale,color=(255,0,255),thickness=3)
    cv2.imshow('Object Detection',frame)
    if ans[0]==1000:
        s=ans[1]
    else:
        s='TThere is a '+ans[1]+' at '+str(ans[0])+'centimeters'
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()