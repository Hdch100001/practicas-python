# Clase 13 
#     Proyecto, filtrando datos 
    #     Nueva caracteristica de las High order funtions: el  " | " que se usa para crear
    #   un diccionario nuevo y a el sumarle una llave mas con determinado valor si se cumple 
    #   la expresion.
    #     A continuación un ejemplo:
                            
    #                      old_people = list(map(lambda worker: worker | {"old": worker["age"] > 69}, DATA))
              

# CODIGO:


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 18,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 17, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 69}, DATA))
    
    # Reto:

    # ¿Nombre de los que dominan python?
    # Con high order funtions:
    all_python_devs2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs2 = list(map(lambda worker: worker["name"], all_python_devs2))

    for worker in all_python_devs2:
        print(worker)


    # ¿Nombre de los que trabajan en platzi?
    # Con high order funtions:
    all_platzi_workers2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers2 = list(map(lambda worker: worker["name"], all_platzi_workers2))
    
    for worker in all_platzi_workers2:
        print(worker)


    # ¿Nombre de los que son mayores de 18 años?
    # Con list comprehensions:
    adults2 = [print(worker["name"]) for worker in DATA if worker["age"] > 17]
   


if __name__ == '__main__':
    run()
