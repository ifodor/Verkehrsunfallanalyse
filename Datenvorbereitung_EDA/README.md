# Verkehrsunfallanalyse Berlin (2018–2021)

Dieses Projekt untersucht Verkehrsunfalldaten aus Berlin im Zeitraum 2018–2021 mittels explorativer Datenanalyse, räumlicher Visualisierung und Clusteranalyse. Ziel ist es, Muster und Risikokonstellationen zu erkennen, die zur datenbasierten Verkehrsplanung beitragen können.

---

## Inhalte

Das Projekt besteht aus vier modularen Analysebausteinen:

### 01_Datenvorbereitung.ipynb
- Einlesen und Bereinigung der Rohdaten
- Erstellung neuer Variablen (Jahreszeit, Tag/Nacht, Verkehrsmittelbeteiligung etc.)
- Ausgabe: `bereinigte_daten.csv`

### 02_EDA.ipynb
- Explorative Datenanalyse (EDA)
- Zeitliche Trends (Monat, Wochentag, Stunde, Jahreszeit)
- Beteiligte Verkehrsmittel und Unfallkategorien
- Korrelationen (Pearson, Cramér’s V)
- Ausgabe: Heatmaps, Balkendiagramme, Kennzahlen

### 03_räumliche_Analyse.ipynb
- Räumliche Verteilung der Unfälle auf Bezirks- und LOR-Ebene
- Verwendung von GeoJSON-Daten (`lor_planungsraeume_2021.geojson`)
- Darstellung mit `matplotlib`, `geopandas` und `folium`
- Erstellung statischer Karten (PNG)

### 04_Prozessübersicht.ipynb
- Visuelle Darstellung des methodischen Workflows
- Übersicht über Schritte: Datenvorbereitung → Clustering → Qualitätsbewertung → Interpretation

---

## Daten

- **Unfalldaten**: Verkehrsunfälle Berlin (2018–2021)  
  Quelle: Berliner Open Data Portal
- **Geodaten**: Planungsräume (LOR)  
  Datei: `lor_planungsraeume_2021.geojson`  
  Quelle: [ODIS Berlin](https://daten.odis-berlin.de/de/dataset/lor_planungsgraeume_2021/)
- **Geodaten**: Bezirke    
  Datei: `bezirksgrenzen.geojson`  
  Quelle: [ODIS Berlin](https://daten.odis-berlin.de/de/dataset/bezirksgrenzen/)

---

## Abhängigkeiten

Die Notebooks nutzen folgende Python-Bibliotheken:

- pandas
- numpy
- matplotlib
- seaborn
- geopandas
- folium
- shapely
- adjustText
- scikit-learn
- scipy
