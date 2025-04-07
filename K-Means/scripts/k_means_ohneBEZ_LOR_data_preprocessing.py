
# -*- coding: utf-8 -*-
"""
Preprocessing für KMeans-Clustering:
- Entfernt BEZ/LOR
- One-Hot-Encoding nominaler Merkmale
- Skalierung numerischer & koordinatenbezogener Merkmale
- Speicherung der transformierten Daten & Encoder
"""

# -------------------------------------------
#  Bibliotheken importieren
# -------------------------------------------

import numpy as np                          # Für numerische Berechnungen (z. B. Arrays)
import pandas as pd                         # Für tabellarische Datenverarbeitung
import joblib                               # Zum Speichern von Scaler & Encodern
from sklearn.preprocessing import StandardScaler, OneHotEncoder  # Für Skalierung & Kodierung

# -------------------------------------------
#  Funktion zur Datenvorverarbeitung
# -------------------------------------------

def preprocess_data(file_path, save_path="k_means_ohneBEZ_LOR_encoded_data.csv"):
    # Lade Rohdaten
    df = pd.read_csv(file_path)

    # Entferne Bezirks- und Raumbezugsspalten (nicht fürs Clustering)
    df = df.drop(columns=['BEZ', 'LOR_ab_2021'], errors='ignore')

    # Variablenlisten definieren
    numerical_vars = ['UJAHR', 'UMONAT', 'USTUNDE', 'UWOCHENTAG']
    coordinate_vars = ['XGCSWGS84', 'YGCSWGS84']
    ordinal_vars = ['UKATEGORIE']
    nominal_vars = ['UART', 'UTYP1', 'ULICHTVERH', 'USTRZUSTAND']
    binary_vars = ['IstRad', 'IstPKW', 'IstFuss', 'IstKrad', 'IstGkfz', 'IstSonstige']

    # Entferne Zeilen mit fehlenden Werten in relevanten Spalten
    df = df.dropna(subset=numerical_vars + coordinate_vars + ordinal_vars + nominal_vars + binary_vars)

    # -------------------------------------------
    #  One-Hot-Encoding für nominale Merkmale
    # -------------------------------------------

    onehot_encoder = OneHotEncoder(sparse_output=False)
    onehot_encoded = onehot_encoder.fit_transform(df[nominal_vars])
    onehot_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(nominal_vars))

    # Entferne Originalspalten und ersetze durch kodierte Spalten
    df = df.drop(columns=nominal_vars)
    df = pd.concat([df, onehot_df], axis=1)

    # -------------------------------------------
    #  Standardisierung der numerischen Werte & Koordinaten
    # -------------------------------------------

    std_scaler = StandardScaler()
    df[numerical_vars + coordinate_vars] = std_scaler.fit_transform(df[numerical_vars + coordinate_vars])

    # -------------------------------------------
    #  Modelle speichern & Daten exportieren
    # -------------------------------------------

    joblib.dump(std_scaler, 'k_means_std_scaler.pkl')
    joblib.dump(onehot_encoder, 'k_means_onehot_encoder.pkl')
    df.to_csv(save_path, index=False)

    return df

# -------------------------------------------
#  Anwendung: Datei laden & verarbeiten
# -------------------------------------------

file_path = "bereinigte_daten.csv"
df_encoded = preprocess_data(file_path)