---
art: Vorbereitung
titel: "Übung 08 – Selbststudium: Docker Swarm & AI Sandboxes"
modul: "3IT-VSIT-50 · Verteilte Systeme und Internet der Dinge"
thema: "Ausblick: Container über einen Rechner hinaus"
dozent: "Dr. Ulrich Winkler"
semester: "5. Semester · Informationstechnik"
---

**Vorlesung:** Ausblick (baut auf *docker-compose* auf)
**Ziel:** Sich zwei weiterführende Docker-Themen **selbstständig** über die offizielle
Dokumentation erschließen und einordnen: **Docker Swarm** (Container über mehrere
Rechner hinweg) und **Docker AI Sandboxes** (isolierte Umgebungen für KI-Agenten).

Dies ist ein **Entdecken-Blatt**: Es gibt keine Musterlösung. Recherchieren Sie in
der Dokumentation und beantworten Sie die Leitfragen **stichpunktartig mit eigenen
Worten**. Wo möglich, probieren Sie einen Befehl im Dev-Container aus.

<!-- raw-typst #hinweis(titel: "Quellen")[Docker Swarm: #link("https://docs.docker.com/engine/swarm/")[docs.docker.com/engine/swarm] · Docker AI Sandboxes: #link("https://docs.docker.com/ai/sandboxes/")[docs.docker.com/ai/sandboxes]] -->

## Teil A – Docker Swarm

Lesen Sie den Einstieg unter *docs.docker.com/engine/swarm/*.

1. Compose startet Container auf **einem** Rechner. Welches Problem löst der
   **Swarm mode** darüber hinaus? Was ist ein „Swarm"?
2. Erklären Sie den Unterschied zwischen einem **Manager-Node** und einem
   **Worker-Node**.
3. Was ist im Swarm ein **Service**, was eine **Task**, und was bedeutet die Anzahl
   der **Replicas**? Wie hängt das mit **Skalierung** zusammen?
4. Der Manager sorgt für „**desired state reconciliation**". Beschreiben Sie in
   einem Satz, was das heißt (Beispiel: ein Container stürzt ab – was passiert?).
5. Wozu dient ein **Overlay-Netzwerk**, und wie finden sich Dienste im Swarm
   (Stichwort **Service Discovery**, eingebauter DNS)?
6. Ordnen Sie zu: Welche Konzepte kennen Sie schon aus Compose (Übung 05/06),
   welche kommen im Swarm **neu** hinzu?
7. **Optional (im Dev-Container):** Initialisieren Sie einen Ein-Knoten-Swarm und
   deployen Sie einen Service mit mehreren Replicas. Nutzen Sie dazu die
   Befehle aus der Doku (`docker swarm init`, `docker service create --replicas ...`,
   `docker service ls`, `docker service ps`, `docker service scale`). Notieren Sie,
   was Sie beobachten. Am Ende `docker swarm leave --force`.

## Teil B – Docker AI Sandboxes

Lesen Sie *docs.docker.com/ai/sandboxes/*.

8. Was ist eine **Docker Sandbox**, und für wen bzw. was ist sie gedacht
   (Stichwort **KI-Coding-Agenten**)?
9. Jede Sandbox erhält „ihren eigenen Docker-Daemon, ihr Dateisystem und ihr
   Netzwerk". Warum ist diese **Isolation** gerade bei automatisch handelnden
   Agenten wichtig?
10. Womit werden Sandboxes gesteuert (Stichwort **`sbx`-CLI**)? Nennen Sie den
    Startbefehl aus der Doku.
11. Was ist der Unterschied zwischen einer **Sandbox** und einem gewöhnlichen
    Container bzw. einem Compose-Stack, wie Sie ihn in Übung 07 gebaut haben?
12. Wozu dient das **MCP Gateway** im Zusammenhang mit Agenten?

## Zum Abschluss

13. Skizzieren Sie in drei bis vier Sätzen die Spannweite, die Sie in diesem Kurs
    kennengelernt haben: vom **einzelnen Container** (Übung 01) über den
    **Compose-Stack auf einem Rechner** (Übung 05–07) bis zum **verteilten Betrieb
    im Swarm** und der **isolierten Agenten-Sandbox**. Wo würden Sie welches
    Werkzeug einsetzen?

<!-- raw-typst #kasten(titel: "Hinweis zur Bearbeitung")[Stichpunkte genügen. Ziel ist, dass Sie die Begriffe einordnen und die offizielle Dokumentation als Nachschlagewerk nutzen können – nicht, dass Sie sie auswendig lernen.] -->
