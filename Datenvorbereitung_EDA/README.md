# Datenvorbereitung & Explorative Analyse – Verkehrsunfälle Berlin (2018–2021)

In diesem Modul erfolgt die grundlegende Vorbereitung der Verkehrsunfalldaten aus Berlin (2018–2021) sowie eine erste explorative Datenanalyse (EDA). Ziel ist die Aufbereitung der Datenbasis für die anschließende Clusteranalyse.

---

## Inhalte

- **01_Datenvorbereitung.ipynb**: Einlesen, Bereinigung und Anreicherung der Rohdaten
- **02_EDA.ipynb**: Analyse zeitlicher Muster, Beteiligungen, Korrelationen
- **03_räumliche_Analyse.ipynb**: Bezirks- und LOR-basierte Karten mit `geopandas`, `folium`
- **04_Prozessübersicht.ipynb**: Visualisierung des methodischen Workflows

---

## Struktur

```
Datenvorbereitung_EDA/
├── notebooks/          → Alle Analysen in Jupyter Notebooks
├── data/               → Roh- und bereinigte Daten
├── output/plots/       → Exportierte Diagramme und Karten
└── README.md           → Diese Dokumentation
```

---

## Daten

- `bereinigte_daten.csv`: Haupt-Datensatz für spätere Clusteranalysen
- `lor_planungsraeume_2021.geojson`: GeoJSON mit Berliner Planungsräumen
- `bezirksgrenzen.geojson`: Bezirksgrenzen Berlins (für Karten)

---

## Abhängigkeiten

```bash
pip install pandas numpy matplotlib seaborn geopandas folium shapely adjustText scikit-learn scipy
```
