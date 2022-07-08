import os
import numpy as np
from PIL import Image
from os.path import join, exists
from utils.data_utils import getPaths

DATASET                 = 'DataSet_ConchasAbanico' #['SUIM', 'DataSet_ConchasAbanico']
HOME_COLAB_DRIVE        = '/content/drive/MyDrive/DATA/{}'.format(DATASET)
HOME_LOCAL              = ''
HOME_LOCAL_DATASET_WIN  = 'E:/DATASETS_LOCAL/{}'.format(DATASET)
HOME_TO_USE             = HOME_LOCAL_DATASET_WIN

masks_dir = os.path.join(HOME_TO_USE, "TEST/masks/")
masks_process_dir = os.path.join(HOME_TO_USE, "TEST/masks_process/" )
# CA: Concha de abanico
# VCA: Valva de concha de abanico (muerta)
# VPP: Valva de pico de pato
# CRC: Caracol
# CNG: Cangrejo
CA_dir  = masks_process_dir + "CA/"
VCA_dir = masks_process_dir + "VCA/"
VPP_dir = masks_process_dir + "VPP/"
CRC_dir = masks_process_dir + "CRC/"
CNG_dir = masks_process_dir + "CNG/" 
if not exists(masks_process_dir): os.makedirs(masks_process_dir)
if not exists(CA_dir): os.makedirs(CA_dir)
if not exists(VCA_dir): os.makedirs(VCA_dir)
if not exists(VPP_dir): os.makedirs(VPP_dir)
if not exists(CRC_dir): os.makedirs(CRC_dir)
if not exists(CNG_dir): os.makedirs(CNG_dir)

n_classes=6

from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
#Define a function to perform additional preprocessing after datagen.
#For example, scale images, convert masks to categorical, etc. 
def preprocess_data(mask, num_class):
    #Scale images
    # img = img / 255. #This can be done in ImageDataGenerator but showing it outside as an example
    #Convert mask to one-hot
    # labelencoder = LabelEncoder()
    # h, w = mask.shape  
    # mask = mask.reshape(-1,1)
    # mask = labelencoder.fit_transform(mask)
    # mask = mask.reshape(h, w)
    print("Unique values in the mask ...", np.unique(mask))
    mask = to_categorical(mask, num_class)
      
    return mask


mask_paths = getPaths(HOME_TO_USE, masks_dir)
print(len(mask_paths))

import matplotlib.pyplot as plt
import cv2
from utils.measure_utils import plot_debug

for i,p in enumerate(mask_paths):
    # read and scale inputs
    img = Image.open(p)
    # img = img.resize((im_w, im_h))
    # img = img.convert('RGB')
    img = np.array(img)
    # img = cv2.imread(p, 0)
    im_h, im_w = img.shape
    print("\nUnique values in the mask are: ", np.unique(img))
    print('img {}, {}'.format(i, img.shape))
    # img = np.array(img)/255.
    # img = np.expand_dims(img, axis=0)
    # if i==1: break
    # plt.show()

    mask = preprocess_data(img,n_classes)
    print("Unique values in the mask after endcoding are: ", np.unique(mask))
    print('mask: ', mask.shape)

    img_name = p.split('/')[-1][:-4]
    print('img_name: ', img_name)

    # imgplot = plt.imshow(mask[:,:,0])
    # fig, ax = plt.subplots(nrows=1, ncols=n_classes+1)
    # plt.title(img_name)
    # ax[0].imshow(mask[:,:,0])
    # ax[1].imshow(mask[:,:,1])
    # ax[2].imshow(mask[:,:,2])
    # ax[3].imshow(mask[:,:,3])
    # ax[4].imshow(mask[:,:,4])
    # ax[5].imshow(mask[:,:,5])
    # ax[6].imshow(img)
    # plt.show()

    CA  = np.reshape(mask[:,:,1], (im_h, im_w))
    VCA = np.reshape(mask[:,:,2], (im_h, im_w))
    VPP = np.reshape(mask[:,:,3], (im_h, im_w))
    CRC = np.reshape(mask[:,:,4], (im_h, im_w))
    CNG = np.reshape(mask[:,:,5], (im_h, im_w))
    Image.fromarray(np.uint8(CA*255.)).save (CA_dir +img_name + '.bmp')
    Image.fromarray(np.uint8(VCA*255.)).save(VCA_dir+img_name + '.bmp')
    Image.fromarray(np.uint8(VPP*255.)).save(VPP_dir+img_name + '.bmp')
    Image.fromarray(np.uint8(CRC*255.)).save(CRC_dir+img_name + '.bmp')
    Image.fromarray(np.uint8(CNG*255.)).save(CNG_dir+img_name + '.bmp')
