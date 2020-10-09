import json
import numpy as np

class json_interface:
    def __init__(self, fileName):
        self.frames = []
        # self.json_data = None
        self.data = None
        try:
            with open(fileName) as json_results:
                self.data = json.load(json_results)
        except:
            print('Cannot load from file')

    def GetFrames(self):
        return self.frames
            
    def COCO_load_to_dict(self):
        # print(self.data)
        for frame_data in self.data:
            # print(frame_data)
            COCOframe = COCO_frame(frame_data) #creating a object from COCO_frame
            COCOframe.load_to_dict()
            self.frames.append(COCOframe)


    def LookForAllErrors(self):
        for key in self.GetFrames()[0].GetKeys():
            self.LookForError(key)
            # for frame in self.GetFrames():
            #     frame.LookForError(key)
    # a function that goes through a joint, and look for abnormalities (sudden changes) and sets theese to the average change. 
    # Setting max deviation per frame to 10%
    def LookForError(self, joint, errorWindow=3):
        # print(joint)
        for i in  range(errorWindow, len(self.GetFrames()) -errorWindow):
            
            dataInFocus_x = np.array([frame.Keypoint(joint)['x'] for frame in self.GetFrames()[i-errorWindow : i+errorWindow]])
            dataInFocus_y = np.array([frame.Keypoint(joint)['y']  for frame in self.GetFrames()[i-errorWindow : i+errorWindow]])
            # print(i, dataInFocus_x, dataInFocus_y)
            avrg_x = np.average(dataInFocus_x)
            avrg_y = np.average(dataInFocus_y)
            # print(avrg_y)

            if self.GetFrames()[i].Keypoint(joint)['x'] > 1.04* abs(avrg_x):
                print(i)
                newVal = ((self.GetFrames()[i-2].Keypoint(joint)['x'] + self.GetFrames()[i+2].Keypoint(joint)['x']) / 2)
                self.GetFrames()[i].setNewVal(joint, 'x', avrg_x)
            
            if self.GetFrames()[i].Keypoint(joint)['y'] > 1.1* abs(avrg_y):
                print(i)
                newVal = ((self.GetFrames()[i-2].Keypoint(joint)['y'] + self.GetFrames()[i+2].Keypoint(joint)['y']) / 2)
                self.GetFrames()[i].setNewVal(joint, 'y', avrg_y)
            



# Handling information for each single frame 
class COCO_frame:

    def __init__(self, frame):
        self.frame = frame
        self.frame_ID = int(frame['image_id'].split('.')[0])
        self.COCO_dict = { # In given order by COCO
        "Nose":None,
        "LEye":None,
        "REye":None,
        "LEar":None,
        "REar":None,
        "LShoulder":None,
        "RShoulder":None,
        "LElbow":None,
        "RElbow":None,
        "LWrist":None,
        "RWrist":None,
        "LHip":None,
        "RHip":None,
        "LKnee":None,
        "Rknee":None,
        "LAnkle":None,
        "RAnkle":None,
    }

    def load_to_dict(self):
        # print(self.frame)
        keypoints = self.frame['keypoints']
        for (i,key) in enumerate(self.COCO_dict.keys()):
            pos = i*3 #The position increments by three*i. Eks set 3 starts at 9
            self.COCO_dict[str(key)] = {'x' : keypoints[pos], 'y' : keypoints[pos+1]} #Settting x and y value of the joint

    def Keypoints(self):
        return self.COCO_dict
    def Keypoint(self, Keypoint):
        return self.COCO_dict[Keypoint]
    def GetKeys(self):
        return self.COCO_dict.keys()
    def FrameID(self):
        return self.frame_ID
    
    def setNewVal(self, joint, axis, newVal):
        self.COCO_dict[joint][axis] = newVal




    
