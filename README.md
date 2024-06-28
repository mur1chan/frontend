# **THIS IS THE README OF THE FRONTEND GROUP**

# about this project
this is currently a university project. it's an open source platform (similar to research gate), where people can write and share their research papers. 

# background of the project

To make the website dynamic, I use htmx (htmx mentioned), and for the design, I rely on TailwindCSS with the daisyUI plugin. This combination allowed my team and me to create a user-friendly, aesthetically pleasing website, without relying on JavaScript, and with both style and dynamic interaction handled seamlessly.

## Screenshots of the current state

  <img src="https://github.com/phdametyildiz/open_science_2024_beta/assets/135551114/1a9ee9eb-8743-4924-a68e-722d0ba132e8" width="300">
  
  <img src="https://github.com/phdametyildiz/open_science_2024_beta/assets/135551114/07063721-1f89-4c44-8d82-02c6f31eed79" width="300">
  
  <img src="https://github.com/phdametyildiz/open_science_2024_beta/assets/135551114/d0b1b1f5-77d3-4e93-82e3-822670730c34" width="300">

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
