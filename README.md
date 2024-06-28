```markdown
# Open Science Portal Frontend

## Projektübersicht

Das Open Science Portal ist eine zentrale Plattform für Wissenschaftler und Forscher, um Forschungsergebnisse, Datensätze, Artikel, Publikationen und Projekte effizient zu teilen und zu verwalten. Diese Repository enthält den Quellcode für das Frontend der Plattform, das mit React entwickelt wurde.

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Projektstruktur](#projektstruktur)
- [Technologien](#technologien)
- [Mitwirkende](#mitwirkende)
- [Lizenz](#lizenz)

## Installation

### Voraussetzungen

Stellen Sie sicher, dass die folgenden Softwarekomponenten auf Ihrem System installiert sind:

- Node.js (Version 14 oder höher)
- npm (Node Package Manager)

### Schritte zur Installation

1. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/mur1chan/frontend.git
    ```

2. Navigieren Sie in das Projektverzeichnis:
    ```bash
    cd frontend
    ```

3. Installieren Sie die Abhängigkeiten:
    ```bash
    npm install
    ```

## Verwendung

### Entwicklung

Starten Sie die Entwicklungsumgebung mit:
```bash
npm start
```
Die Anwendung wird unter `http://localhost:3000` gestartet und Änderungen im Quellcode werden automatisch neu geladen.

### Produktion

Um eine Produktionsversion der Anwendung zu erstellen, führen Sie aus:
```bash
npm run build
```
Die optimierten Dateien befinden sich im Verzeichnis `build`.

## Projektstruktur

Die Projektstruktur ist wie folgt organisiert:

```
frontend/
├── src/
│   ├── components/        # Wiederverwendbare React-Komponenten
│   ├── pages/             # Seitenkomponenten für verschiedene Routen
│   ├── services/          # API-Service-Dateien für die Backend-Kommunikation
│   ├── styles/            # CSS-Dateien und Tailwind-Konfiguration
│   ├── App.js             # Haupteinstiegspunkt der React-Anwendung
│   └── index.js           # Einstiegsdatei für React
├── public/                # Statische Dateien
├── package.json           # Projektmetadaten und Abhängigkeiten
├── README.md              # Projektdokumentation
└── .gitignore             # Dateien und Verzeichnisse, die von Git ignoriert werden
```

## Technologien

Die folgenden Haupttechnologien und -bibliotheken werden in diesem Projekt verwendet:

- **React**: Eine JavaScript-Bibliothek für den Aufbau von Benutzeroberflächen
- **Tailwind CSS**: Ein CSS-Framework für die Erstellung von responsiven Designs
- **Axios**: Eine Bibliothek für HTTP-Anfragen
- **Webpack**: Ein Modul-Bundler für JavaScript-Dateien

## Mitwirkende

- **Abdul Rahman El Chatleh** (Projektleiter)
- **Sevde Kasapoglu**
- **Dennis Bremer**

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der `LICENSE`-Datei.
```

Feel free to customize this README to better fit your project's specifics.
