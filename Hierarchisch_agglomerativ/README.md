# Agglomerative Clusteranalyse – Verkehrsunfälle Berlin (2018–2021)

In diesem Modul wird eine hierarchische Clusteranalyse für Verkehrsunfalldaten aus Berlin durchgeführt – separat für jeden Bezirk.

---

## Ziel

Identifikation lokaltypischer Unfallmuster in den 12 Berliner Bezirken auf Basis hierarchischer Strukturen.

---

## Struktur

```
Hierarchisch_agglomerativ/
├── notebooks/          → Clusterbildung, Dendrogramme, Visualisierungen
├── scripts/            → Vorverarbeitung & Modellierung pro Bezirk
├── data/               → Eingabedaten & Geo-Daten
├── output/plots/       → Dendrogramme & Clusterkarten
└── README.md           → Diese Datei
```

---

## Clusterbildung

Die Anzahl der Cluster wird **automatisch** aus dem **Dendrogramm** bestimmt (Cutoff bei 70% der maximalen Höhe). Ergebnisse werden bezirksweise gespeichert (`best_clusters.csv`).

---

## Daten

- `hierarchisch_encoded_data.csv`: Eingabedaten
- `geo_coords.csv`: Geokoordinaten der Unfälle
- `hierarchisch_final_clusters_pro_bezirk.csv`: Clusterzuordnungen
