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


## Systemumgebung & Bibliotheken

Die Analyse wurde auf folgender Hardware- und Softwarebasis durchgeführt:

**Rechner:**
- Desktop-PC mit **Intel Core i3-6100** (2 Kerne / 4 Threads)
- 16 GB RAM
- SSD + HDD-Speicherlösung
- **NVIDIA GeForce GT 710**, Treiber 470.161.03

**Betriebssystem:**
- Linux Mint 20.3 "Una" (Ubuntu 20.04 LTS-basiert)
- Cinnamon 5.2.7 Desktop
- Kernel: 5.15.0-67-generic (x86_64)

**Python-Version:**
```bash
Python 3.8 (Ubuntu system default)
```

**Verwendete Bibliotheken (Auszug):**

| Bibliothek         | Version     |
|--------------------|-------------|
| pandas             | 2.0.3       |
| numpy              | 1.24.4      |
| matplotlib         | 3.7.5       |
| seaborn            | 0.13.2      |
| scikit-learn       | 1.3.2       |
| scipy              | 1.10.1      |
| geopandas          | 0.13.2      |
| shapely            | 2.0.2       |
| folium             | 0.18.0      |
| adjustText         | 1.3.0       |
| tqdm               | 4.67.1      |
| fiona              | 1.9.6       |
| pyogrio            | 0.9.0       |

> Für alle verwendeten Pakete siehe [`requirements.txt`](./requirements.txt)
