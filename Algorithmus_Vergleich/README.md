# Vergleich von Clustering-Algorithmen

Im Zuge der Auswertung nach der Durchführung der Cluster-Analyse vergleicht dieses Script die verwendeten Clustering-Methoden — **K-Means**, **DBSCAN** und **agglomeratives Clustering** — anhand von drei Evaluationskriterien. Ziel ist es, die Qualität der Clusterbildung sowohl hinsichtlich interner Konsistenz als auch statistischer Trennschärfe zu bewerten.

---

## Bewertete Kriterien

| Kriterium                  | Ziel                         |
|---------------------------|------------------------------|
| Silhouette-Wert           | Hoch → gute Trennung         |
| Davies-Bouldin-Index      | Niedrig → geringe Überlappung|
| Signifikante Features     | Hoch → klare Merkmalsunterschiede |

---

## Struktur

```
Algorithmus_Vergleich/
├── notebooks/          → Vergleich und Visualisierung der Kennwerte
├── output/plots/       → PNG-Grafiken der Bewertungsdiagramme
└── README.md           → Diese Datei
```

---

## Abhängigkeiten

```bash
pip install pandas matplotlib seaborn
```

Die Auswertung erzeugt eine Grafik `Clustering_Evaluation_Horizontal.png`, die die Methoden gegenüberstellt.
