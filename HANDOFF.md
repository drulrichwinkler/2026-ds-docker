# HANDOFF — Übungs-Repo „Docker" (`2026-ds-docker`)

Auftrag an einen Coding-Agenten: Baue in **diesem Repo** ein Docker-Übungs-Repo für
Studierende. Alle Entscheidungen unten sind in einer Grill-Session mit dem Dozenten
festgelegt worden — **nicht neu verhandeln**, einfach umsetzen. Bei echten Lücken:
sinnvollen Default nehmen und im PR/Commit anmerken.

---

## 0. Kontext (wichtig für Ton & Stil)

- **Kurs:** Duale Hochschule Sachsen (DHSN), Staatliche Studienakademie Dresden,
  Studiengang Informationstechnik, 5. Semester. Modul (verifizieren, wie im
  Schwester-Repo): `3IT-VSIT-50 · Verteilte Systeme und Internet der Dinge`.
  Dozent: **Dr. Ulrich Winkler**.
- **Schwester-Repos** (gleiche Machart, als Vorbild ansehen):
  - `/Users/uw/work/vorlesungen/iot/git/2026-distributed-systems-git/` — Struktur,
    `.devcontainer/`, `uebungen/NN_thema/aufgaben.md`, `README.md`.
  - `/Users/uw/work/vorlesungen/iot/python/2026-distributed-systems-python/` — Devcontainer.
- **Anrede: durchgehend siezen** („Sie", „Legen Sie an …"). Deutsch.
- **Flipped Classroom, Aufgaben UNBEWERTET.** Kein Prüfungscharakter.
- **Ziel des Kurses:** Docker praktisch lernen — und als **Vorbereitung auf die
  kommenden Python-Kurse**. Roter Faden: ein kleines Python-Tool, das schrittweise
  containerisiert wird und am Ende mit einer Postgres-DB im Docker-Netz spricht.

## 1. Zielumgebung — wo Studierende arbeiten

- **Primär: GitHub Codespaces / Devcontainer** mit **Docker-in-Docker**. Null lokale
  Installation, läuft im Browser. Das ist der empfohlene Weg für ALLE, besonders Windows.
- **Optional lokal:** Mac/Linux mit Docker + „Reopen in Container"; Windows nur mit
  WSL2 / Docker Desktop (Nebenpfad, im README knapp erwähnen).
- **Klarstellen** (häufiges Missverständnis): Man installiert Docker NICHT per
  Ubuntu-Image. Das „Ubuntu-Image + Python installieren" ist **Übung 01 (Inhalt)**,
  keine Setup-Anleitung.

## 2. Grundform des Repos

Hybrid: **nummerierte Übungen** (`uebungen/NN_thema/`), deren spätere aufeinander
aufbauen und in einen **Capstone**-Stack münden (Python-CLI + Postgres + Compose +
Secrets), als Python-Modul-Vorbereitung. Umfang bewusst **schlank**.

---

## 3. Übungsliste (8 Stück)

Jede Übung: eigener Ordner `uebungen/NN_thema/` mit `aufgaben.md` (+ **Startdateien** +
**inline-Musterlösung**). Verweis auf das passende Keynote-Deck oben in der Datei
(Decks liegen unter `/Users/uw/work/vorlesungen/iot/2026/2026-09-01/*.key`:
`docker-basics`, `docker-data`, `docker-network`, `docker-compose`).

