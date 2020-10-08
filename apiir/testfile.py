import alphapose_tools.alphapose_results_importer as ari



test2 = ari.json_interface('10frames_test.json')

test2.COCO_load_to_dict()

frame1 = test2.GetFrames()[1]
print(frame1.Keypoints()['LKnee'], frame1.FrameID())