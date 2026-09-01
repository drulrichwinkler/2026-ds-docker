# log_tool mit Datenbank-Anbindung.
FROM python:3.13-slim

WORKDIR /app

# Erst die Abhängigkeiten (ändern sich selten -> guter Cache),
# dann den Code.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY log_tool.py .

ENTRYPOINT ["python", "log_tool.py"]
