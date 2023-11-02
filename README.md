# Virtual Assistance For Blind People
>## Open Projects 2023
## Abstract
Blind people often need assistance while walking and doing day-to-day tasks. It's not possible for them to gain human assistance throughout the day. This recurring issue is being addressed in this project.
Our goal is to make a headwear with a camera that will scan the surroundings and tell the blind person about the objects, people, roads, and many more things which come ahead of him/her through audio jacks attached to that eyewear.
## Motivation
Blind individuals face significant challenges in navigating their surroundings, identifying objects, and recognizing people. This can lead to a feeling of isolation and limited independence. This technology has the potential to transform the lives of blind individuals, providing them with increased independence, safety, and confidence. Our goal is to create a product that is not only practical and effective, but also affordable and accessible to all blind individuals. The designed device is lightweight and modularised with mechanical aspects powered by a Raspberry Pi, which is responsible for controlling the camera, processing the data, sending button inputs and audio output to the earphones.
## Workflow
Depth sensing is the process of capturing depth information from the surrounding environment using depth sensors such as LiDAR, stereo cameras, or structured light sensors. This data is then processed using algorithms such as stereo matching, depth estimation, or point cloud segmentation to create a 3D representation of the scene.


However, when using a RGB camera to measure distance, it can be challenging to accurately determine an object's depth without using sensors. To solve this problem, we can use the object's width in front of the camera. We use the concept of plane angle to calculate the object's depth from the camera. The following steps are involved:



1.  **Calibration:** For each object in the data set, we determine the product of the distance and width of the object from the camera.
2.  **Measurement of Width:** We identify two extreme points on the object and use the distance between them to determine the object's width.
3.  **Calculation of Depth:** The original width of the object remains constant, but as the distance increases, the observed width decreases.

The relationship between the depth (d) and width (w) follows a rectangular hyperbola,
 `d x w = constant.`

This constant value depends on various factors such as the object type and is determined during the calibration step. We can calculate the depth using the equation

    d1 = (c x d) / c1,

where c is the constant value determined during calibration.

