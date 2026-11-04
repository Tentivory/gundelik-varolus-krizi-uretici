#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gündelik Varoluş Krizi Üretici
Her çalıştırmada yeni bir kriz.
"""

import random
import time

krizler = [
    "Buzdolabının ışığı kapanıyor. Ama biz bakmazsak, o ışık gerçekten var mıydı?",
    "Çoraplarım neden her zaman tekini kaybediyor? Belki diğeri daha iyi bir hayat yaşıyordur.",
    "Kahve soğuyor. Entropi artıyor. Demek ki evren beni özel olarak hedef almış.",
    "Neden her şey 'sonra yaparım' diyerek bitiyor? Sonra hiç gelmiyor.",
    "Telefon şarjı bitiyor. Belki de telefon da varoluşsal bir kriz yaşıyordur.",
    "Neden her Pazartesi aynı Pazartesi? Zaman döngüsü mü, yoksa sadece ben mi?",
    "Yemek yerken 'neden yiyorum?' diye düşünmek, yemeği daha lezzetli mi yapar?",
    "Rüzgar esiyor. Ama rüzgarın kendisi rüzgarı hissetmiyor. Adaletsizlik.",
]

def uret_kriz():
    print("\n" + "="*50)
    print("GÜNDELİK VAROLUŞ KRİZİ ÜRETİCİ v1.0")
    print("="*50)
    print("Kriz üretiliyor... Lütfen derin bir nefes alın.\n")
    time.sleep(1.5)
    
    kriz = random.choice(krizler)
    print(f">>> {kriz}\n")
    print("Bu kriz sizi etkilediyse, lütfen bir çay demleyin ve devam edin.")
    print("Etkilemediyse de demleyin. Çay her zaman iyi gelir.\n")

# Gizli not: Bazen en büyük krizler en küçük şeylerden doğar. 
# (Base64: SGlsYWwgZWRpbGVuIGtlbmRpIGJpcmkgZGVnaXNpbWxpaz8= )
# Yukarıdaki satır tamamen rastgeledir. Dekode etmeyin.

if __name__ == "__main__":
    uret_kriz()
