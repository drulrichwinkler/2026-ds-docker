#!/usr/bin/env python3
"""log_tool – winziges Logbuch, jetzt in einer echten Datenbank (PostgreSQL).

    python log_tool.py add "Nachricht"   # Eintrag in die DB schreiben
    python log_tool.py list              # alle Einträge anzeigen

Die Verbindungsdaten kommen aus Umgebungsvariablen. Das Passwort wird – wenn
vorhanden – aus der Datei in DB_PASSWORD_FILE gelesen (Docker Secret),
andernfalls aus DB_PASSWORD. So funktioniert dasselbe Skript in allen Übungen
von 04 bis zum Capstone.
"""
import os
import sys

import psycopg


def passwort() -> str:
    datei = os.environ.get("DB_PASSWORD_FILE")
    if datei and os.path.exists(datei):
        with open(datei, encoding="utf-8") as f:
            return f.read().strip()
    return os.environ.get("DB_PASSWORD", "")


def verbinden() -> psycopg.Connection:
    return psycopg.connect(
        host=os.environ.get("DB_HOST", "db"),
        dbname=os.environ.get("DB_NAME", "logbuch"),
        user=os.environ.get("DB_USER", "logger"),
        password=passwort(),
    )


def tabelle_anlegen(conn: psycopg.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            id        SERIAL PRIMARY KEY,
            ts        TIMESTAMPTZ NOT NULL DEFAULT now(),
            nachricht TEXT NOT NULL
        )
        """
    )
    conn.commit()


def add(nachricht: str) -> None:
    with verbinden() as conn:
        tabelle_anlegen(conn)
        conn.execute("INSERT INTO logs (nachricht) VALUES (%s)", (nachricht,))
        conn.commit()
    print(f"gespeichert: {nachricht}")


def liste() -> None:
    with verbinden() as conn:
        tabelle_anlegen(conn)
        for id_, ts, nachricht in conn.execute(
            "SELECT id, ts, nachricht FROM logs ORDER BY id"
        ):
            print(f"{id_:>3}  {ts:%Y-%m-%d %H:%M:%S}  {nachricht}")


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
