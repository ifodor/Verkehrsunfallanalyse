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
- Die **Distanzmatrizen** (euklidische und haversine) sind in **Batches unterteilt** und können nicht direkt im Repository bereitgestellt werden.
- Aufgrund der **Größe der Daten** (insgesamt über 50 GB) werden sie **in Google Drive** gespeichert. Um auf diese Daten zuzugreifen, kannst du den **Link zu den Google Drive-Dateien** verwenden, der in diesem Repository bereitgestellt wird (oder die Dateien von dort herunterladen).
  - **Google Drive** ist über [diesen Link](https://drive.google.com) erreichbar. Weitere Anweisungen folgen.

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

Da die erzeugten Distanzmatrizen sehr groß sind, wurden sie in **Batches** gespeichert und auf **Google Drive** hochgeladen. Die Links zu den Batch-Dateien sind im entsprechenden Ordner auf Dropbox verfügbar, um den Zugriff und die Verwendung der großen Dateien zu erleichtern.

- **Euklidische Distanzen**: Batches der euklidischen Distanzen sind als `.npy`-Dateien gespeichert und wurden auf Google-Drive hochgeladen.
- **Haversine Distanzen**: Ebenso wurden die Haversine-Distanzen in Batches verarbeitet und hochgeladen.

## Verarbeitung der Distanzmatrizen:
Die Berechnung der Distanzen erfolgt in **Batches**:
- **Batch-Verarbeitung**: Die **euklidische** und **haversine Distanz** werden parallelisiert und nach Batches in separate **.npy**-Dateien gespeichert. Diese Dateien werden als **Sparse-Matrizen** in einem **.npz**-Format abgespeichert.
- **Datenzugriff**: Die geladenen Distanzen werden dann verwendet, um DBSCAN auf den verarbeiteten Distanzmatrizen auszuführen.

## Code Erklärung
- **Distanzmatrix-Berechnung**: Der Code berechnet die Distanzmatrizen in kleinen Batches, um Speicherprobleme zu vermeiden.
- **DBSCAN Clustering**: Mit den berechneten Distanzen wird der **DBSCAN-Algorithmus** angewendet, um die Verkehrsunfälle zu clustern.

### Google Drive-Links:

Die Batch-Dateien (z. B. `euklid_batch_0.npy`, `haversine_batch_0.npz`) können über die entsprechenden Google Drive-Links heruntergeladen werden. Achten Sie darauf, die Dateien vor der Analyse herunterzuladen, falls sie benötigt werden.

## Ausführliche Anleitung
1. Lade die **Daten von Google Drive herunter** und platziere sie im richtigen Ordner.
2. Führe das Skript `dbscan_model.py` aus, um den DBSCAN-Clusterprozess zu starten.
3. Analysiere die Ergebnisse in der Datei `dbscan_merged_clusters.csv`.

## Anmerkungen:
- **Datenmengen**: Die Distanzmatrizen in den Batches sind sehr speicherintensiv, was dazu führt, dass sie auf **Google Drive** gespeichert und aus der Cloud geladen werden müssen.
- **Speicherplatz**: Stelle sicher, dass du genügend Speicherplatz auf deinem Google Drive hast, um die Daten herunterzuladen.
- **Parallelisierung**: Die Berechnungen der Distanzmatrizen in Batches werden mit **Parallelisierung** durchgeführt, um die Verarbeitung zu beschleunigen und Speicherprobleme zu vermeiden.

## Installation

Die folgenden Pakete müssen installiert sein, um das Projekt auszuführen:

```bash
pip install pandas numpy geopandas scikit-learn matplotlib seaborn joblib tqdm fiona
