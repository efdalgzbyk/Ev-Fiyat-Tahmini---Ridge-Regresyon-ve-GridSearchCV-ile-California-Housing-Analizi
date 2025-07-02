
---

## 🇬🇧 English README


# House Price Prediction – Ridge Regression with California Housing Dataset

This project aims to predict housing prices in the state of California using machine learning techniques. A Ridge Regression model is trained on real-world housing data, focusing on regression basics, hyperparameter tuning, and performance visualization.

---

## 📌 Dataset Used

The project uses the California Housing dataset, fetched using `fetch_california_housing()` from `sklearn.datasets`. It includes features such as:

- Average number of rooms
- Average household income
- Crime rate
- Proximity to schools
- Population density
- and more...

Target variable: **House price (in thousands of dollars)**

---

## 🔧 Technologies and Libraries

- Python 3.x
- scikit-learn
- pandas
- matplotlib
- seaborn
- joblib

---

## 🚀 Project Workflow

1. **Data Loading and Exploration:**  
   Load the dataset into a pandas DataFrame and generate a heatmap to analyze feature correlations.

2. **Train-Test Split:**  
   Split the dataset into 80% training and 20% testing sets.

3. **Model Training (Ridge Regression):**  
   Train a Ridge Regression model with hyperparameter optimization (`alpha`) using GridSearchCV.

4. **Model Evaluation:**  
   Evaluate model performance using R² score and Mean Squared Error (MSE).

5. **Prediction Visualization:**  
   Plot predicted vs actual house prices in a scatter plot (`price_prediction_plot.png`).

6. **Model Saving:**  
   Save the trained model to a `.pkl` file (`house_price_model.pkl`).

---

## 📁 Generated Files

- `house_price_prediction.py`: Main project script
- `feature_correlation.png`: Feature correlation heatmap
- `price_prediction_plot.png`: Actual vs predicted price plot
- `house_price_model.pkl`: Saved trained model

---

## 💻 Run the Project

To execute the script, run:

```bash
python house_price_prediction.py
```



# Ev Fiyat Tahmini – Ridge Regresyon ile California Housing Dataset

Bu proje, ABD'nin California eyaletine ait konut verilerini kullanarak ev fiyatlarını tahmin etmeyi amaçlamaktadır. Ridge regresyon modeli ile eğitilen bu proje, temel makine öğrenmesi regresyon algoritmalarını öğrenmek, hiperparametre optimizasyonu yapmak ve model performansını görselleştirmek isteyenler için pratik bir örnektir.

---

## 📌 Kullanılan Veri Seti

Bu projede, `sklearn.datasets` içindeki `fetch_california_housing()` fonksiyonu kullanılarak yüklenen California Housing veri seti kullanılmıştır. Veri seti aşağıdaki özellikleri içerir:

- Ortalama oda sayısı
- Ortalama hane geliri
- Suç oranı
- Okul yakınlığı
- Nüfus yoğunluğu
- ve daha fazlası...

Hedef değişken: **Ev fiyatı (binlerce dolar cinsinden)**

---

## 🔧 Kullanılan Teknolojiler ve Kütüphaneler

- Python 3.x
- scikit-learn
- pandas
- matplotlib
- seaborn
- joblib

---

## 🚀 Proje Aşamaları

1. **Veri Yükleme ve İnceleme:**  
   California konut verisi yüklenir ve pandas DataFrame'e dönüştürülür. Özellikler incelenir ve korelasyon haritası çıkarılır.

2. **Eğitim ve Test Bölme:**  
   Veri seti %80 eğitim ve %20 test olarak ikiye ayrılır.

3. **Model Eğitimi (Ridge Regresyon):**  
   Ridge regresyon modeli, GridSearchCV ile `alpha` hiperparametresi için optimize edilir.

4. **Model Değerlendirme:**  
   Modelin doğruluğu R² skoru ve Ortalama Kare Hatası (MSE) ile ölçülür.

5. **Tahmin Görselleştirmesi:**  
   Gerçek ve tahmin edilen fiyatlar bir grafikte karşılaştırılır (`price_prediction_plot.png`).

6. **Model Kaydetme:**  
   Eğitilen model `.pkl` dosyasına (`house_price_model.pkl`) kaydedilir.

---

## 📁 Üretilen Dosyalar

- `house_price_prediction.py`: Ana proje dosyası
- `feature_correlation.png`: Korelasyon ısı haritası
- `price_prediction_plot.png`: Tahmin grafiği
- `house_price_model.pkl`: Eğitilmiş model

---

## 💻 Çalıştırma

Aşağıdaki komutu kullanarak projeyi çalıştırabilirsiniz:

```bash
python house_price_prediction.py

