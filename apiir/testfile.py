import alphapose_tools.alphapose_results_importer as ari
# test = ari.json_interface('10frames_test.json')
test2 = ari.json_interface('10frames_test.json')
# test3 = ari.json_interface("APIIR\apiir\alphapose_tools\10frames_test.json")

test2.COCO_load_to_dict()
frame1 = test2.GetFrames()[1]
print(frame1.Keypoints(), frame1.FrameID())