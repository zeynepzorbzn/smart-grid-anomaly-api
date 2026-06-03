Markdown
# ⚡ Smart Grid Anomaly Detection API (Akıllı Şebeke Anormallik Tespiti)

Bu proje, akıllı elektrik şebekelerindeki (Smart Grid) sensör ve tüketim verilerini analiz ederek, olası kaçakları, donanım arızalarını veya anormal kullanımları gerçek zamanlı olarak tespit eden uçtan uca bir **Makine Öğrenmesi (Machine Learning)** mikro servisidir.

Enerji sektöründe veri odaklı karar alma süreçlerini desteklemek amacıyla geliştirilmiş olup; Veri Bilimi (EDA & Modelleme) ile Yazılım Mühendisliği (FastAPI) disiplinlerini tek bir üründe birleştirir.

## 🚀 Öne Çıkan Özellikler (Features)
* **Veri Ön İşleme ve EDA:** Eksik verilerin (missing values) medyan ve mod stratejileriyle temizlenmesi; korelasyon ısı haritaları (Heatmap) ve saçılım grafikleri (Scatter Plot) ile sektörel içgörü çıkarımı.
* **Makine Öğrenmesi Mimarisi:** Test verisinde **%91.06 doğruluk (accuracy)** oranına ulaşan, aşırı öğrenmeden (overfitting) arındırılmış **Random Forest Classifier** modeli.
* **Üretim Ortamına Hazır API (Production-Ready):** Asenkron ve yüksek performanslı **FastAPI** kullanılarak geliştirilmiş, Swagger UI destekli modern web servisi.
* **Dinamik Şema Hizalama (Feature Alignment):** Dışarıdan gelen eksik veya hatalı JSON verilerine karşı modelin çökmesini engelleyen Pandas veri hizalama mühendisliği.

## 🛠️ Kullanılan Teknolojiler (Tech Stack)
* **Dil:** Python 3.12
* **Veri Bilimi & ML:** Scikit-Learn, Pandas, NumPy, Joblib
* **Görselleştirme:** Matplotlib, Seaborn
* **API & Sunucu:** FastAPI, Uvicorn, Pydantic

## 📂 Proje Yapısı
```text
├── main.py                          # FastAPI Sunucu Kodları ve Uç Noktalar (Endpoints)
├── Enerji_Verisi_Kesan_Analizi.ipynb # Veri Analizi, Keşif (EDA) ve Model Eğitimi (Jupyter)
├── anormallik_modeli.pkl            # Eğitilmiş Yapay Zeka Modeli (Random Forest)
├── veri.csv                         # Örnek Şebeke Sensör Veri Seti
└── requirements.txt                 # Gerekli Python Kütüphaneleri
⚙️ Nasıl Çalıştırılır? (How to Run)
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:
1. Repoyu Klonlayın ve Klasöre Girin:
Bash
git clone [https://github.com/zeynepzorbozan/smart-grid-anomaly-api.git](https://github.com/zeynepzorbozan/smart-grid-anomaly-api.git)
cd smart-grid-anomaly-api
2. Gerekli Kütüphaneleri Yükleyin:
Bash
pip install -r requirements.txt
3. API Sunucusunu Başlatın:
Bash
uvicorn main:app --reload
4. Canlı Test (Swagger UI):
Tarayıcınızı açın ve http://127.0.0.1:8000/docs adresine giderek modeli interaktif olarak test edin!
Developed by Zeynep Nur | Software Engineering Portfolio Project
