#!/usr/bin/env bash
# Wird einmalig nach dem Bau des Dev-Containers ausgeführt.
# Startet Portainer als "Beobachtungsfenster": eine Web-Oberfläche, in der Sie
# jeden Container, jedes Volume und jedes Netzwerk sehen, das Sie in den Übungen
# per Kommandozeile anlegen.
set -euo pipefail

echo "==> Warte auf Docker-Daemon"
for i in $(seq 1 30); do
  if docker info >/dev/null 2>&1; then break; fi
  sleep 1
done

echo "==> Starte Portainer (Docker-Oberfläche auf Port 9000)"
docker volume create portainer_data >/dev/null 2>&1 || true
if [ -z "$(docker ps -aq -f name=^portainer$)" ]; then
  docker run -d \
    --name portainer \
    --restart=unless-stopped \
    -p 9000:9000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce:latest >/dev/null
else
  docker start portainer >/dev/null 2>&1 || true
fi

echo
echo "==> Fertig. Docker-Version:"
docker --version
echo
cat <<'HINWEIS'
------------------------------------------------------------------------
Portainer läuft auf Port 9000 (Reiter "Ports" -> 9000 öffnen).

  WICHTIG: Beim ERSTEN Öffnen legen Sie innerhalb von ca. 5 Minuten ein
  Admin-Passwort an. Verpassen Sie das Zeitfenster, sperrt sich Portainer
  aus Sicherheitsgründen. Dann einfach neu starten:

      docker restart portainer

Loslegen:  cat README.md   und dann  uebungen/01_python_in_docker/aufgaben.md
------------------------------------------------------------------------
HINWEIS
