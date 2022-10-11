#!/bin/bash
pip install --upgrade --no-cache-dir gdown

cd /content/
echo "===> Creating folders..."
mkdir /content/DATA
mkdir /content/DATA/DataSet_ConchasAbanico

echo "===> Downloading ABANICO dataset"
id="1qJpTORrTuCETMWg3FBJeCaCrn8IVrBDh"

gdown --id $id
filename="train_val.rar"
src="/content/${filename}"
dst="/content/DATA/DataSet_ConchasAbanico"
mv $src ${dst}

echo "===> Unzipping ${filename}"
unrar x -Y "/content/DATA/DataSet_ConchasAbanico/${filename}" "/content/DATA/DataSet_ConchasAbanico"
rm "/content/DATA/DataSet_ConchasAbanico/${filename}"

#########################
cd /content/
echo "===> Creating folders..."
mkdir /content/drive/MyDrive/DATA
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/mask_process

echo "===> Downloading..."
id="1Hed8HHT2fp5AMZPagKexZamINm04ynis"
gdown --id $id
filename="images.zip"
src="/content/${filename}"
dst="/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images"
mv $src ${dst}

echo "===> Downloading..."
id="1asBQdvI7S8J0HkP1lAGWeDry0VSOtIwI"
gdown --id $id
filename="masks_process.zip"
src="/content/${filename}"
dst="/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/mask_process"
mv $src ${dst}
