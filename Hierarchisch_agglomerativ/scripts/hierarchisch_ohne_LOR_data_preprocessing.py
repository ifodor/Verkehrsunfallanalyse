import numpy as np  # Für numerische Berechnungen
import pandas as pd  # Für die Verarbeitung von tabellarischen Daten
import joblib  # Zum Speichern und Laden von Modellen (Scaler, Encoder)
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder  # Für Normalisierung und Kategorisierung

def preprocess_data(file_path, save_path="hierarchisch_encoded_data.csv"):
    df = pd.read_csv(file_path)

    # LOR_ab_2021 entfernen, aber BEZ (Bezirk) nicht – BEZ ist für das Clustern pro Bezirk wichtig.
    df = df.drop(columns=['LOR_ab_2021'], errors='ignore')

    # Variablen definieren
    numerical_vars = ['UJAHR', 'UMONAT', 'USTUNDE', 'UWOCHENTAG']
    coordinate_vars = ['XGCSWGS84', 'YGCSWGS84']  # Für Visualisierung benötigt
    ordinal_vars = ['UKATEGORIE']
    nominal_vars = ['UART', 'UTYP1', 'ULICHTVERH', 'USTRZUSTAND']
    binary_vars = ['IstRad', 'IstPKW', 'IstFuss', 'IstKrad', 'IstGkfz', 'IstSonstige']
    
    # Sicherstellen, dass BEZ vorhanden ist (BEZ: Bezirk, Zahl von 1 bis 12)
    if "BEZ" not in df.columns:
        raise ValueError("Die Spalte 'BEZ' (Bezirk) fehlt im Datensatz!")
    
    # Fehlende Werte entfernen (inklusive BEZ und Koordinaten)
    required_vars = numerical_vars + coordinate_vars + ordinal_vars + nominal_vars + binary_vars + ['BEZ']
    df = df.dropna(subset=required_vars)
    
    # Speichern der Koordinaten im Originalformat
    geo_coords = df[coordinate_vars].copy()
    geo_coords.to_csv("geo_coords.csv", index=False)
    
    # One-Hot-Encoding für nominale Variablen
    onehot_encoder = OneHotEncoder(sparse_output=True)
    onehot_encoded = onehot_encoder.fit_transform(df[nominal_vars])
    onehot_df = pd.DataFrame(onehot_encoded.toarray(), columns=onehot_encoder.get_feature_names_out(nominal_vars))
    
    df = df.drop(columns=nominal_vars)
    df = pd.concat([df, onehot_df], axis=1)
    
    # Min-Max Scaler für numerische Variablen und ordinale Variablen (BEZ bleibt unberührt, da es als Bezirk dient)
    scaler_vars = numerical_vars + ordinal_vars
    minmax_scaler = MinMaxScaler()
    df[scaler_vars] = minmax_scaler.fit_transform(df[scaler_vars])
    
    # Speichern des Scalers und One-Hot Encoders
    joblib.dump(minmax_scaler, 'min_max_scaler.pkl')
    joblib.dump(onehot_encoder, 'onehot_encoder.pkl')
    
    # Speichern der transformierten Daten
    df.to_csv(save_path, index=False)
    return df

# Daten transformieren & speichern
file_path = "bereinigte_daten.csv"
df_encoded = preprocess_data(file_path)
