import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def main():
    # 1. Veri setini yükle
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='Price')

    print("Veri seti boyutu:", X.shape)
    print("\nİlk 5 kayıt:")
    print(X.head())

    # 2. Korelasyon haritası
    plt.figure(figsize=(10,8))
    sns.heatmap(X.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Özellik Korelasyonları")
    plt.tight_layout()
    plt.savefig("feature_correlation.png")
    plt.show()

    # 3. Eğitim-test bölme
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Ridge regresyon + GridSearchCV
    model = Ridge()
    param_grid = {'alpha': [0.1, 1.0, 10.0, 100.0]}
    grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2')
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_
    print("En iyi alpha:", grid_search.best_params_['alpha'])

    # 5. Tahmin ve performans
    y_pred = best_model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"\nTest R² Skoru: {r2:.4f}")
    print(f"Ortalama Kare Hatası (MSE): {mse:.4f}")

    # 6. Tahmin görselleştirme
    plt.figure(figsize=(8,6))
    plt.scatter(y_test, y_pred, alpha=0.6, color='teal')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel("Gerçek Fiyat")
    plt.ylabel("Tahmin Edilen Fiyat")
    plt.title("Gerçek vs Tahmin Edilen Ev Fiyatları")
    plt.tight_layout()
    plt.savefig("price_prediction_plot.png")
    plt.show()

    # 7. Modeli kaydet
    joblib.dump(best_model, 'house_price_model.pkl')
    print("\nModel 'house_price_model.pkl' olarak kaydedildi.")

if __name__ == "__main__":
    main()
