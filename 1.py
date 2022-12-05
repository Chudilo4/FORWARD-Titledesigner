import os
import re
import datetime
import argparse
import logging
from pathlib import Path

logging.basicConfig(level='INFO')  # Задаём уровень логирования
logger = logging.getLogger()


def parser():
    pars = argparse.ArgumentParser(
        description='Указать файл расписания для создания задания в титрах'
    )
    pars.add_argument('file',
                      metavar='file - Передать путь до файла ',
                      type=str,)
    args = pars.parse_args()
    return args.file


def main():
    try:
        file = parser()
        with open(file, encoding='windows-1251', mode='r') as f:
            path_file = f'log {datetime.datetime.now()}.txt'
            path = Path(os.getcwd(), path_file)
            path.replace('\\', '/')
            print(path)
            with open(f"{path}", encoding='windows-1251', mode='w') as f3:
                for line in f:
                    r = re.findall(r'D:\\ЭФИР\\.*', line)
                    r2 = re.findall(r'(?<=\\ЭФИР)\\.*', line)
                    if r and r2:
                        f3.write(r[0] + f' |D:\Титры{r2[0]}' + '\n')
        logger.info('Файл сформирован')
        logger.info(path)
    except FileNotFoundError:
        logger.info('Файла либо нет либо указан не правильно!')


if __name__ == '__main__':
    main()

