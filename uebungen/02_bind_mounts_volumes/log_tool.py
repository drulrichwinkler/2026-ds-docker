#!/usr/bin/env python3
"""log_tool – winziges Logbuch auf der Kommandozeile (Datei-Variante).

    python log_tool.py add "Nachricht"   # Eintrag anhängen
    python log_tool.py list              # alle Einträge anzeigen

Die Einträge landen in einer Textdatei. Wo genau, steht in LOG_FILE
(Voreinstellung: /data/log.txt). In dieser Übung mounten wir den Code per
Bind Mount in den Container und die Datei in ein Volume – so überleben die
Einträge das Löschen des Containers.
"""
import os
import sys
from datetime import datetime

LOG_FILE = os.environ.get("LOG_FILE", "/data/log.txt")


def add(nachricht: str) -> None:
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    zeitstempel = datetime.now().isoformat(timespec="seconds")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{zeitstempel}\t{nachricht}\n")
    print(f"gespeichert: {nachricht}")


def liste() -> None:
    if not os.path.exists(LOG_FILE):
        print("(noch keine Einträge)")
        return
    with open(LOG_FILE, encoding="utf-8") as f:
        print(f.read(), end="")


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "add":
        add(" ".join(sys.argv[2:]))
    elif len(sys.argv) == 2 and sys.argv[1] == "list":
        liste()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
