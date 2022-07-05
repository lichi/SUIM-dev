#!/bin/bash
pip install --upgrade --no-cache-dir gdown

cd /content/
echo "===> Creating folders..."
mkdir /content/DATA
mkdir /content/DATA/DataSet_ConchaAbanico

echo "===> Downloading ABANICO dataset"
id="1qJpTORrTuCETMWg3FBJeCaCrn8IVrBDh"

gdown --id $id
filename="train_val.rar"
src="/content/${filename}"
dst="/content/DATA/DataSet_ConchaAbanico"
mv $src ${dst}

echo "===> Unzipping ${filename}"
unrar x -Y "/content/DATA/DataSet_ConchaAbanico/${filename}" "/content/DATA/DataSet_ConchaAbanico"
rm "/content/DATA/DataSet_ConchaAbanico/${filename}"