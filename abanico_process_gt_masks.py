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
CA_dir = masks_process_dir + "CA/"
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

n_classes=5

from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
#Define a function to perform additional preprocessing after datagen.
#For example, scale images, convert masks to categorical, etc. 
def preprocess_data(mask, num_class):
    #Scale images
    # img = img / 255. #This can be done in ImageDataGenerator but showing it outside as an example
    #Convert mask to one-hot
    labelencoder = LabelEncoder()
    h, w, c = mask.shape  
    mask = mask.reshape(-1,1)
    mask = labelencoder.fit_transform(mask)
    mask = mask.reshape(h, w, c)
    mask = to_categorical(mask, num_class)
      
    return mask

im_h, im_w = 240, 320
mask_paths = getPaths(HOME_TO_USE, masks_dir)
print(len(mask_paths))
import matplotlib.pyplot as plt
for i,p in enumerate(mask_paths):
    # read and scale inputs
    img = Image.open(p).resize((im_w, im_h)).convert('RGB')
    img = np.array(img)
    imgplot = plt.imshow(img)
    print('img {}, {}'.format(i, img.shape))
    # img = np.array(img)/255.
    # img = np.expand_dims(img, axis=0)
    # if i==1: break
    plt.show()

    mask = preprocess_data(img,5)
    print('mask: ', mask.shape)
