import alphapose_tools.alphapose_results_importer as ari
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


jump = ari.json_interface('/home/marcus/Documents/APIIR/Eksempel/Eksempel_AILab/Output/Person1_dataset.json')
jump.COCO_load_to_dict()


KneePosX = []
KneePosY = []
for frame in jump.GetFrames():
    KneePosX.append(frame.Keypoint("LKnee")['x']-5)
    KneePosY.append(frame.Keypoint("LKnee")['y']-5)

# print(len(KneePosX))

plt.style.use('ggplot')
plt.figure()
plt.plot(KneePosX, KneePosY, 'rd')
# plt.plot(KneePosY)
# plt.show()

KneePosX = savgol_filter(np.array(KneePosX), 101, 2)
KneePosY = savgol_filter(np.array(KneePosY), 101, 2)
plt.plot(KneePosX, KneePosY, 'bd')

jump.LookForError('LKnee', errorWindow=2)
KneePosX = []
KneePosY = []
for frame in jump.GetFrames():
    KneePosX.append(frame.Keypoint("LKnee")['x']+5)
    KneePosY.append(frame.Keypoint("LKnee")['y']+5)

# plt.style.use('ggplot')
# plt.figure()
plt.plot(KneePosX, KneePosY, 'gd')
# plt.plot(KneePosY)
plt.show()

