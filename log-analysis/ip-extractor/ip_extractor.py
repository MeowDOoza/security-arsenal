
# ИНСТРУМЕНТ: IP Extractor (v1.0)
# НАЗНАЧЕНИЕ: Автоматический поиск и извлечение уникальных IPv4 адресов из текста или файлов.
# КОНТЕКСТ: Используется в задачах форензики, анализа логов (SIEM, веб-серверы) и OSINT.
# КАК ПОЛЬЗОВАТЬСЯ:
# 1. Анализ текста: python3 ip_extractor.py "твой текст"
# 2. Анализ файла: python3 ip_extractor.py путь/к/файлу.log
# 3. Сохранение результата в файл: python3 ip_extractor.py файл.log > result.txt(или другое название файла который нужен для отчета)
import re
import sys
import os

# Регулярное выражение для поиска IPv4.
# Использует non-capturing group (?) для корректного извлечения всего адреса.
ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}'

# Входной блок: поддержка прямого ввода текста или пути к файлу
if len(sys.argv) > 1:
    path_or_text = sys.argv[1]

    # Если аргумент — существующий файл, считываем его содержимое
    if os.path.isfile(path_or_text):
        with open(path_or_text, 'r') as f:
            input_text = f.read()
            print(f"[*] Анализ источника: {path_or_text}")
    else:
        # В ином случае обрабатываем аргумент как сырую строку
        input_text = path_or_text
else:
    print("[-] Ошибка: Отсутствуют входные данные (текст или файл).")
    sys.exit()

# Извлечение уникальных адресов через множество (set) для исключения дублей
found_ips = set(re.findall(ip_pattern, input_text))

# Вывод результатов в стандартный поток (stdout)
for ip in found_ips:
    print(f"[+] Найден IP: {ip}")