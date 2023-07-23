import serial
import os

width, _ = os.get_terminal_size()


def main(port: str, baudrate: int = 115200):
    with serial.Serial(port, baudrate) as connection:
        while True:
            try:
                output = connection.readline().decode().strip()
                if output == '':
                    continue
                print()
                print(connection.readline().decode().strip())
                print()
                print('-' * width)
            except:
                pass


if __name__ == '__main__':
    try:
        main(input("Serial Port? "))
    except KeyboardInterrupt:
        exit(0)
