import imageio
from skimage.transform import resize
from os import listdir, mkdir
import numpy as np
import colorsys
import tensorflow as tf
import keras

import cv2

en = 96
boy = 96
kanal = 3

if(kanal==1):
    renkliDeger = "gri"
elif(kanal==3):
    renkliDeger = "renkli"

resimlerDiziniOrjinal = "Resimler_Orjinal"
resimlerDiziniOnIslenmis = "Resimler_OnIslenmis"

etiketler = listdir(resimlerDiziniOrjinal)
etiketler.sort()
etiketSayisi = len(etiketler)
liste1 = [0 for i in range(etiketSayisi)]
yeniliste = [liste1, etiketler]

enbuyuketiket = []
enbuyukdeger = []
enbuyukler = [enbuyukdeger, enbuyuketiket]

def kanal_ayarla(resim):
    """
    _, _, kanalSayisi = resim.shape
    if(kanalSayisi > 3):
        rgb2hsv = np.vectorize(colorsys.rgb_to_hsv)
        h,s,v = rgb2hsv(resim[:,:,0], resim[:,:,1], resim[:,:,2])
        h *= h
        hsv2rgb= np.vectorize(colorsys.hsv_to_rgb)
        resim = hsv2rgb(h,s,v)
        resim = np.array(resim).transpose((1,2,0))
        resim.flatten();
    """
    # In case of grayScale images the len(img.shape) == 2
    if len(resim.shape) > 2 and resim.shape[2] == 4:
        #convert the image from RGBA2RGB
        resim = cv2.cvtColor(resim, cv2.COLOR_BGRA2BGR)
    resim = resize(resim, (boy, en, kanal))
    return resim

def resmi_kaydet(path, etiket, deger):
    if(deger=="gri"):
        resim = imageio.imread(path, as_gray=True)
        resim.flatten();
        resim = resize(resim, (boy, en, kanal))
        imageio.imwrite(resimlerDiziniOnIslenmis + '/' + etiket, resim)
    elif(deger=="renkli"):
        resim = imageio.imread(path, as_gray=False)
        resim = kanal_ayarla(resim)
        imageio.imwrite(resimlerDiziniOnIslenmis + '/' + etiket, resim)

def resmi_al(path, deger):
    if(deger=="gri"):
        resim = imageio.imread(path, as_gray=True)
        resim.flatten();
        resim = resize(resim, (boy, en, kanal))
        return resim
    elif(deger=="renkli"):
        resim = imageio.imread(path, as_gray=False)
        resim = kanal_ayarla(resim)
        return resim
