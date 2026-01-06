[app]
# Основные настройки
title = Oblivion Reaper
package.name = oblivionreaper
package.domain = org.cyber
version = 1.0.0
source.dir = .
source.main = main.py

# Включаемые файлы
source.include_exts = py,png,jpg,json,txt

# Требования (ВСЕ необходимые библиотеки)
requirements = 
    python3,
    kivy==2.3.0,
    telethon==1.34.0,
    cryptography==42.0.0,
    colorama==0.4.6,
    pyfiglet==0.8.post1,
    aiofiles==23.2.1

# Настройки Android
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
android.minapi = 21
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Графические настройки
orientation = portrait
fullscreen = 0
log_level = 2

[buildozer]
# Настройки Buildozer
log_level = 2
warn_on_root = 1
