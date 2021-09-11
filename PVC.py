from random import randrange

arq = open('txt.txt', 'r')  #abre o arquivo
text = []  #Vetor para receber o txt
distance_matrix = [] #declaro um segundo vetor
cities = []
text = arq.readlines() #quebra as linhas do arquivo em vetores
distances = []
distances1 = []
distances2 = []
count = 0
textconcat = "a"

for i in range(len(text)):          #esse for percorre a posições dp vetor texto
    distance_matrix.append(text[i].split())  #aqui eu quebro nos espasos das palavras

for i in range(len(text)):          #Pega numero da cidade
    cities.append(i)

for n, i in enumerate(distance_matrix):
    for k, j in enumerate(i):
        distance_matrix[n][k] = int(j)


def funcao_objetivo(solution, file, textconcat):
    distancie = 0
    for i in range(0, len(solution) - 1):
        x = solution[i]
        y = solution[i + 1]
        distance_cities = distance_matrix[x][y]
        distancie = distancie + distance_cities

    return distancie + distance_matrix[solution[len(solution) - 1]][solution[0]]


def algoritmo_aleatorio(file):

    solution = []
    c_cities = []

    for i in cities:
        c_cities.append(i)

    while len(c_cities) > 0:
        index = randrange(len(c_cities))
        s_cities = c_cities[index]
        del c_cities[index]
        solution.append(s_cities)

    printt = str(funcao_objetivo(solution, file, textconcat))
    distances.append(printt)
    print("Solução final :", solution, " Distancia = ", printt )


def algoritmo_guloso(file):
    solution = []
    c_cities = []

    for i in cities:
        c_cities.append(i)

    index = randrange(len(c_cities))
    s_cities = c_cities[index]
    del c_cities[index]
    solution.append(s_cities)

    while len(c_cities) > 0:
        exit_citie = cities[solution[len(solution) - 1]]
        n_citie = c_cities[0]
        n_citie_index = 0
        s_distance = distance_matrix[exit_citie][n_citie]
        i = 0
        for cn_citie in c_cities:
            distance = distance_matrix[exit_citie][cn_citie]

            if distance < s_distance:
                s_distance = distance
                n_citie = cn_citie
                n_citie_index = i
            i = i + 1
        solution.append(c_cities[n_citie_index])
        del c_cities[n_citie_index]
    printt = str(funcao_objetivo(solution, file, textconcat))
    distances1.append(printt)
    print("Solução final :", solution, " Distancia = ", printt )


def algoritmo_semi_guloso(file):
    solution = []
    c_citie = []
    delta = 70

    for i in cities:
        c_citie.append(i)


    index = randrange(len(c_citie))
    s_citie = c_citie[index]
    del c_citie[index]
    solution.append(s_citie)

    while len(c_citie) > 0:
        val_random = randrange(100)
        if delta > val_random:
            citie_exit = cities[solution[len(solution) - 1]]
            n_citie = c_citie[0]
            n_citie_index = 0
            s_distance = distance_matrix[citie_exit][n_citie]
            i = 0
            for cn_citie in c_citie:
                distance = distance_matrix[citie_exit][cn_citie]
                if distance < s_distance:
                    s_distance = distance
                    n_citie = cn_citie
                    n_citie_index = i
                i = i + 1
            solution.append(c_citie[n_citie_index])
            del c_citie[n_citie_index]
        else:
            index = randrange(len(c_citie))
            s_citie = c_citie[index]
            del c_citie[index]
            solution.append(s_citie)

    printt = str(funcao_objetivo(solution, file, textconcat))
    distances2.append(printt)
    print("Solução final :", solution, " Distancia = ", printt )



execucao = 30
file = open("aleatorio.txt", "w")
while execucao > 0:
    algoritmo_aleatorio(file)
    execucao -= 1

textconcat0 = " ".join(distances)
file.write(textconcat0)


execucao = 30
file2 = open("guloso.txt", "w")
while execucao > 0:
    algoritmo_guloso(file2)
    execucao -= 1

textconcat1 = " ".join(distances1)
file2.write(textconcat1)

execucao = 30
file3 = open("semi_guloso.txt", "w")
while execucao > 0:
    algoritmo_semi_guloso(file3)
    execucao -= 1

textconcat2 = " ".join(distances2)
file3.write(textconcat2)
