# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:54:26 2020

@author: IAKGUL
"""

from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

import sys
sys.path.append('..')
import Functions as fn

X, Y = [], []
for i, etiket in enumerate(fn.etiketler):
    etiket_klasoru = fn.resimlerDiziniOnIslenmis + '/' + etiket
    for resim_adi in fn.listdir(etiket_klasoru):
        resim = fn.resmi_al(etiket_klasoru + '/' + resim_adi, fn.renkliDeger)
        X.append(resim)
        Y.append(i)

if(fn.renkliDeger=="gray"):
    X = fn.np.array(X).astype('float32')/255.
elif(fn.renkliDeger=="colourful"):
    X = fn.np.array(X).astype('float32')
X = X.reshape(X.shape[0], fn.boy, fn.en, fn.kanal)

#Sample Demonstration
#------------------------------
from matplotlib import pyplot as plt
plt.imshow(fn.np.squeeze(X[10]))
plt.show()
#------------------------------
#Sample Demonstration

Y = fn.np.array(Y).astype('float32')
Y = to_categorical(Y, fn.etiketSayisi)

x, x_test, y, y_test = train_test_split(X, Y, test_size=0.15, random_state=1, stratify=Y)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.1764705, random_state=1, stratify=y)
fn.np.save('Datasets/x_train.npy', x_train)
fn.np.save('Datasets/y_train.npy', y_train)
fn.np.save('Datasets/x_test.npy', x_test)
fn.np.save('Datasets/y_test.npy', y_test)
fn.np.save('Datasets/x_val.npy', x_val)
fn.np.save('Datasets/y_val.npy', y_val)
