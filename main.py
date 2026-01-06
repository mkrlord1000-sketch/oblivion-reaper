#!/usr/bin/env python3
"""
OBLIVION REAPER v1.0 - CYBER GUARDIAN SYSTEM
Главный файл приложения.
"""

import asyncio
import sys
import os

# Добавляем путь для импорта локальных модулей
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """Точка входа в приложение"""
    print("=" * 60)
    print("OBLIVION REAPER v1.0 - CYBER GUARDIAN SYSTEM")
    print("=" * 60)
    print("\nСистема инициализирована.")
    print("Для работы приложения требуется настройка.")
    print("\nПроверка зависимостей...")
    
    # Проверка основных библиотек
    try:
        import telethon
        print(f"✅ Telethon {telethon.__version__}")
    except ImportError:
        print("❌ Telethon не установлен")
        return
    
    try:
        import cryptography
        print("✅ Cryptography")
    except ImportError:
        print("❌ Cryptography не установлена")
        return
    
    print("\n✅ Все зависимости установлены.")
    print("\nПриложение готово к настройке.")
    print("Запустите: python setup.py")

if __name__ == "__main__":
    main()
