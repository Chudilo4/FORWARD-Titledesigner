import os
import re
import datetime
import argparse
import logging
from pathlib import Path, PureWindowsPath

logging.basicConfig(level='INFO')  # Задаём уровень логирования
logger = logging.getLogger()


def main():
    try:
        path_to_file = str(input("Введите путь до файла: "))
        with open(path_to_file, encoding='windows-1251', mode='r') as f:
            path_file = f'log {str(datetime.datetime.now())}'
            with open(f"{path_file}", encoding='windows-1251', mode='w') as f3:
                for line in f:
                    r = re.findall(r'D:\\ЭФИР\\.*', line)
                    r2 = re.findall(r'(?<=\\ЭФИР)\\.*', line)
                    if r and r2:
                        f3.write(r[0] + f' |D:\Титры{r2[0]}' + '\n')
        logger.info('Файл сформирован')
        logger.info(os.path.join(os.getcwd(), path_file))
    except FileNotFoundError:
        logger.info('Файла либо нет либо указан не правильно!')


if __name__ == '__main__':
    main()