Note that this depth measurement method only applies to objects in the daytime and in horizontal sight views (where the angle between the vertical and the camera's sight is 90 degrees). For other angles of view, we can use the MPU 9650 to measure the angle and calibrate the data set accordingly.

![enter image description here](https://i.postimg.cc/YSCcdcDk/workflow.jpg)
## Mechanical Aspects of design
The project involves creating a 3D model prototype using SolidWorks and 3D printing it using UltiMaker Cura. This prototype serves as the base for the hardware setup and includes a Raspberry Pi incorporated with a Pi Cam, power source and audio aids.


![enter image description here](https://i.postimg.cc/L4CYdLGq/photo-2023-03-29-23-46-18.jpg)

![photo-2023-03-29-23-46-21.jpg](https://i.postimg.cc/7ZNKDB41/photo-2023-03-29-23-46-21.jpg)
## Software Aspects of design
The major tech stack for this project is built on the programming language Python for implementing object identification, depth vision sensing and text-speech interconversion through the OpenCV library.The process includes the following:

**1. Image Classification:**

 -   Based on salient features, classify the image to which category it belongs to
 -  Deep learning algorithm ‘Mobile Net’ is used

**2. Object Detection:**

 -   Based on salient features specifies the location of multiple objects in the image
 -   The famous ‘SSD-MobileNetv3’ algorithm is used
 -   The famous ‘Coco’ dataset containing 80 classes is used which is mainly built for objects that can be viewed on roadways

**3. Depth Sensing:**

 -   The property that depth depends on the observed width of the object detected is used
 -   For each class, a multiplying factor is computed in order to calibrate the model

**4. Text to Speech Conversion:**
 -   The python library pyttsx3 is used to convert text to speech
 -   The library gives us the benefit of choosing type of voice and rate of speech
## Simulation
[![Screenshot-2023-03-06-150014.png](https://i.postimg.cc/BbwYk8r9/Screenshot-2023-03-06-150014.png)](https://postimg.cc/vxft6m83)
  ![enter image description here](https://i.postimg.cc/63fJ59mk/photo-2023-03-29-23-45-24.jpg)
  ![enter image description here](https://i.postimg.cc/Y9DN0VDg/photo-2023-03-29-23-45-36.jpg)
  ![enter image description here](https://i.postimg.cc/bY5LSXfW/photo-2023-03-29-23-45-31.jpg) 
## Prerequisites and Installation
- Clone/Download the Repository and go to src/ directory
- Install the necessary dependencies by using the following command:<br>
  ```bash
  >>> pip install cvzone mediapipe matplotlib pyttsx3 keyboard
  ```
- Run the `main.py`
    ```bash
    >>> python main.py
    ```
- Objects detected will be visible marked and the audio output can be listened by any keyboard input (in our case was an earbud tap)
## Cost Structure
|Components| Cost ( in INR) |
|--|--|
| Raspberry Pi 4 |15,000 |
| Memory Card|380 |
| Night Vision Camera|1,000 |
| Speaker (Earbuds)|1,800 |
| Ultrasonic sensors|550 |
|Jumpers|180 |
| USB Cables|500 |
| 3D Printing|2,500|
| Power Bank|1,200|
| Display Screen|250 |
| **Total**|**23,360** |
## Applications
 -   Currently available solutions such as canes, guide dogs, and audio prompts have their limitations and are not always accessible or practical. Our device becomes handy in such scenarios.
 -   Real time dynamic video capture and processing gives real time updates to the person(when prompted) about the distance to different objects 
 -   By minimal use of sensors, or hardware the system not only helps the blind people avoid any obstacle it also helps them recognize the necessary warning sign boards and act accordingly.
## Results
 -   A headwear holding a camera and audio aids connected a processor was developed
 -   The functioning starts as the visually challenged person presses the button on the ear-pods indicating his requirement for the distance input
 -   The processing runs over the processor and the closest object distance is identified by the software
 -   The object name along with its distance is relayed; if no object is present within the vision proximity, ‘Nothing close enough’ is conveyed
 -   The object detection and distance observed is found to be quite accurate to the actual value, signifying a robust and efficient algorithm

![enter image description here](https://i.postimg.cc/sxQPS2SJ/New-Project.png)
![OK](https://i.postimg.cc/Y2RwcYPV/New-Project-1.png)
## Limitations
 -   Currently the model functions upon roadside objects with limited object entries.    
 -   The device doesn’t function properly under dim light conditions.
 -   Currently the device weight doesn’t match with the safe limit to handle the weight over the skull.  
 -   The depth measurement functions with only horizontal sight views(when the angle between the vertical and the camera's sight is 90 degrees).
## Future Advancements
 -   Generation of an automated warning audio output in case of emergency conditions like sudden appearance of an object in front of camera.
 -   Replacing the switch button with an audio input if the user wishes to ask for the distance of a certain object.
 -   Integrating the support for night vision camera for the device to function properly under dim light conditions.
 -   Enhancing the support for detection of zebra crossings, and helping visually challenged people cross roads via zebra crossings with fine tuning .
 -   Redesigning of the model with more compact size and lesser weight keeping in mind the mechanical aspects such as heat cooling control over the skull of the person.
## Team Members
1. [Anjali Bhattad](https://github.com/abhattad53)
 2. [Divyansh Kothari](https://github.com/deev1010)
 3. [Gaurav](https://github.com/gaurav0github)
 4. [Hardik Sahnni](https://github.com/hsahnisr07)
 5. [Himanshi Lalwani](https://github.com/Himanshilalwani175)
 6. [Shubham Barahate](https://github.com/ShubhamBarahate)
 7. [Tanish Pathak](https://github.com/pathakiitr)
 8. [Taniya Tarannum](https://github.com/taniya-04)
 9. [Vasu Kashiv](https://github.com/VasuKashiv)
## Mentors
1. [Nagesh Bansal](https://github.com/Nageshbansal)
2. [Apurba Prasad Padhy](https://github.com/apurba-pp)
## References

 - [OpenCV](https://towardsdatascience.com/yolo-object-detection-with-opencv-and-python-21e50ac599e9)
 - [Text to Speech](https://www.thepythoncode.com/article/convert-text-to-speech-in-python)
