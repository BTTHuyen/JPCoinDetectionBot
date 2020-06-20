# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))

import darknet as dn
import pdb

dn.set_gpu(0)
net = dn.load_net("cfg/yolo-obj.cfg", "/data1/huyen/CoinBot/darknet/backup/yolo-obj_30000.weights", 0)

meta = dn.load_meta("cfg/obj.data")
r = dn.detect(net, meta, "userPicture.jpg")
