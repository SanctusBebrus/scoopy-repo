import socket
import threading

UDP_MAX_SIZE = 65535


def listen(s: socket.socket):
    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('utf-8') + '\n' + f'вы: ', end='')


def connect(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    s.send(f'__join{NAME}'.encode('utf-8'))

    while True:
        msg = input(f'вы: ')
        s.send(f'{NAME}: {msg}'.encode('utf-8'))


if __name__ == '__main__':
    NAME = input('Имя пользователя: ')
    print(f'Добро пожаловать, {NAME}!')
    connect()
