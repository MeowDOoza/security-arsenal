import socket
import argparse
import sys
from datetime import datetime
def check_port(ip, port):
    try:
        # Создаем сокет: AF_INET (IPv4), SOCK_STREAM (TCP)
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)  # Повышаем скорость: полсекунды на порт

        # Попытка соединения
        result = scanner.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Порт {port:<5} | СТАТУС: ОТКРЫТ")

        scanner.close()
    except KeyboardInterrupt:
        print("\n[!] Сканирование прервано пользователем.")
        sys.exit()
    except socket.error:
        print("[-] Ошибка соединения с сервером.")
        sys.exit()


def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description="Professional TCP Port Scanner v1.0")
    parser.add_argument("target", help="IP адрес или домен цели")
    parser.add_argument("-p", "--ports", help="Список портов через запятую (например: 80,443)", type=str)

    args = parser.parse_args()
    target_ip = args.target

    # Определяем список портов для проверки
    if args.ports:
        ports_to_scan = [int(p) for p in args.ports.split(",")]
    else:
        # Стандартный набор, если порты не указаны
        ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
    print("-" * 50)
    print(f"[*] СКАНИРОВАНИЕ ЦЕЛИ: {target_ip}")
    print(f"[*] ВРЕМЯ НАЧАЛА: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    for port in ports_to_scan:
        check_port(target_ip, port)
    print("-" * 50)
    print("[*] Сканирование завершено.")
if __name__ == "__main__":
    main()