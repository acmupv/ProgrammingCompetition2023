#Author: Jaume Ivars Grimalt
#        https://github.com/jaume2000

import argparse
import random

description= """
    Este programa sirve para generar casos de prueba para el problema de Friends del
    concurso de programación de ACM.

    Tomará 3 parámetros opcionales:
    1. Lista del número de personas por caso. Por defecto solo habrá 1 caso con un numero al azar de peronas (3~1000).
    2. Lista con el número de subconjuntos totales en ese caso. Esta lista debe ser tan larga como el número de casos. Por defecto será un número al azar entre 1 y el nº de personas de ese caso.
    3. El nombre del fichero para el output
    4. Archivo para debuggear y ver las respuestas. es el mismo que el anterior pero añadiendo + '_response.txt y otro +_debbugging.txt'

    Ejemplo:
    python friends_generator -p 3 25 60 250 -o results.txt
"""

parser = argparse.ArgumentParser(prog="Friends Generator", description=description)
parser.add_argument("-p", "--person_list", nargs="+", default=None)
parser.add_argument("-c", "--conjuntos", nargs="+", default=None)
parser.add_argument("-o", "--output", action="store", default="output.txt")
args = parser.parse_args()
person_list = args.person_list
conjuntos_list = args.conjuntos

#################################################
#####   1.Comprobación de los parámetros    #####
#################################################


#Si no nos han dado el argumento del nº de personas, hacemos 1 solo caso con un numero alazar de personas entre 3 y 1000
if person_list == None:
    person_list = [random.randint(3,1000)]
else:
    try:
        person_list = [int(p) for p in person_list]
    except:
        print("Error: el nº de personas debe ser un número")
    for people in person_list:
        if people < 2:
            print("Error: Deben haber almenos 2 personas en todos los casos.")
            exit()

#Si no nos han dado el nº de subconjuntos por caso, lo elegimos nosotros.
if conjuntos_list == None:
    conjuntos_list = list()
    for people in person_list:
        conjuntos_list.append(random.randint(1,people))
else:
    try:
        conjuntos_list = [int(c) for c in conjuntos_list]
    except:
        print("Error: el nº de conjuntos debe ser un número")
    for n_conj in conjuntos_list:
        if n_conj < 1:
            print("Error: Debe haber un número positivo (>0) de casos")
            exit()

#Si no hay el mismo número de conjuntos que de casos, lanzamos error.
if len(conjuntos_list) != len(person_list):
    print("Error: No hay el mismo número de elementos en la lista de personas por caso que en la lista de conjuntos por caso.")
    exit()

for i,n_conj in enumerate(conjuntos_list):
    if n_conj > person_list[i]:
        print("Error: no pueden haber más conjuntos que personas")
        exit()


#################################################
####        2. Ejecución del algoritmo      #####
#################################################


casos=len(person_list)
#Este será la id de la última persona del caso anterior, de este modo, nunca empezaremos desde la id 1 para diferentes casos.
#De este modo, ninguna persona tendrá la misma id para casos diferentes.
prevCase_max_person_id = 0
prevCase_num_relations = 0


#Conjunto R: Contiene las 2-tuplas de las relaciones, estas 2-tuplas serán conjuntos con 2 elementos, ya que {x,y} = {y,x} donde x != y
output = list()
response = list()
debugging = list()

for n_caso in range(casos):
    people = person_list[n_caso]
    num_conjuntos = conjuntos_list[n_caso]
    #Lista con los n_conj subconjuntos
    C = list()
    for conj_n in range(1,num_conjuntos+1):
        #Añadimos los conjuntos y la 1ra persona para tener un conjunto no-vacio.
        first_added_person = conj_n
        C.append({frozenset([prevCase_max_person_id+first_added_person])})

    #para el resto de personas las vamos añadiendo al azar entre estos conjuntos
    for person_n in range(prevCase_max_person_id+num_conjuntos+1, prevCase_max_person_id+people+1):
        rand_conj_n = random.randint(0,num_conjuntos-1)
        C[rand_conj_n].add(frozenset([person_n]))


    #print(C)
    #print()

    R = list()
    for Cn in C:
        #print(Cn)
        #mientras el subconjunto sea disjunto, hacer conexiones hasta que deje de ser disjunto.
        Rn = list()
        while len(Cn) > 1:
            Cn1 = random.choice(list(Cn))

            #Si se llegara a elegir el mismo conjunto y resulta que solo tiene 1 persona... No podríamos conectar a nadie!
            if(len(Cn1) == 1):
                Cn2 = random.choice(list(Cn.difference({Cn1})))
            else:
                Cn2 = random.choice(list(Cn))

            #Hacer una conexión entre dos personas diferentes en estos subconjuntos que PUEDE que sean el mismo.
            p1 =random.choice(list(Cn1))
            p2 =random.choice(list(Cn2.difference({p1})))

            #print("Connecting " + str(p1) + " with " + str(p2))

            #Si ya exisitía la conexión, no importa, no saldrá 2 veces
            Rn.append(frozenset([p1,p2]))
            #Si los conjuntos son diferentes, los unimos.
            if Cn1 != Cn2:
                Cn.remove(Cn1)
                Cn.remove(Cn2)
                Cn.add(Cn1.union(Cn2))

        R.extend(Rn)
    #Fin del caso, podemos hacer lo que queramos con las variables

    C = {c.pop() for c in C}
    output.append((people, len(R)))
    output.extend(R)
    debugging.append(([people], [len(R)]))
    debugging.extend(R)


    response.append(max([len(c) for c in C]))

    #prevCase_max_person_id = people

    print("Conjunto de los subconjuntos disjuntos en el caso " +str(n_caso)+":")
    print(C)
    debugging.append((str(C),""))
    debugging.append(("",""))
    print()

with open(args.output, "w") as f:
    f.write(str(casos) + "\n")
    for p1,p2 in output:
        f.write(str(p1) + " " + str(p2)+ "\n")

with open(args.output.split(".")[0] + "_results.txt", "w") as f:
    for n_res in response:
        f.write(str(n_res)+ "\n")

with open(args.output.split(".")[0] + "_debugging.txt", "w") as f:
    for p1, p2 in debugging:
        f.write(str(p1) + " " + str(p2) + "\n")
        







