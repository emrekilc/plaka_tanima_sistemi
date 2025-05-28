# 🚗 Plaka Tanıma Sistemi

Bu proje, Python ve OpenCV kullanılarak geliştirilmiş bir plaka tanıma sistemidir. Sistem, araç görüntülerinden plakaları tespit eder, karakterleri ayrıştırır ve tanımlar. Makine öğrenimi teknikleriyle eğitilmiş bir model kullanarak, plaka üzerindeki karakterleri yüksek doğrulukla tanır.

## 🧠 Kullanılan Teknolojiler

* Python 3.x
* OpenCV
* scikit-learn (Random Forest)
* NumPy
* Matplotlib

## 📁 Proje Yapısı

```
plaka_tanima_sistemi/
├── PTS.py
├── alg1_plaka_tespiti.py
├── alg2_karakter_ayrıstırma.py
├── alg2_model_m_o.py
├── alg2_model_m_o_test.py
├── alg2_plaka_tanima.py
├── veri_seti_inceleme.py
├── rfc_model.rfc
├── plaka_sonuclar.txt
├── karakterseti/
├── veriseti/
└── __pycache__/
```

* `PTS.py`: Ana uygulama dosyasıdır.
* `alg1_plaka_tespiti.py`: Plaka tespiti için kullanılan algoritmaları içerir.
* `alg2_karakter_ayrıstırma.py`: Plaka üzerindeki karakterlerin ayrıştırılmasını sağlar.
* `alg2_model_m_o.py`: Modelin eğitilmesini gerçekleştirir.
* `alg2_model_m_o_test.py`: Eğitilen modelin test edilmesini sağlar.
* `alg2_plaka_tanima.py`: Plaka tanıma işlemini gerçekleştirir.
* `veri_seti_inceleme.py`: Veri setinin analizini yapar.
* `rfc_model.rfc`: Eğitilmiş Random Forest model dosyasıdır.
* `plaka_sonuclar.txt`: Tanınan plakaların sonuçlarını içerir.
* `karakterseti/`: Karakter görüntülerini barındırır.
* `veriseti/`: Plaka görüntülerini içerir.

## ⚙️ Kurulum

1. **Gereksinimleri Yükleyin:**

   ```bash
   pip install opencv-python numpy scikit-learn matplotlib
   ```

2. **Projeyi Klonlayın:**

   ```bash
   git clone https://github.com/emrekilc/plaka_tanima_sistemi.git
   cd plaka_tanima_sistemi
   ```

## 🚀 Kullanım

1. **Modeli Eğitmek:**

   ```bash
   python alg2_model_m_o.py
   ```

2. **Modeli Test Etmek:**

   ```bash
   python alg2_model_m_o_test.py
   ```

3. **Plaka Tanıma İşlemi:**

   ```bash
   python PTS.py
   ```

   Bu komut, `veriseti/` klasöründeki görüntüler üzerinde plaka tanıma işlemini gerçekleştirir ve sonuçları `plaka_sonuclar.txt` dosyasına kaydeder.

## 📝 Notlar

* `karakterseti/` ve `veriseti/` klasörlerinin içeriği, modelin doğruluğu için önemlidir. Bu klasörlerde yeterli ve çeşitli veri bulunmalıdır.
* `rfc_model.rfc` dosyası, eğitilmiş Random Forest modelini içerir. Modeli yeniden eğitmek isterseniz, mevcut dosyayı silip `alg2_model_m_o.py` dosyasını çalıştırabilirsiniz.

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen önce bir issue açın ve değişikliklerinizi tartışalım.

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

---

**Geliştirici:** Emre Kılıç
**GitHub:** [emrekilc](https://github.com/emrekilc)
