import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from alg1_plaka_tespiti import plaka_konum_don
from alg2_plaka_tanima import plakaTani

veriler = os.listdir("veriseti")

# Çıktıyı yazacağımız dosya
with open("plaka_sonuclar.txt", "w", encoding="utf-8") as dosya:
    for isim in veriler:
        yol = f"veriseti/{isim}"
        print("resim:", yol)
        dosya.write(f"resim: {yol}\n")

        img = cv2.imread(yol)
        img = cv2.resize(img, (500, 500))

        try:
            plaka = plaka_konum_don(img)
            plakaImg, plakaKarakter = plakaTani(img, plaka)
            sonuc = f"resimdeki plaka: {''.join(plakaKarakter)}\n"
        except Exception as e:
            sonuc = f"HATA: {str(e)}\n"

        print(sonuc)
        dosya.write(sonuc + "\n")

        # Eğer görselleştirme istenmiyorsa bu kısmı yoruma al:
        # plt.imshow(plakaImg)
        # plt.show()
