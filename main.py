from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Akıllı Şebeke Anormallik Tespiti API'si",
    description="Sensör ve tüketim verilerine göre şebekedeki anormallikleri tespit eden ML Servisi",
    version="1.0.0"
)

try:
    model = joblib.load('anormallik_modeli.pkl' )
    print("🤖 Makine Öğrenmesi Modeli başarıyla hafızaya yüklendi!")
except Exception as e:
    print(f"❌ Model yüklenirken hata oluştu: {e}")

class SebekeVerisi(BaseModel):
    Num_Occupants: int
    House_Area_sqft: float
    Appliance_Score: int
    Connected_Load_kw: float
    Temperature_C: float
    Humidity_pct: float
    Expected_Energy_kwh: float
    Actual_Energy_kwh: float
    Usage_Deviation_pct: float
    Cluster_Avg_Energy_kwh: float

@app.get("/")
def read_root():
    return {
        "mesaj": "Akıllı Şebeke Anormallik Tespiti API'sine Hoş Geldiniz!",
        "durum": "Sistem Aktif",
        "dokumantasyon": "/docs"
    }

@app.post("/predict")
def predict_anomaly(data: SebekeVerisi):
    # 1. API'den gelen veriyi DataFrame'e çeviriyoruz
    input_df = pd.DataFrame([{
        'Num_Occupants': data.Num_Occupants,
        'House_Area (sqft)': data.House_Area_sqft,
        'Appliance_Score': data.Appliance_Score,
        'Connected_Load(kw)': data.Connected_Load_kw,
        'Temperature_C': data.Temperature_C,
        'Humidity (%)': data.Humidity_pct,
        'Expected_Energy(kwh)': data.Expected_Energy_kwh,
        'Actual_Energy(kwh)': data.Actual_Energy_kwh,
        'Usage_Deviation(%)': data.Usage_Deviation_pct,
        'Cluster_Avg_Energy(kwh)': data.Cluster_Avg_Energy_kwh
    }])
    
    # 2. SİHİRLİ MÜHENDİSLİK DOKUNUŞU: Sütun Hizalama
    # Modelin eğitim sırasında ezberlediği sütun listesini çağırıyoruz
    beklenen_sutunlar = model.feature_names_in_
    
    # Gelen veriyi modelin beklediği formata zorluyoruz.
    # Fazla sütunları otomatik atar, eksik sütun varsa 0 ile doldurur.
    input_df = input_df.reindex(columns=beklenen_sutunlar, fill_value=0)
    
    # 3. Temizlenen veri ile tahmin yapıyoruz
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    return {
        "anormallik_var_mi": int(prediction),
        "anormallik_olasiligi": round(float(probability), 4),
        "tespit_sonucu": "ANORMAL KULLANIM (Riskli)" if prediction == 1 else "NORMAL KULLANIM (Güvenli)"
    }
    
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    return {
        "anormallik_var_mi": int(prediction),
        "anormallik_olasiligi": round(float(probability), 4),
        "tespit_sonucu": "ANORMAL KULLANIM (Riskli)" if prediction == 1 else "NORMAL KULLANIM (Güvenli)"
    }