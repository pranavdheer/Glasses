import tensorflow as tf
import tensorflow.contrib.slim as slim
import os
import vgg
import copy

import numpy as np
import misc.utils as utils

from misc.ShowTellModel import ShowTellModel
from misc.AttentionModel import AttentionModel
from misc.ShowAttendTellModel import ShowAttendTellModel

def setup(opt):
    
    # check compatibility if training is continued from previously saved model
    if vars(opt).get('start_from', None) is not None:
        # check if all necessary files exist 
        assert os.path.isdir(opt.start_from)," %s must be a a path" % opt.start_from
        assert os.path.isfile(os.path.join(opt.start_from,"infos_"+opt.id+".pkl")),"infos.pkl file does not exist in path %s"%opt.start_from
        ckpt = tf.train.get_checkpoint_state(opt.start_from)
        assert ckpt,"No checkpoint found"
        assert ckpt.model_checkpoint_path,"No model path found in checkpoint"
        opt.ckpt = ckpt
    if opt.caption_model == 'show_tell':
        return ShowTellModel(opt)
    elif opt.caption_model == 'attention':
        return AttentionModel(opt)
    elif opt.caption_model == 'show_attend_tell':
        return ShowAttendTellModel(opt)
    else:
        raise Exception("Caption model not supported: {}".format(opt.caption_model))
