# Agglomerative Clusteranalyse - Verkehrsunfälle in Berlin

## Beschreibung

Der **Agglomerative Clusteransatz** wird zur Analyse von Verkehrsunfällen in Berlin (2018–2021) verwendet, genauer noch, die Analyse wird für jedes der 12 Berliner Bezirke separat durchgeführt. Für jeden Bezirk wird automatisch die optimale Anzahl an Clustern bestimmt, indem ein Dendrogramm erstellt und an einem Schnittpunkt die Cluster abgeschnitten werden.

Die Analyse hilft dabei, **Cluster von Verkehrsunfällen** basierend auf geografischen und zeitlichen Merkmalen zu identifizieren und zu untersuchen.

## Inhalt

- **notebooks/**: Jupyter Notebooks für die interaktive Analyse der Ergebnisse der Agglomerativen Clusteranalyse.
- **scripts/**: Python-Skripte für die Datenvorverarbeitung, Modellierung und Analyse.
- **data/**: Enthält die Rohdaten sowie die verarbeiteten und modellierten Datensätze.
- **output/**: Hier werden die Visualisierungen der Clusterergebnisse und die analysierten Daten gespeichert.

## Daten

Die Verkehrsunfalldaten stammen aus Berlin und decken den Zeitraum von 2018 bis 2021 ab. Es werden geographische Koordinaten, Zeitstempel und verschiedene Merkmale der Unfälle verwendet.

### Eingabedaten:

- `hierarchisch_encoded_data.csv`: Die transformierten und vorverarbeiteten Verkehrsunfalldaten, die für die Agglomerative Clusteranalyse verwendet werden.
- `geo_coords.csv`: Die geographischen Koordinaten (Längen- und Breitengrad) der Unfälle.

### Ausgabedaten:

- `hierarchisch_final_clusters_pro_bezirk.csv`: Eine CSV-Datei, die die Clusterzuordnung der Verkehrsunfälle für jeden Bezirk enthält.
- `best_clusters.csv`: Eine CSV-Datei mit der **optimalen Anzahl von Clustern** für jeden Bezirk.
- Visualisierungen der **Dendrogramme** und **Clusterergebnisse** (in `output/plots`).

## Agglomerative Clusteranalyse

Für die **Agglomerative Clusteranalyse** wird die Clusteranzahl nicht direkt vorgegeben, sondern durch die Analyse des **Dendrogramms** automatisch festgelegt. Der **Schwellenwert für den Schnitt** des Dendrogramms wird so gewählt, dass eine sinnvolle Clusteranzahl pro Bezirk entsteht.

### Schritte der Analyse:

1. **Dendrogramm-Erstellung**: Für jeden Bezirk wird ein **Dendrogramm** erstellt, das die hierarchische Clusterbildung anzeigt. Die optimale Clusteranzahl wird durch das **Schneiden des Dendrogramms** bestimmt, basierend auf einem festgelegten **Schwellenwert** (70% der maximalen Höhe des Dendrogramms).
   
2. **Clusterbildung**: Die Cluster werden mit der **optimalen Clusteranzahl** für jeden Bezirk gebildet und die Clusterzuordnungen werden dem DataFrame hinzugefügt.

3. **Visualisierung der Dendrogramme**: Das Dendrogramm für jeden Bezirk wird visualisiert und gespeichert. Die Ergebnisse werden in **PNG-Dateien** im Ordner `output/plots` abgelegt.

## Clusterzuordnung und Ergebnisse

Für jeden Bezirk wird die **Clusterzuordnung** in einer separaten Spalte im DataFrame gespeichert. Die Anzahl der Cluster pro Bezirk wird automatisch ermittelt und in der Datei `best_clusters.csv` gespeichert.

### Wichtige Dateien:
- `hierarchisch_encoded_data.csv`: Vorverarbeitete, transformierte Daten, die für die Agglomerative Clusteranalyse verwendet werden.
- `hierarchisch_final_clusters_pro_bezirk.csv`: Eine CSV-Datei mit den finalen Clusterzuordnungen für jedes Verkehrsunfallereignis.
- Visualisierungen der Dendrogramme in `output/plots/`.

