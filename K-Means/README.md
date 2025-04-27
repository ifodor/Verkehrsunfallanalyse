# Clustering Analyse – K-Means (Berlin Verkehrsunfälle)

Dieses Modul enthält die Implementierung und Analyse der K-Means-Clusteranalyse für Verkehrsunfalldaten aus Berlin (2018–2021).

---

## Struktur

```
K-Means/
├── notebooks/          → Jupyter-Analyse: Clustering, Statistiken, Visualisierung
├── scripts/            → (Optional) Skripte zur Datenverarbeitung
├── data/               → Eingabedaten und Modellartefakte
├── output/plots/       → Visualisierte Ergebnisse
└── README.md           → Diese Datei
```

---

## Hinweise

- `.pkl`-Dateien wurden mit `scikit-learn 1.6.1` erzeugt
- Für Geo-Daten wird `geopandas` mit `pyogrio` empfohlen
