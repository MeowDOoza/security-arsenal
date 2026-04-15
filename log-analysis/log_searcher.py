import time

def log_searcher(input_file, output_file, keywords):
    start_time = time.time()
    count = 0

    # Приводим ключевые слова к нижнему регистру один раз заранее
    target_words = [w.lower() for w in keywords]

    print(f"[*] Поиск запущен. Цель: {input_file}")

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f_in, \
                open(output_file, 'w', encoding='utf-8') as f_out:

            for line_num, line in enumerate(f_in, 1):
                # Ищем без учета регистра
                lower_line = line.lower()

                if any(word in lower_line for word in target_words):
                    f_out.write(f"[L:{line_num}] {line}")
                    count += 1

                # Принт оставим только один, чтобы видеть, что процесс идет
                if line_num % 1000000 == 0:
                    print(f"[*] Обработано {line_num // 1000000} млн строк...")

    except FileNotFoundError:
        print("[!] Файл не найден.")
        return

    print(f"[+] Готово! Найдено: {count}. Время: {round(time.time() - start_time, 2)} сек.")

if __name__ == "__main__":
    # Настраивай здесь:
    search_keywords = ["ERROR", "failed", "critical"]
    log_searcher("access.log", "report.txt", search_keywords)
"""
ТЕХНИЧЕСКИЙ ПАСПОРТ ИНСТРУМЕНТА: Log Searcher (Stream Edition)

1. НАЗНАЧЕНИЕ:
Поиск критических событий в текстовых массивах данных (логи, дампы баз данных) 
объемом от 1 до 100+ Гб.

2. ПРИНЦИП РАБОТЫ (МЕХАНИКА):
- Итератор: Скрипт использует генератор строк `for line in f_in`. Это значит, 
  что в RAM одновременно находится только ОДНА строка файла. Потребление памяти 
  стабильно низкое (10-50 Мб).
- Case-Insensitive: Метод `.lower()` применяется к текущей строке в памяти, 
  что позволяет находить совпадения независимо от регистра (Error = ERROR).
- Errors Ignore: Параметр `errors='ignore'` при открытии файла предотвращает 
  падение скрипта при встрече невалидных UTF-8 символов (бинарные данные).

3. ИНСТРУКЦИЯ ПО ЭКСПЛУАТАЦИИ:
- Поместить лог-файл в одну директорию со скриптом.
- Отредактировать список `SEARCH_WORDS` в блоке __main__.
- Запустить через терминал: `python3 log_searcher.py`.
- Результат будет сохранен в файл отчета с указанием номера строки оригинала.
"""
