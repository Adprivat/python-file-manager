# Automatischer Datei-Manager

Ein Python-Skript zur automatischen Sortierung und Organisation von Dateien.

## Features

- Automatische Überwachung des Download-Ordners
- Sortierung nach Dateitypen (Bilder, Dokumente, Audio, Video, Archive)
- Automatische Umbenennung mit Zeitstempel
- Logging aller Aktivitäten
- Konfigurierbare Ordner und Dateitypen

## Installation

1. Klone das Repository:
2. Installiere die benötigten Pakete

## Verwendung

1. Starte das Skript:
2. 
python file_manager.py


3. Der Manager überwacht nun automatisch den Download-Ordner und sortiert neue Dateien in die entsprechenden Kategorien:
   - Bilder (jpg, jpeg, png, gif, bmp)
   - Dokumente (pdf, doc, docx, txt, xls, xlsx)
   - Audio (mp3, wav, flac, m4a)
   - Video (mp4, avi, mkv, mov)
   - Archive (zip, rar, 7z, tar, gz)

4. Sortierte Dateien werden in den `~/Sorted` Ordner verschoben und nach Kategorien organisiert.

5. Beende das Programm mit `Ctrl+C`

## Konfiguration

Die Standardkonfiguration kann in der `CONFIG`-Variable im Skript angepasst werden:
- `watch_folder`: Zu überwachender Ordner
- `destination_root`: Zielordner für sortierte Dateien
- `file_types`: Dateitypen und ihre Kategorien

## Logs

Das Programm protokolliert alle Aktivitäten mit Zeitstempel. Die Logs werden in der Konsole angezeigt. 