| Nr | Ordner | Thema | Kerninhalt |
|----|--------|-------|------------|
| 01 | `01_python_in_docker` | Python in Docker | `docker run hello-world`; `docker run -it ubuntu bash` + `apt install python3` → **Änderungen sind flüchtig** (Container weg = weg); dann offizielles `python:3.13-slim`-Image, Skript ausführen; `ps`, `exec`, `logs`. Portainer schon offen → beobachten. |
| 02 | `02_bind_mounts_volumes` | Bind Mounts + Volumes | `log_tool.py` per **Bind Mount** live in den Container (Host-Code editieren, im Container sofort wirksam); dann **Volume** für persistente Daten, Kontrast Bind Mount vs. Volume. |
| 03 | `03_image_und_env` | Eigenes Image + Env | **Dockerfile** fürs `log_tool` bauen (Layer-Konzept, `.dockerignore`); Konfiguration per `-e` / `--env-file` (z.B. DB-Host, DB-User). |
| 04 | `04_netzwerk_und_db` | Netzwerk + Datenbank | Eigenes Docker-**Netzwerk**; **Postgres**-Container + **Adminer** (DB-UI) starten; `log_tool` verbindet sich per Netzwerk-Alias mit Postgres. In Adminer die Tabelle ansehen. |
| 05 | `05_compose` | Docker Compose | Denselben Stack (`log_tool` + `postgres` + `adminer`) **deklarativ** in `compose.yaml`; `up`/`down`/`logs`; `depends_on`. |
| 06 | `06_secrets` | Secrets | DB-Passwort zuerst per Env → zeigen, dass es in `docker inspect` / `docker ps -e` **leakt** → auf **Compose file-based secrets** umstellen (`secrets:`, Quelle = Datei → `/run/secrets/…`). **Bonus/Ausblick:** kurz Docker-Swarm-Secrets (`docker secret create`) als Produktions-Mechanismus. |
| 07 | `07_capstone` | Capstone | Kompletter Stack via Compose: `log_tool` (CLI) + Postgres + Adminer + Portainer, DB-Passwort als Secret, Daten im Volume. End-to-end: `add` schreibt, `list` liest, sichtbar in Adminer & Portainer. |
| 08 | `08_selbststudium_swarm_sandboxes` | Selbststudium (entdecken) | **Reines Entdecken-Arbeitsblatt** (Web-Recherche, keine Musterlösung): Leitfragen zu **Docker Swarm** (Manager/Worker, Services, Replicas, Secrets im Swarm; https://docs.docker.com/engine/swarm/) und zu **Docker AI Sandboxes** (https://docs.docker.com/ai/sandboxes/ — was ist das, wofür, Abgrenzung zu Compose/Swarm). Vorher die Seite via WebFetch lesen und aktuelle Begriffe/Struktur übernehmen. |

### Capstone-App `log_tool` (Detail)

- Reines Python-CLI, **anfängertauglich** (kein Web-Framework), Treiber `psycopg` (v3).
- Interface: `python log_tool.py add "Nachricht"` und `python log_tool.py list`.
- Schema: Tabelle `logs(id serial primary key, ts timestamptz default now(), nachricht text)`.
- Config aus Env (`DB_HOST`, `DB_NAME`, `DB_USER`) + Passwort aus Secret-Datei
  `/run/secrets/db_password` (Fallback Env für die frühen Übungen).
- Startdatei `log_tool.py` wird mitgeliefert (Studierende sollen Docker lernen, nicht Python tippen).

---

## 4. Infrastruktur

### `.devcontainer/`
- `devcontainer.json`: Base `mcr.microsoft.com/devcontainers/base:bookworm`, Features:
  `ghcr.io/devcontainers/features/docker-in-docker`, `git`, `github-cli`. `remoteUser: vscode`.
  `forwardPorts` für Portainer (9000/9443), Adminer (8080), ggf. Postgres (5432).
  VS-Code-Extensions: Docker (`ms-azuretools.vscode-docker`).
  Vorbild: `../git/2026-distributed-systems-git/.devcontainer/`.
- `postCreate.sh`: startet **Portainer** als Beobachtungsfenster **ab Übung 01**:
  `docker volume create portainer_data` + `docker run -d -p 9000:9000 --name portainer
  -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`.
  **Portainer-Auth NICHT vorkonfigurieren** — Studierende setzen beim ersten Öffnen ihr
  eigenes Admin-Passwort. **README muss vor dem ~5-Minuten-Lockout warnen** (wenn nicht
  rechtzeitig gesetzt: `docker restart portainer`).

### `README.md`
- Einstieg, gesiezt: Was ist das Repo, Lernziele, wie loslegen.
- Codespaces-primär (Badge/Anleitung), lokaler Weg (Mac/Linux + Windows/WSL2) als Nebenpfad.
- Portainer öffnen (Port-Forward) + **Lockout-Hinweis**. Adminer-Zugang.
- Reihenfolge der Übungen.

### `.gitignore`
- Typst-Tooling: `lib.typ`, `*.typ`, `build.sh`, `assets/` (siehe §5 — **nur PDFs werden committet**).
- Echte Secrets: `**/db_password.txt`, `**/*.secret` (aber `*.example` committen!).
- `__pycache__/`, `*.pyc`, `.venv/`.
- **`*.pdf` NICHT ignorieren** — die gebauten Aufgaben-PDFs gehören ins Repo.

---

## 5. Typst → PDF Pipeline (alle `.md` zu PDF)

Anforderung: **jede `aufgaben.md` (und README.md) wird via Typst zu PDF gesetzt.**
Nur die **PDFs werden committet**; das Tooling bleibt gitignored (lokal vorhanden).

**Vorlage 1:1 wiederverwenden** aus `/Users/uw/work/vorlesungen/iot/vs-uebungen/`:
- `lib.typ` — rendert Markdown direkt via `@preview/cmarker:0.1.6`, liest YAML-Frontmatter,
  DHSN-Briefkopf. Funktion: `dhsn-material(quelle, art: …, titel: …, modul: …, thema: …,
  dozent: …, semester: …, logo: "assets/dhsn_logo.png")`. Metadaten kommen aus dem Frontmatter.
- `assets/dhsn_logo.png` — mitkopieren.
- Frontmatter-Beispiel (oben in jede `aufgaben.md`):
  ```yaml
  ---
  art: Aufgabe
  titel: "Übung 01 – Python in Docker"
  modul: "3IT-VSIT-50 · Verteilte Systeme und Internet der Dinge"
  thema: "Docker: Container-Grundlagen"
  dozent: "Dr. Ulrich Winkler"
  semester: "5. Semester · Informationstechnik"
  ---
  ```
- **`build.sh`** (gitignored): iteriert über alle `uebungen/**/aufgaben.md` + `README.md`,
  erzeugt pro Datei einen **temporären Wrapper-`.typ` im Repo-Root** (wo `lib.typ` +
  `assets/` liegen, damit der Logo-Pfad auflöst), Inhalt genau:
  ```typst
  #import "lib.typ": dhsn-material
  #dhsn-material("uebungen/01_python_in_docker/aufgaben.md", art: "Aufgabe")
  ```
  dann `typst compile <wrapper>.typ uebungen/01_python_in_docker/aufgaben.pdf`, Wrapper löschen.
  (Wrapper im Root, weil `lib.typ` das Logo relativ zum kompilierten `.typ` sucht.)
- Bilder in den `.md` möglichst vermeiden bzw. root-relativ referenzieren (cmarker löst
  Pfade relativ zum Wrapper = Root auf).
- `typst` 0.14+, `pandoc` vorhanden. `cmarker` wird via `@preview` automatisch geholt.

---

## 6. Konventionen für `aufgaben.md`

Gliederung wie im Git-Repo
(`../git/2026-distributed-systems-git/uebungen/01_erste_schritte/aufgaben.md` ansehen):

1. `# Übung NN – Titel`
2. **Vorlesung:** Verweis aufs Keynote-Deck.  **Ziel:** ein Satz.
3. `## Kontext` — worum geht's, Spielwiese.
4. `## Aufgabenstellung` — nummerierte Schritte, gesiezt.
5. `> Tipp:` — Hinweise.
6. `## Musterlösung` — **inline**, mit realen Befehlen in ```bash-Blöcken und erwarteter
   Ausgabe als Kommentar. (Musterlösung = einzige Erfolgskontrolle; keine separaten
   `pruefe.sh`, keine „Erwartetes Ergebnis"-Sektion.)

Übung 08 hat **keine** Musterlösung (Entdecken-Blatt, `art: "Vorbereitung"` im Frontmatter).

---

## 7. Bilder/Images & Pinning

Gepinnte Major-Tags: `postgres:17`, `adminer`, `portainer/portainer-ce`, `python:3.13-slim`.
Alle multi-arch (laufen auf ARM-Macs & amd64-Codespaces).

---

## 8. Abschluss

- Alles **lokal committen**, aber **nicht pushen** (Wunsch des Dozenten; Remote existiert:
  `github.com/drulrichwinkler/2026-ds-docker`).
- Es ist ein in `iot` verschachteltes Repo → gitlink-Hinweis beim äußeren Repo ist erwartet.
- Sinnvolle, kleine Commits (pro Übung / Infrastruktur-Baustein).

## 9. Akzeptanzkriterien

- [ ] `.devcontainer/` baut in Codespaces, Docker-in-Docker funktioniert, Portainer läuft nach `postCreate`.
- [ ] Alle 8 Übungsordner mit `aufgaben.md` (gesiezt, inline-Lösung außer 08) + Startdateien.
- [ ] Capstone (`07`) startet per `docker compose up` einen Stack, in dem `log_tool add/list`
      gegen Postgres läuft, Passwort als Secret, Daten im Volume, sichtbar in Adminer.
- [ ] `build.sh` erzeugt für jede `.md` ein `aufgaben.pdf` (DHSN-Layout); nur PDFs committet,
      Tooling gitignored.
- [ ] `README.md` inkl. Codespaces-/Lokal-Anleitung + Portainer-Lockout-Warnung, auch als PDF.
- [ ] Übung 08 spiegelt aktuelle Inhalte von docs.docker.com (Swarm + AI Sandboxes) — Seiten vorher abrufen.

## 10. NICHT Teil dieses Auftrags (separat/später)

- Aufgezeichnete `autodemo`/asciinema-Demos (kommen später, wenn die Übungen final sind).
- PDF-Export der Keynote-Decks (separater, offener Nebenschauplatz).
- Kein Pushen zum Remote.
