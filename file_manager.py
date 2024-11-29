import os
import time
import shutil
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import sys

# Konfiguration
CONFIG = {
    'watch_folder': str(Path.home() / 'Downloads'),  # Zu überwachender Ordner
    'destination_root': str(Path.home() / 'Downloads' / 'Sorted'),  # Zielordner für sortierte Dateien
    'file_types': {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
        'audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'video': ['.mp4', '.avi', '.mkv', '.mov'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }
}

# Logging einrichten
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_file_category(file_path: str) -> str:
    """Bestimme die Kategorie einer Datei basierend auf ihrer Erweiterung."""
    file_ext = Path(file_path).suffix.lower()
    
    for category, extensions in CONFIG['file_types'].items():
        if file_ext in extensions:
            return category
    return 'misc'

def process_file(file_path: str) -> None:
    """Verarbeite eine einzelne Datei."""
    try:
        file_path = Path(file_path)
        if not file_path.exists():
            return

        # Überspringe den Sorted-Ordner selbst
        if 'Sorted' in file_path.parts:
            return

        category = get_file_category(file_path)
        destination_folder = Path(CONFIG['destination_root']) / category
        destination_folder.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{timestamp}_{file_path.name}"
        destination_path = destination_folder / new_filename

        shutil.move(str(file_path), str(destination_path))
        logger.info(f'Datei verschoben: {file_path.name} -> {category}/{new_filename}')

    except Exception as e:
        logger.error(f'Fehler beim Verarbeiten von {file_path}: {str(e)}')

def scan_directory() -> None:
    """Scanne das Verzeichnis nach neuen Dateien."""
    watch_folder = Path(CONFIG['watch_folder'])
    if not watch_folder.exists():
        logger.error(f"Überwachter Ordner existiert nicht: {watch_folder}")
        return

    for file_path in watch_folder.glob('*'):
        if file_path.is_file():
            process_file(str(file_path))

def main() -> None:
    """Hauptfunktion des Programms."""
    logger.info(f'Datei-Manager gestartet. Überwache: {CONFIG["watch_folder"]}')
    logger.info(f'Sortierte Dateien werden nach: {CONFIG["destination_root"]} verschoben')
    
    try:
        while True:
            scan_directory()
            time.sleep(2)  # Alle 2 Sekunden scannen
    except KeyboardInterrupt:
        logger.info('Datei-Manager beendet.')

if __name__ == "__main__":
    main() 