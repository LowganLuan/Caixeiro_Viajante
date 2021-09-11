from random import randrange

arq = open('txt.txt', 'r')  #abre o arquivo
text = []  #Vetor para receber o txt
distance_matrix = [] #declaro um segundo vetor
cities = []
text = arq.readlines() #quebra as linhas do arquivo em vetores


for i in range(len(text)):          #esse for percorre a posições dp vetor texto
    distance_matrix.append(text[i].split())  #aqui eu quebro nos espasos das palavras

for i in range(len(text)):          #Pega numero da cidade
    cities.append(i)

for n, i in enumerate(distance_matrix):
    for k, j in enumerate(i):
        distance_matrix[n][k] = int(j)


def funcao_objetivo(solution):
    distancie = 0
    for i in range(0, len(solution) - 1):
        x = solution[i]
        y = solution[i + 1]
        distance_cities = distance_matrix[x][y]
        distancie = distancie + distance_cities
    return distancie + distance_matrix[solution[len(solution) - 1]][solution[0]]


def algoritmo_aleatorio():
    solution = []
    c_cities = []

    for i in cities:
        c_cities.append(i)

    while len(c_cities) > 0:
        index = randrange(len(c_cities))
        s_cities = c_cities[index]
        del c_cities[index]
        solution.append(s_cities)

    print("Solução final :", solution, " Distancia = ", funcao_objetivo(solution))


def algoritmo_guloso():
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

    print("Solução final :", solution, " Distancia = ", funcao_objetivo(solution))


def algoritmo_semi_guloso():
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

    print("Solução final :", solution, " Distancia = ", funcao_objetivo(solution))

#execucao = 30
#while execucao > 0:
#    algoritmo_aleatorio()
#    execucao -= 1

#execucao = 30
#while execucao > 0:
#    algoritmo_guloso()
#    execucao -= 1

execucao = 30
while execucao > 0:
    algoritmo_semi_guloso()
    execucao -= 1