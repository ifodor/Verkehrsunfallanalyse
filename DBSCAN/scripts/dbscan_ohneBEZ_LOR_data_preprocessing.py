import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

def preprocess_data_for_dbscan(file_path, save_path="dbscan_encoded_data.csv"):
    df = pd.read_csv(file_path)

    # BEZ & LOR direkt aus dem DataFrame entfernen
    df = df.drop(columns=['BEZ', 'LOR_ab_2021'], errors='ignore')

    # Variablen definieren
    numerical_vars = ['UJAHR', 'UMONAT', 'USTUNDE', 'UWOCHENTAG']
    coordinate_vars = ['XGCSWGS84', 'YGCSWGS84']  # Geographische Koordinaten
    ordinal_vars = ['UKATEGORIE']
    nominal_vars = ['UART', 'UTYP1', 'ULICHTVERH', 'USTRZUSTAND']
    binary_vars = ['IstRad', 'IstPKW', 'IstFuss', 'IstKrad', 'IstGkfz', 'IstSonstige']

    # Fehlende Werte entfernen
    df = df.dropna(subset=numerical_vars + coordinate_vars + ordinal_vars + nominal_vars + binary_vars)

    # Speichern der Koordinaten im Originalformat**
    geo_coords = df[coordinate_vars].copy()  # WICHTIG: Als DataFrame behalten

    # One-Hot-Encoding für nominale Variablen
    onehot_encoder = OneHotEncoder(sparse_output=False)
    onehot_encoded = onehot_encoder.fit_transform(df[nominal_vars])
    onehot_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(nominal_vars))
    df = df.drop(columns=nominal_vars)  # Originale nominale Variablen entfernen
    df = pd.concat([df, onehot_df], axis=1)  # Füge die One-Hot-kodierten Variablen hinzu


    # MinMaxScaler für alle nicht-geographischen numerischen Variablen
    minmax_scaler = MinMaxScaler()
    df[numerical_vars + ordinal_vars] = minmax_scaler.fit_transform(df[numerical_vars + ordinal_vars])

    # Speichern der Encoder & Scaler
    joblib.dump(minmax_scaler, 'dbscan_minmax_scaler.pkl')
    joblib.dump(onehot_encoder, 'dbscan_onehot_encoder.pkl')

    # Geokoordinaten wieder hinzufügen (im Originalformat!)**
    df_no_geo = df.drop(columns=coordinate_vars)  # Geographische Variablen entfernen für Skalierung
    df_no_geo[['XGCSWGS84', 'YGCSWGS84']] = geo_coords  # Originalwerte wieder einfügen

    # Speichern der transformierten Daten (mit unskalierten Koordinaten)**
    df_no_geo.to_csv(save_path, index=False)

    # Speichern der geographischen Koordinaten separat**
    geo_coords.to_csv("geo_coords.csv", index=False)

    return df_no_geo, geo_coords  # Rückgabe der Daten & Koordinaten für spätere Distanzberechnung

# Daten transformieren & speichern
file_path = "bereinigte_daten.csv"
df_encoded, geo_coords = preprocess_data_for_dbscan(file_path)
