# DBSCAN Clusteranalyse - Verkehrsunfälle in Berlin

## Beschreibung

Dieses Repository enthält die Implementierung und Ergebnisse der **DBSCAN Clusteranalyse** auf Verkehrsunfalldaten aus Berlin (2018–2021). DBSCAN (Density-Based Spatial Clustering of Applications with Noise) ist ein Algorithmus zur Clusterbildung, der dichte Bereiche von Datenpunkten identifiziert und aus diesen Clustern schließt, während er Rauschpunkte (Ausreißer) ignoriert.

Die Analyse verwendet geographische und andere Merkmale von Verkehrsunfällen, um Muster und Cluster zu identifizieren, die für die Verkehrssicherheit und Unfallprävention relevant sind.

## Inhalt

- **notebooks/**: Jupyter Notebooks für die interaktive Analyse der DBSCAN-Ergebnisse.
- **scripts/**: Python-Skripte für die Datenvorverarbeitung, Modellierung und Analyse.
- **data/**: Enthält die Rohdaten sowie die verarbeiteten und modellierten Datensätze.
- **output/**: Hier werden die Visualisierungen der Clusterergebnisse und die analysierten Daten gespeichert.

## Daten

Die Verkehrsunfalldaten stammen aus Berlin und decken den Zeitraum von 2018 bis 2021 ab. Es werden geographische Koordinaten, Zeitstempel und verschiedene Merkmale der Unfälle verwendet.

### Eingabedaten:

- `dbscan_encoded_data.csv`: Die transformierten und vorverarbeiteten Verkehrsunfalldaten.
- `geo_coords.csv`: Die geographischen Koordinaten (Längen- und Breitengrad) der Unfälle.
- `bezirksgrenzen.geojson`: Die GeoJSON-Datei mit den Bezirksgrenzen Berlins.

### Ausgabedaten:

- `dbscan_merged_clusters.npy`: Die Clusterzuordnungen für die Verkehrsunfälle.
- `dbscan_cluster_results.csv`: Eine CSV-Datei mit den Clusterzuordnungen und den zugehörigen Merkmalen.
- Visualisierungen der Clusterergebnisse (in `output/plots`).

## Distanzmatrizen

Für die Berechnung der Distanzmatrizen wurden **euklidische Distanzen** und **Haversine-Distanzen** verwendet. Aufgrund der großen Datenmengen, die bei der Berechnung der Distanzen anfallen, wurden die Distanzen in **Batches** berechnet, um die Effizienz zu steigern und die Speicheranforderungen zu reduzieren.

- **Euklidische Distanz**: Berechnet die lineare Entfernung zwischen den Punkten in den geografischen Koordinaten.
- **Haversine-Distanz**: Berechnet die Entfernung unter Berücksichtigung der Erdkrümmung.

Da die erzeugten Distanzmatrizen sehr groß sind, wurden sie in Batches gespeichert und auf **Dropbox** hochgeladen. Die Links zu den Batch-Dateien sind im entsprechenden Ordner auf Dropbox verfügbar, um den Zugriff und die Verwendung der großen Dateien zu erleichtern.

- **Euklidische Distanzen**: Batches der euklidischen Distanzen sind als `.npy`-Dateien gespeichert und wurden auf Dropbox hochgeladen.
- **Haversine Distanzen**: Ebenso wurden die Haversine-Distanzen in Batches verarbeitet und hochgeladen.

### Dropbox-Links:

Die Batch-Dateien (z. B. `euklid_batch_500.npy`, `haversine_batch_0.npz`) können über die entsprechenden Dropbox-Links heruntergeladen werden. Achten Sie darauf, die Dateien vor der Analyse herunterzuladen, falls sie benötigt werden.

## Installation

Die folgenden Pakete müssen installiert sein, um das Projekt auszuführen:

```bash
pip install pandas numpy geopandas scikit-learn matplotlib seaborn joblib tqdm fiona
