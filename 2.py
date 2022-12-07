import os
import re
import logging

logging.basicConfig(level='INFO')
logger = logging.getLogger()


def main():
    try:
        path_to_file = str(input("Введите путь до файла: "))
        with open(path_to_file, encoding='windows-1251', mode='r') as f:
            path_file = f'log {path_to_file[:-4]}.txt'
            with open(f"{path_file}", mode='w') as f3:
                b = ''
                for line in f:
                    r = re.findall(r'D:\\ЭФИР\\.*', line)
                    r2 = line.split('\\')
                    if r and r2[2] != 'Живая природа':
                        b += r[0] + f' |D:\Титры\{r2[-1][0:-4]}' + 'mov' '\n'
                f3.write(b)
        logger.info('Файл сформирован')
        logger.info(os.path.join(os.getcwd(), path_file))
    except FileNotFoundError:
        logger.info('Файла либо нет либо указан не правильно!')


if __name__ == '__main__':
    main()

