import csv
import os

CSVNAME = "integrador.csv"

def showAllCountry():
    countries = getAllCountry()

    print(f"{'NOMBRE':<20} {'POBLACION':>20} {'SUPERFICIE':>20} {'CONTINENTE':>20}")
    print("-" * 83)
    for country in countries:
        print(f"{country['nombre'].strip():<20} {country['poblacion']:>20} {country['superficie']:>20} {country['continente'].strip():>20}")


def addCountry(country):
    # Escribir header solo si el archivo no existe o esta vacio
    writeHeader = not os.path.exists(CSVNAME) or os.path.getsize(CSVNAME) == 0
    with open(CSVNAME, "a", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
        if writeHeader:
            writer.writeheader()
        writer.writerow(country)


def getAllCountry():
    catalog = []
    if not os.path.exists(CSVNAME):
        with open(CSVNAME, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()
        return catalog

    with open(CSVNAME, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            catalog.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"] })
    return catalog

def countryExist(nameCountry):
    catalog = getAllCountry()

    for country in catalog:
        if country["nombre"].strip().lower() == nameCountry.strip().lower():
            return True

    return False

def getNonEmptyCountryName():
    nameCountry = input("Ingrese el nombre del pais: ").strip()

    while nameCountry == "":
        print("No puede contener campos vacios .")
        nameCountry = input("Ingrese el nombre del pais: ").strip()

    return nameCountry

def getIntInput(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Error: debe ingresar un numero entero.")

def addMultipleyCountry():
    while True:
        nameCountry = getNonEmptyCountryName()

        if countryExist(nameCountry):
            print("El pais ingresado ya existe. Ingrese otro.")
        else:
            break

    population = getIntInput("Ingrese la poblacion total del pais: ")
    while population < 0:
        print("Error: la cantidad no puede ser negativa.")
        population = getIntInput("Ingrese la poblacion total del pais: ")
    
    areakm2 = getIntInput("Ingrese el area del pais: ")
    while areakm2 < 0:
        print("Error: la cantidad no puede ser negativa.")
        areakm2 = getIntInput("Ingrese el area del pais: ")
    
    continent = input(f"Ingrese el continente en donde se encuentra {nameCountry} : ")

    addCountry({"nombre": nameCountry, "poblacion": population, "superficie": areakm2, "continente": continent})
    print(f"El pais : {nameCountry} fue agregado correctamente.")

def saveCountry(country):
    with open(CSVNAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["nombre","poblacion","superficie","continente"])
        writer.writeheader()
        writer.writerows(country)

def updateCountry():
    countries = getAllCountry()
    showAllCountry()

    print("\nIngrese el nombre del pais que desea modificar:")
    nameCountry = getNonEmptyCountryName()

    for country in countries:
            if country["nombre"].strip().lower() == nameCountry.lower():
                print(f"Pais encontrado: {country['nombre']}")
                print(f"Poblacion actual: {country['poblacion']}")
                print(f"Superficie actual: {country['superficie']} km2")

                newPopulation = getIntInput("Ingrese nueva poblacion: ")
                while newPopulation < 0:
                    print("La poblacion no puede ser negativa.")
                    newPopulation = getIntInput("Ingrese nueva poblacion: ")

                newArea = getIntInput("Ingrese nueva superficie (km2): ")
                while newArea < 0:
                    print("La superficie no puede ser negativa.")
                    newArea = getIntInput("Ingrese nueva superficie (km2): ")

                country["poblacion"] = newPopulation
                country["superficie"] = newArea

                print("Datos actualizados correctamente.")
                break

    saveCountry(countries)

def findCountriesByName(query):
    query = query.strip().lower()  
    results = []                   
    countries = getAllCountry()    

    for country in countries:      
        name = country["nombre"].strip().lower()  
        if query in name:          
            results.append(country)  

    return results  
    
def searchCountryByName():
    name = getNonEmptyCountryName()
    results = findCountriesByName(name)
    print("\nResultados encontrados:\n")
    showCountries(results)


# LA DIFERENCIA CON SHOWALLCOUNTRY es que este muestra el pais que busque
def showCountries(countries):
    if not countries:
        print("No se encontraron paises.")
        return
    print(f"{'NOMBRE':<25} {'POBLACION':>15} {'SUPERFICIE':>15} {'CONTINENTE':>15}")
    print("-" * 70)
    for c in countries:
        print(f"{c['nombre'].strip():<25} {c['poblacion']:>15} {c['superficie']:>15} {c['continente'].strip():>15}")


def filterByContinent():
    continent = input("Ingrese el continente: ").strip().lower()
    if not continent:
        print("El continente no puede estar vacio.")
        return
    matches = []
    for c in getAllCountry():
        if continent in c["continente"].strip().lower():
            matches.append(c)
    print("\nResultados (por continente):")
    showCountries(matches)

def getIntRange(promptMin, promptMax):
    minVal = getIntInput(promptMin)
    maxVal = getIntInput(promptMax)
    if minVal > maxVal:
        minVal, maxVal = maxVal, minVal
    return minVal, maxVal


def filterByPopulationRange():
    minPop, maxPop = getIntRange("Ingrese poblacion minima: ", "Ingrese poblacion maxima: ")

    matches = []
    for c in getAllCountry():
        if minPop <= c["poblacion"] <= maxPop:
            matches.append(c)

    print(f"\nResultados (poblacion entre {minPop} y {maxPop}):")
    showCountries(matches)


def filterByAreaRange():
    minArea, maxArea = getIntRange("Ingrese superficie minima (km2): ", "Ingrese superficie maxima (km2): ")
 

    matches = []
    for c in getAllCountry():
        if minArea <= c["superficie"] <= maxArea:
            matches.append(c)

    print(f"\nResultados (superficie entre {minArea} y {maxArea} km2):")
    showCountries(matches)

def getOrderSettings():
    countries = getAllCountry()
    if not countries:
        print("No hay paises cargados para ordenar.")
        return None, None

    print("Seleccione el orden:")
    print("1) Ascendente")
    print("2) Descendente")
    option = input("Ingrese una opcion (1-2): ").strip()

    if option == "2":
        reverseOrder = True
    else:
        reverseOrder = False

    return countries, reverseOrder

def orderCountryByName():
    countries, reverseOrder = getOrderSettings()
    if not countries:
        return

# Se define una funcion interna porque solo se usa dentro de esta funcion.
# Permite mantener el codigo encapsulado y mas ordenado sin afectar el ambito global. Lo mismo en getPopulation y getArea
    def getName(country):
        return country["nombre"].strip().lower()

    ordered = sorted(countries, key=getName, reverse=reverseOrder)
    print("Paises ordenados por nombre:\n")
    showCountries(ordered)

def orderCountryByPopulation():
    countries, reverseOrder = getOrderSettings()
    if not countries:
        return

    def getPopulation(country):
        return country["poblacion"]

    ordered = sorted(countries, key=getPopulation, reverse=reverseOrder)
    print("Paises ordenados por poblacion:\n")
    showCountries(ordered)

def orderCountryByArea():
    countries, reverseOrder = getOrderSettings()
    if not countries:
        return

    def getArea(country):
        return country["superficie"]

    ordered = sorted(countries, key=getArea, reverse=reverseOrder)
    print("Paises ordenados por superficie:\n")
    showCountries(ordered)

def getMaxMinPopulation(countries):
    if not countries:
        return None, None

    maxPop = countries[0]
    minPop = countries[0]

    for c in countries:
        if c["poblacion"] > maxPop["poblacion"]:
            maxPop = c
        if c["poblacion"] < minPop["poblacion"]:
            minPop = c

    return maxPop, minPop

def getAverages(countries):
    if not countries:
        return 0, 0

    totalPopulation = 0
    totalArea = 0

    for c in countries:
        totalPopulation += c["poblacion"]
        totalArea += c["superficie"]

    avgPopulation = totalPopulation / len(countries)
    avgArea = totalArea / len(countries)

    return avgPopulation, avgArea

def getCountryCountByContinent(countries):
    continentCount = {}

    for c in countries:
        continent = c["continente"].strip().title()
        if continent in continentCount:
            continentCount[continent] += 1
        else:
            continentCount[continent] = 1

    return continentCount

def showStatistics():
    countries = getAllCountry()
    if not countries:
        print("No hay paises cargados para mostrar estadisticas.")
        return

    maxPop, minPop = getMaxMinPopulation(countries)

    avgPopulation, avgArea = getAverages(countries)

    continentCount = getCountryCountByContinent(countries)

    print("========== ESTADISTICAS ==========")
    print(f"Pais con mayor poblacion: {maxPop['nombre']} ({maxPop['poblacion']})")
    print(f"Pais con menor poblacion: {minPop['nombre']} ({minPop['poblacion']})")
    print(f"Poblacion promedio: {avgPopulation:.2f}")
    print(f"Superficie promedio: {avgArea:.2f} km2")
    print("Cantidad de paises por continente:")
    for cont, count in continentCount.items():
        print(f"  {cont}: {count}")

def mainMenu():
    while True:
        print("#" * 76)
        print("#                              MENU PRINCIPAL                              #")
        print("#" * 76)
        print("# 1. Agregar paises                                                        #")
        print("# 2. Actualizar los datos de Población y Superfice de un Pais              #")
        print("# 3. Buscar un país por nombre (coincidencia parcial o exacta).            #")
        print("# 4. Filtrar países (continente, rango de oblacion, rango de superficie)   #")
        print("# 5. Ordenar países (nombre, poblacion, superficie)                        #")
        print("# 6. Mostrar estadisticas                                                  #")
        print("# 7. Mostrar todos los paises                                              #")
        print("# 8. Salir                                                                 #")
        print("#" * 76)
        option = input("Ingrese opcion: ").strip()

        match option:
            case "1":         
                print("--------------------Agregar paises--------------------")  
                addMultipleyCountry()     
            case "2":
                print("--------------------Actualizar los datos de Población y Superfice de un Pais--------------------")
                updateCountry()
            case "3":
                print("--------------------Buscar un país por nombre (coincidencia parcial o exacta).--------------------")
                searchCountryByName()
            case "4":
                while True:
                    print("--------------------Filtrar paises--------------------")
                    print("1) Filtrar por continente")
                    print("2) Filtrar por rango de poblacion")
                    print("3) Filtrar por rango de superficie")
                    print("4) Salir")
                    option = input("Ingrese una opcion (1-4): ").strip()

                    if option == "1":
                        filterByContinent()
                    elif option == "2":
                        filterByPopulationRange()
                    elif option == "3":
                        filterByAreaRange()
                    elif option == "4":
                        print("Saliendo del menu de ordenamiento")
                        break
                    else:
                        print("Opcion invalida. Ingrese una opcion correcta.")           
            case "5":
                while True:
                    print("--------------------Ordenar países (nombre, poblacion, superficie)--------------------")
                    print("1) Ordenar por nombre")
                    print("2) Ordenar por poblacion")
                    print("3) Ordenar por superficie")
                    print("4) Salir")
                    option = input("Ingrese una opcion (1-4): ").strip()

                    if option == "1":
                        orderCountryByName()
                    elif option == "2":
                        orderCountryByPopulation()
                    elif option == "3":
                        orderCountryByArea()
                    elif option == "4":
                        print("Saliendo del menu de ordenamiento")
                        break
                    else:
                        print("Opcion invalida. Ingrese una opcion correcta")
            case "6":
                print("--------------------Mostrar estadisticas--------------------")
                showStatistics()
            case "7":
                print("--------------------------Mostrar toda la lista de paises--------------------------")
                showAllCountry()
            case "8":
                print("--------------------SALIR--------------------")
                break
            case _:   
                print("--------------------Opcion invalida. Intente nuevamente--------------------")

mainMenu()