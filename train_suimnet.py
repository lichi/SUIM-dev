"""
# Training pipeline of the SUIM-Net
# Paper: https://arxiv.org/pdf/2004.01241.pdf  
"""
from __future__ import print_function, division
import os
import math
from os.path import join, exists
from keras import callbacks
# local libs
from models.suim_net import SUIM_Net
from utils.data_utils import trainDataGenerator
import matplotlib.pyplot as plt
import numpy as np

HOME_COLAB_REPO='/content/SUIM-dev'
HOME_COLAB_TRAIN_DATA='/content/DATA'

DATASET             = 'DataSet_ConchasAbanico' #['SUIM', 'DataSet_ConchasAbanico']
HOME_COLAB_DRIVE    = '/content/drive/MyDrive/DATA/{}'.format(DATASET)
HOME_LOCAL_WINDOWS  = 'E:/DATASETS_LOCAL/'
HOME_TO_USE         = HOME_COLAB_DRIVE


def train_plot_debug(train_gen):
  for bi in range(5):
    fig, ax = plt.subplots(nrows=1, ncols=n_classes+1, figsize=(15,15))
    data = next(train_gen)
    image = data[0] #(1, 256, 320, 3)
    masks = data[1] #(1, 256, 320, 5)
    image = np.squeeze(image[0])
    ax[0].imshow(image)
    ax[0].axis('off')
    for i in range(1, n_classes+1):
      # mask_max = np.argmax(data[1][i], axis=2)
      mask_i = masks[:,:,:,i-1]
      print('mask_i: ', mask_i.shape)
      # changing size from (1, 200, 200, 3) to (200, 200, 3) for plotting the image
      mask_i = np.squeeze(mask_i)
      ax[i].imshow(mask_i)
      ax[i].axis('off')
    plt.show()

## dataset directory
# dataset_name = "suim"
# train_dir = os.path.join(HOME_COLAB, "/mnt/data1/ImageSeg/suim/train_val/")
train_dir = os.path.join(HOME_COLAB_TRAIN_DATA, DATASET, "train_val/")
# train_dir = os.path.join(HOME_COLAB_DATA, "DataSet_ConchaAbanico/train_val/")

## ckpt directory
ckpt_dir = os.path.join(HOME_TO_USE, "ckpt/")
base_ = 'VGG' # or 'RSB'
if base_=='RSB':
    im_res_ = (320, 240, 3) 
    ckpt_name = "suimnet_rsb.hdf5"
else: 
    im_res_ = (320, 256, 3)
    ckpt_name = "suimnet_vgg.hdf5"
model_ckpt_name = join(ckpt_dir, ckpt_name)
if not exists(ckpt_dir): os.makedirs(ckpt_dir)

## initialize model
n_classes = 5
suimnet = SUIM_Net(base=base_, im_res=im_res_, n_classes=n_classes)
model = suimnet.model
# print (model.summary())
## load saved model
# model.load_weights(os.path.join(HOME_TO_USE, "ckpt/saved/", "suimnet_vgg.hdf5"))

batch_size = 8
# batch_size = 1
num_epochs = 100 #50
# setup data generator
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')

model_checkpoint = callbacks.ModelCheckpoint(model_ckpt_name, 
                                   monitor = 'loss', 
                                   verbose = 1, mode= 'auto',
                                   save_weights_only = True,
                                   save_best_only = True)

# data generator
train_gen = trainDataGenerator(batch_size, # batch_size 
                              train_dir,# train-data dir
                              "images", # image_folder 
                              "masks", # mask_folder
                              data_gen_args, # aug_dict
                              image_color_mode="rgb", 
                              mask_color_mode="rgb",
                              target_size = (im_res_[1], im_res_[0]))
test_sample = next(train_gen)
print('image: ', test_sample[0].shape)
print('mask: ', test_sample[1].shape)

# train_plot_debug(train_gen)

# fit model
model.fit(train_gen, 
                    steps_per_epoch = 18, #5000
                    epochs = num_epochs,
                    callbacks = [model_checkpoint])

