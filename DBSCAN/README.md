# DBSCAN Clusteranalyse – Verkehrsunfälle Berlin (2018–2021)

Dieses Modul beinhaltet die Implementierung der dichtebasierten DBSCAN-Analyse auf Unfalldaten aus Berlin, unter Berücksichtigung geografischer und zeitlicher Merkmale.

---

## Struktur

```
DBSCAN/
├── notebooks/          → Analyse der DBSCAN-Ergebnisse
├── scripts/            → Tools zur Distanzberechnung und Modellanwendung
├── data/               → Eingabedaten, Koordinaten, Geo-Daten
├── output/plots/       → Diagramme und Karten
└── README.md           → Diese Datei
```

---

## Datenquellen

- `dbscan_encoded_data.csv`, `geo_coords.csv`: Vorverarbeitete Daten
- Distanzmatrizen (Euklid/Haversine): Extern via Google Drive
  [📂 Zum Download](https://drive.google.com/drive/folders/1QmqFjW6Ajc4rsulmfUj3tjEL7NWzuWBV?usp=sharing)

---

## Voraussetzungen

```bash
pip install pandas numpy geopandas scikit-learn matplotlib seaborn joblib tqdm fiona
```

Die Distanzmatrizen werden in Batches verarbeitet und liegen als `.npy`/`.npz`-Dateien vor.
