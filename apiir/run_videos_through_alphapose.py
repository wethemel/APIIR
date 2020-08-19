import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('-a', '--alphapose', default='/home/marcus/Programfiler/AlphaPose', help='path to alphapose module')
ap.add_argument('-i', '--input', required=True, help='path to input directory of videos')
ap.add_argument('-o', '--output', required=True, help='path to output directory')
ap.add_argument('-e', '--exclude_annotated', action='store_true', help='exclude files that has already been annotated. Recognized by AlphaPose_')
args = vars(ap.parse_args())

files = os.listdir(args['input'])

if args['exclude_annotated']:
    annot_files = os.listdir(args['output'])
    files = [f for f in files if str('AlphaPose_' + f) not in annot_files]
  
run_alphapose = str('python ' + args['alphapose'] + '/scripts/demo_inference.py' 
' --cfg pretrained_models/256x192_res152_lr1e-3_1x-duc.yaml'
' --checkpoint pretrained_models/fast_421_res152_256x192.pth'
' --video {input_video}' 
' --outdir {outdir}' 
' --save_video' 
' --detbatch 1' 
' --posebatch 30'
)

for f in files:
    print('\n[INFO] running file: {} through alphapose...'.format(f))
    filePath = str(args['input'] + '/' + f)
    os.system(run_alphapose.format(input_video=filePath, outdir=args['output']))




