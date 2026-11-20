# 🌌 Die Repo-Galaxie

Eine interaktive 3D-Sternenkarte der **500 GitHub-Repositories mit den meisten Sternen**.

- Jeder Lichtpunkt ist ein echtes Open-Source-Projekt. Größe und Helligkeit zeigen die Sterne auf GitHub.
- Jede Programmiersprache bildet einen eigenen Spiralarm, in der Farbe, die GitHub für die Sprache verwendet.
- Alte Projekte liegen nahe am Kern, neue weit draußen.
- Ziehen zum Drehen, Scrollen oder Zwei-Finger-Zoom, Klick auf einen Stern für Details.

## Wie es funktioniert

| Datei | Aufgabe |
| --- | --- |
| `index.html` | Die ganze Galaxie: Canvas-Rendering, Steuerung, Suche. Keine Abhängigkeiten. |
| `data.json` | Die Repo-Daten (Name, Sterne, Forks, Sprache, Jahr, Topics). |
| `scripts/update_data.py` | Holt frische Daten über die GitHub-Such-API. |
| `.github/workflows/update.yml` | Läuft jeden Montag und aktualisiert `data.json` automatisch. |

## Lokal starten

```bash
python3 -m http.server 8000
```

Dann http://localhost:8000 im Browser öffnen.

## Online stellen mit GitHub Pages

**Settings → Pages → Source: „Deploy from a branch“ → Branch `main`, Ordner `/ (root)`** auswählen. Nach etwa einer Minute ist die Galaxie online.
