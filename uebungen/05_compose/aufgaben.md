---
art: Aufgabe
titel: "Übung 05 – Docker Compose"
modul: "3IT-VSIT-50 · Verteilte Systeme und Internet der Dinge"
thema: "Docker: mehrere Dienste deklarativ starten"
dozent: "Dr. Ulrich Winkler"
semester: "5. Semester · Informationstechnik"
---

**Vorlesung:** Deck *docker-compose*
**Ziel:** Den kompletten Stack aus Übung 04 (Datenbank, Adminer, `log_tool`) mit
**einer** Konfigurationsdatei und **einem** Befehl starten – statt vieler langer
`docker run`-Aufrufe.

## Kontext

In Übung 04 haben Sie Netzwerk, Datenbank, Adminer und `log_tool` einzeln von Hand
gestartet. **Docker Compose** beschreibt denselben Aufbau **deklarativ** in einer
Datei `compose.yaml`: welche Dienste es gibt, welche Images, welche Umgebungs-
variablen, welche Volumes. Das gemeinsame Netzwerk legt Compose automatisch an;
die Dienste erreichen sich über ihren Dienstnamen (`db`, `adminer`).

Sehen Sie sich die mitgelieferte `compose.yaml` an. Der Dienst `log_tool` steht in
einem **Profil** `werkzeug`, damit er nicht dauerhaft mitläuft, sondern nur auf
Abruf gestartet wird.

## Aufgabenstellung

1. Starten Sie den Stack im Hintergrund. Prüfen Sie mit `docker compose ps`, welche
   Dienste laufen.
2. Öffnen Sie Adminer (Port 8080) und melden Sie sich an (Server `db`).
3. Fügen Sie mit dem `log_tool`-Dienst zwei Einträge hinzu und listen Sie sie.
4. Sehen Sie sich die Logs der Datenbank an (`docker compose logs db`).
5. Fahren Sie den Stack herunter (`down`). Starten Sie ihn erneut – die Einträge
   sind dank Volume noch da. Vergleichen Sie mit `down -v` (löscht das Volume).

> Tipp: `docker compose up -d` baut fehlende Images automatisch. Nach Änderungen am
> `Dockerfile`/Code hilft `docker compose build` bzw. `--build`.

## Musterlösung

```bash
cd uebungen/05_compose

# 1) Stack starten (db + adminer). log_tool ist im Profil "werkzeug" und läuft
#    hier NICHT dauerhaft mit.
docker compose up -d
docker compose ps

# 2) Adminer im Browser (Port 8080): System=PostgreSQL, Server=db,
#    Benutzer=logger, Passwort=geheim123, Datenbank=logbuch

# 3) log_tool auf Abruf ausführen (baut beim ersten Mal das Image):
docker compose run --rm log_tool add "Compose macht das Leben leichter"
docker compose run --rm log_tool add "Zweiter Eintrag"
docker compose run --rm log_tool list

# 4) Datenbank-Logs
docker compose logs db

# 5) Stoppen und erneut starten -> Daten bleiben (Volume pgdaten):
docker compose down
docker compose up -d
docker compose run --rm log_tool list      # Einträge sind noch da

# Alles inklusive Daten entfernen:
docker compose down -v
```

**Was Sie gelernt haben:** Eine `compose.yaml` beschreibt den ganzen Stack an einer
Stelle; `up`/`down` starten und stoppen alles gemeinsam; das Netzwerk entsteht
automatisch; Profile trennen dauerhafte Dienste von Abruf-Werkzeugen. Ein Problem
bleibt: Das DB-Passwort steht im Klartext in der Datei – das lösen wir in Übung 06.
