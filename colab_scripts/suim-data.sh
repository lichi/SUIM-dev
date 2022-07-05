#!/bin/bash
pip install --upgrade --no-cache-dir gdown

cd /content/
echo "===> Creating ckpt/saved folder..."
mkdir DATA/SUIM

echo "===> Downloading SUIM train_val"
id="1ZXf4Vu1PjR2uDzr-kQQrj7X21B-EetIz"

gdown --id $id
filename="train_val.zip"
src="/content/${filename}"
dst="/content/DATA/SUIM"
mv $src ${dst}

echo "===> Unzipping ${filename}"
unzip -q "/content/DATA/SUIM/${filename}" -d "/content/DATA/SUIM"
rm "/content/DATA/SUIM/${filename}"