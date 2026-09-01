---
art: Information
titel: "Docker – Übungen"
modul: "3IT-VSIT-50 · Verteilte Systeme und Internet der Dinge"
thema: "Container, Images, Netzwerke, Compose, Secrets"
dozent: "Dr. Ulrich Winkler"
semester: "5. Semester · Informationstechnik"
---

# Docker – Übungen

Übungen zur Docker-Vorlesung (5. Semester, Studiengang Informationstechnik,
DHSN Dresden). Sie lernen Docker praktisch kennen – vom ersten Container bis zu
einem kompletten Stack aus Python-Anwendung und Datenbank. Gleichzeitig ist dies
eine **Vorbereitung auf die kommenden Python-Kurse**: Der rote Faden ist ein
kleines Python-Werkzeug, das Sie Schritt für Schritt containerisieren.

Die Aufgaben sind **unbewertet**. Arbeiten Sie in Ihrem eigenen Tempo und
probieren Sie ruhig Dinge aus, die über die Anleitung hinausgehen.

## Wie Sie arbeiten

### GitHub Codespaces (empfohlen – nichts zu installieren)

Der einfachste Weg, besonders unter **Windows**. Sie brauchen keinerlei lokale
Installation; alles läuft im Browser.

1. Auf **Code → Codespaces → Create codespace on main** klicken.
2. Warten, bis der Container gebaut ist (beim ersten Mal einige Minuten).
3. Fertig. Docker läuft im Container (*Docker-in-Docker*), Terminal und Editor
   sind sofort einsatzbereit.

### Lokal in VS Code (optional)

- **macOS / Linux:** [VS Code](https://code.visualstudio.com/), die Erweiterung
  **Dev Containers** und [Docker](https://www.docker.com/) installieren. Repo
  klonen, in VS Code öffnen und bei der Nachfrage **Reopen in Container** wählen.
- **Windows:** Nutzen Sie **WSL2** mit Docker Desktop. Ohne WSL2/Docker Desktop
  können Sie lokal kein Docker ausführen – dann nehmen Sie bitte Codespaces.

> **Wichtig:** Man installiert Docker **nicht**, indem man ein Ubuntu-Image lädt.
> Das Ubuntu-Image in Übung 01 ist *Übungsinhalt*, keine Installationsmethode.
> Docker selbst kommt aus Codespaces bzw. Docker Desktop / WSL2.

## Portainer – Ihr Beobachtungsfenster

Nach dem Start läuft **Portainer**, eine Web-Oberfläche für Docker, auf Port
**9000**. Öffnen Sie im Reiter **Ports** den Port 9000. Dort sehen Sie live jeden
Container, jedes Volume und jedes Netzwerk, das Sie in den Übungen anlegen.

> **Achtung, Erst-Login:** Beim allerersten Öffnen müssen Sie **innerhalb von ca.
> 5 Minuten** ein Admin-Passwort vergeben. Verpassen Sie das Zeitfenster, sperrt
> sich Portainer aus Sicherheitsgründen. Starten Sie es dann einfach neu:
>
> ```bash
> docker restart portainer
> ```

## Aufbau

```
uebungen/
├── 01_python_in_docker/          Erster Container, Python-Image, flüchtige Änderungen
├── 02_bind_mounts_volumes/       Code live rein (Bind Mount), Daten sichern (Volume)
├── 03_image_und_env/             Eigenes Image (Dockerfile), Konfiguration per Env
├── 04_netzwerk_und_db/           Docker-Netzwerk, PostgreSQL + Adminer
├── 05_compose/                   Denselben Stack deklarativ mit Docker Compose
├── 06_secrets/                   Passwörter richtig behandeln (Secrets statt Env)
├── 07_capstone/                  Alles zusammen: log_tool + Postgres + Adminer
└── 08_selbststudium_swarm_sandboxes/   Recherche: Docker Swarm & AI Sandboxes
```

Jede Übung enthält eine `aufgaben.md` (mit Aufgabenstellung **und** Musterlösung)
sowie – wo nötig – Startdateien. Beginnen Sie mit
`uebungen/01_python_in_docker/aufgaben.md`.

## Werkzeuge im Überblick

| Werkzeug   | Wozu                                   | Ab Übung |
|------------|----------------------------------------|----------|
| Portainer  | Docker per Weboberfläche beobachten    | 01       |
| PostgreSQL | Datenbank im Docker-Netzwerk           | 04       |
| Adminer    | schlanke Web-Oberfläche für die DB     | 04       |
| `log_tool` | kleines Python-CLI (schreibt Log-DB)   | 02       |
