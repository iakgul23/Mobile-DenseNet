# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:43:07 2020

@author: IAKGUL
"""

import sys
sys.path.append('..')
import Functions as fn

for i, etiket in enumerate(fn.etiketler):
    fn.mkdir(fn.resimlerDiziniOnIslenmis + '/' + etiket)
    etiket_klasoru = fn.resimlerDiziniOrjinal + '/' + etiket
    for resim_adi in fn.listdir(etiket_klasoru):
        fn.resmi_kaydet(etiket_klasoru + '/' + resim_adi, etiket + '/' + resim_adi, fn.renkliDeger)
