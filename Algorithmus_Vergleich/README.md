# Vergleich von Clustering-Algorithmen

Im Zuge der Auswertung nach der Durchführung der Cluster-Analyse vergleicht dieses Script die verwendeten Clustering-Methoden — **K-Means**, **DBSCAN** und **agglomeratives Clustering** — anhand von drei Evaluationskriterien. Ziel ist es, die Qualität der Clusterbildung sowohl hinsichtlich interner Konsistenz als auch statistischer Trennschärfe zu bewerten.

---

## Bewertete Kriterien

| Kriterium                     | Interpretation                  |
|------------------------------|----------------------------------|
| **Silhouette-Wert**          | Hoch = gute Trennung & Kompaktheit |
| **Davies-Bouldin-Index**     | Niedrig = gute Separierbarkeit  |
| **Signifikante Features**    | Hoch = starke Merkmalsunterscheidung zwischen Clustern |

---

## Visualisierung

Das Skript erzeugt eine horizontale Balkengrafik mit drei Subplots:

1. **Silhouette-Wert** (blau)
2. **Davies-Bouldin-Index** (rot)
3. **Anzahl signifikanter Features** (grün)

Die Ausgabe wird als PNG-Datei gespeichert:  
`Clustering_Evaluation_Horizontal.png`

---

## Abhängigkeiten

Dieses Skript verwendet folgende Python-Bibliotheken:

- `pandas`
- `matplotlib`
- `seaborn`
