import json
# import numpy

class json_interface:
    def __init__(self, fileName):
        # self.json_data = None
        self.frames = []
        # with open(fileName) as json_results:
        #     self.data = json.load(json_results) # A list of dicts
    # def load_data(self):
        try:
            with open(fileName) as json_results:
                self.data = json.load(json_results)
        except:
            print('Cannot load from file')

    def GetFrames(self):
        return self.frames
            
    def COCO_load_to_dict(self):
        for frame_data in self.data:
            # print(frame_data)
            COCOframe = COCO_frame(frame_data) #creating a object from COCO_frame
            COCOframe.load_to_dict()
            self.frames.append(COCOframe)


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
    def FrameID(self):
        return self.frame_ID


    
