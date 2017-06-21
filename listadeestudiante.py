import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]
           

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:

        estudiantes = {
            

            'abcd': random.choice(NOMBRES),
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }
        return estudiantes


print generar_diccionario_estudiantes()
