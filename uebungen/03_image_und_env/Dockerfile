# Eigenes Image für das log_tool.
# Ein Image entsteht Schicht für Schicht (Layer). Jede Anweisung hier erzeugt
# eine neue Schicht; Docker kann unveränderte Schichten zwischenspeichern.

FROM python:3.13-slim

# Arbeitsverzeichnis im Image
WORKDIR /app

# Nur den Code hineinkopieren (Daten kommen später aus einem Volume)
COPY log_tool.py .

# Voreinstellung: Log-Datei liegt unter /data (per Volume einhängbar).
# Kann beim Start mit -e LOG_FILE=... überschrieben werden.
ENV LOG_FILE=/data/log.txt

# Standardbefehl: zeigt die Hilfe. In der Übung hängen wir add/list an.
ENTRYPOINT ["python", "log_tool.py"]
