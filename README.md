# Verkehrsunfallanalyse Berlin (2018–2021)

Dieses Projekt analysiert Verkehrsunfalldaten aus Berlin mit dem Ziel, typische Muster und Risikokonstellationen mithilfe von Clusteranalyse zu identifizieren. Die Analyse erfolgt schrittweise von der Datenaufbereitung bis zum Vergleich verschiedener Clustering-Algorithmen.

---

## Projektstruktur (Hauptordner)

Die Analyse ist in fünf thematische Hauptordner unterteilt:

1. `Datenvorbereitung_EDA/`  
2. `K-Means/`  
3. `DBSCAN/`  
4. `Hierarchisch_agglomerativ/`  
5. `Algorithmus_Vergleich/`

### Reihenfolge der Ausführung

Die Module bauen aufeinander auf und sollten in folgender Reihenfolge ausgeführt werden:

1. **Datenvorbereitung & EDA**
2. **K-Means-Analyse**
3. **DBSCAN-Analyse**
4. **Hierarchisch-agglomerative Analyse**
5. **Vergleich der Verfahren**

---

## Ordnerstruktur innerhalb jedes Moduls

Jede Methode (z. B. `DBSCAN/`, `K-Means/`) folgt derselben einheitlichen Struktur:

```
DBSCAN/
├── data/             → Bereinigte und ggf. reduzierte Eingabedaten
├── notebooks/        → Jupyter-Notebooks mit allen Auswertungen & Visualisierungen
├── scripts/          → Python-Skripte zur Analyse (optional)
├── ouput/plots/      → Generierte Diagramme & Karten (PNG)
└── README.md         → Kurze Dokumentation zum jeweiligen Modul
```

> **Hinweis**: Alle benötigten Dateien befinden sich vollständig im jeweiligen Methodenordner. Es ist keine externe Datei-Referenzierung nötig.

---

## Ziel

Ziel ist die datenbasierte Erkennung räumlich-zeitlicher Unfallmuster zur Unterstützung der Verkehrsplanung. Clusterverfahren helfen dabei, latente Strukturen und Risikogruppen aufzudecken.

---

## Verwendete Technologien

- **Analyse & Visualisierung**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`
- **Geodaten**: `geopandas`, `folium`, `shapely`, `adjustText`

---
