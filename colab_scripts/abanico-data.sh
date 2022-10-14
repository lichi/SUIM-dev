#!/bin/bash
pip install --upgrade --no-cache-dir gdown

cd /content/
echo "===> Creating folders..."
mkdir /content/DATA
mkdir /content/DATA/DataSet_ConchasAbanico

echo "===> Downloading ABANICO dataset"
#id="1qJpTORrTuCETMWg3FBJeCaCrn8IVrBDh"
id="1xrX4CoK2gCOsNJ7HjEuceiPtnbhfpugJ"


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
mkdir /content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/masks_process

echo "===> Downloading..."
#id="1Hed8HHT2fp5AMZPagKexZamINm04ynis"
id="1X9AwfK_Y3tSBDjK18-gl3o2ntZQEWNlc"
gdown --id $id
filename="images.zip"
src="/content/${filename}"
dst="/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images"
mv $src ${dst}

echo "===> Unzipping ${filename}"
unzip -q "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images/${filename}" -d "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images"
rm "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/images/${filename}"


echo "===> Downloading..."
#id="1asBQdvI7S8J0HkP1lAGWeDry0VSOtIwI"
id="1c-bO7xhGzIR0D9FfUs2uttp12nYOcgwK"
gdown --id $id
filename="masks_process.zip"
src="/content/${filename}"
dst="/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/masks_process"
mv $src ${dst}

echo "===> Unzipping ${filename}"
unzip -q "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/masks_process/${filename}" -d "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/masks_process"
rm "/content/drive/MyDrive/DATA/DataSet_ConchasAbanico/data/test/masks_process/${filename}"
