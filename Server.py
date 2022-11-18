import socket

UDP_MAX_SIZE = 65535
members = []


def listen(host: str = 'localhost', port=55511):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((host, port))
    print(f'Запуск на {host}:{port}')

    while True:
        try:
            msg, addr = s.recvfrom(UDP_MAX_SIZE)
        except ConnectionResetError:
            members.remove(addr)
            continue
        finally:
            if addr not in members:
                members.append(addr)

            if not msg:
                continue
            user_id = addr[1]
            try:
                if '__join' in msg.decode('utf-8'):
                    print(f'Клиент {msg.decode("utf-8").replace("__join", "")} подключился!')
                    print(*members)
                    continue
            except AttributeError:
                continue
            else:
                msg = f'{msg.decode("utf-8")}'

                for member in members:
                    if member == addr:
                        continue
                    s.sendto(f"[{user_id}]{msg}".encode('utf-8'), member)


if __name__ == '__main__':
    listen()
