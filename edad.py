import argparse
import datetime


mensaje = '{0} cumplira 100 en el {1} felicidades'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('nombre')
    parser.add_argument('edad_actual')

    args = parser.parse_args()
    now = datetime.datetime.now()
    year = now.year

    temp = (100-int(args.edad_actual)) + year

    print (mensaje.format(args.nombre, temp))
