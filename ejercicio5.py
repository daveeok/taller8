courseA = {"Ana", "Carlos", "Laura", "Pedro", "Sofia", "Andres", "Camila"}
courseB = {"Laura", "Pedro", "Daniel", "Sofia", "Mateo", "Valentina"}

def text(group):
    return ", ".join(sorted(group)) if group else "(ninguno)"

def showMenu():
    print(f"""
    ------ MENU DE CURSOS ------
    1. Ver información de los cursos.
    2. Agregar estudiantes.
    0. Salir.
    """)
    
    selectOption()

def selectOption():
    option = int(input("Seleccione una opción: "))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    else: 
        print("Finalizando programa.")
        SystemExit

def option1():
    print(f"""
    ------ CURSOS ------
    Cuso A: {text(courseA)}
    Curso B: {text(courseB)}

    Estudiantes en total: {len(courseA.union(courseB))}
    Estudiantes que están en ambos cursos: {text(courseA.intersection(courseB))}
    Estudiantes que solo estan en el curso A: {text(courseA.difference(courseB))} 
    Estudiantes que solo estan en el curso B: {text(courseB.difference(courseA))}
    Estudiantes que estan en solo uno de los 2 cursos: {text(courseA.symmetric_difference(courseB))}
    ¿Todos los del curso A están en B? {(courseA <= courseB)}
          """)
    returnMenu = input("Presione [Enter] para volver al menú")
    showMenu()

def option2():
    while True:
        print("--- AGREGAR ESTUDIANTE ---")
        course = input("Ingrese el curso (A o B): ").strip().upper()
        if course == "A":
            name = input("Ingrese el Nombre del estudiante: ").strip().title()
            if name == "":
                print("El nombre no puede estar vacio")
            elif not name in courseA and not name in courseB:
                print("El estudiante no existe")
            else: 
                courseA.add(name)
                print(f"El estudiante {name} ha sido agregado correctanmente al curso {course}")
                returnMenu = input("Presione [Enter] para volver al menú")
                showMenu()
                break
        elif course == "B":
            name = input("Ingrese el Nombre del estudiante: ").strip().title()
            if name == "":
                print("El nombre no puede estar vacio")
            elif not name in courseA and not name in courseB:
                print("El estudiante no existe")
            else:       
                courseB.add(name)
                print(f"El estudiante {name} ha sido agregado correctanmente al curso {course}")
                returnMenu = input("Presione [Enter] para volver al menú")
                showMenu()
                break
        else:
            print("El curso no existe.")

showMenu()