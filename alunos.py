import csv

def readDataset(fnome):
    f = open(fnome)
    csv_reader = csv.reader(f, delimiter=';')
    alunos = []
    for row in csv_reader:
        alunos.append(tuple(row))
    return alunos

def distribCurso(alunos):
    res = {}
    for _, _, curso, *_ in alunos:
        if curso in res.keys():
            res[curso] = res[curso] + 1
        else: 
            res[curso] = 1
    return res

def mediaNotas(alunos):
    listaMedia = []
    for aluno in alunos:
        if len(aluno) > 7:
            id_aluno, nome, curso, tpc1, tpc2, tpc3, tpc4, media = aluno
        else:
            media= (int(aluno[3])+int(aluno[4])+int(aluno[5])+int(aluno[6]))/4
        alunoMedia=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media
        listaMedia.append(alunoMedia)
    return listaMedia

def escalaoPorMedia(listaMedia):
    escalaoMedia = []
    for alunoMedia in listaMedia:
        if len(alunoMedia) > 8:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao=alunoMedia
        else:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media=alunoMedia
        
        if int(media) in range (1,5):
            escalao="E"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            escalaoMedia.append(alunoEscalao)
        
        elif int(media) in range (5,9):
            escalao="D"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            escalaoMedia.append(alunoEscalao)

        elif int(media) in range (9,13):
            escalao="C"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            escalaoMedia.append(alunoEscalao)

        elif int(media) in range (13,16):
            escalao="B"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            escalaoMedia.append(alunoEscalao)
        
        elif int(media) in range (16,21):
            escalao="A"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            escalaoMedia.append(alunoEscalao)

    return escalaoMedia

def alunosPorEscalao(alunos):
    res = {}
    for _, _, _, _, _, _, _, _, escalao in alunos:
        if escalao in res.keys():
            res[escalao] += 1
        else: 
            res[escalao] = 1
    return res

def grafLinha(alunos):
    import matplotlib.pyplot as plt
    print("""    1-Distribuição por curso
    2-Distribuição por escalão
    Escolha uma das opções""")

    opcao=input("Escolha uma distribuição")

    if opcao=="1":
            distrib=distribCurso(alunos)
            eixoXx=distrib.keys()
            eixoXy=distrib.values()
            plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
            plt.title("Distribuição de alunos por Curso")
            plt.xlabel("Cursos", color ="blue")
            plt.ylabel("Número de alunos", color = "blue")
            plt.show()

    elif opcao=="2":
            distrib=alunosPorEscalao(alunos)
            eixoXx=distrib.keys()
            eixoXy=distrib.values()
            plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
            plt.title("Distribuição de alunos por Escalões")
            plt.xlabel("Escalões", color ="blue")
            plt.ylabel("Número de alunos", color = "blue")
            plt.show()
    else:
        print("Opção inválida")

def tabela(alunos):
    print("""    1- Distribuição de alunos por curso
    2- Distribuição de alunos por escalão
    Escolha uma das opções""")

    opcao=input("Escolha uma distribuição")
    
    if opcao=="1":
        distrib=distribCurso(alunos)
        print("Tabela distribuição de alunos por curso")
        print("")
        print(f" Curso   |  Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7} ")

    elif opcao == "2":
        distrib = alunosPorEscalao(alunos) 
        print(" Tabela distribuição de alunos por escalão:")
        print("")
        print(f" Escalão |  Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7} ")

    else:
        print("Opção inválida")

# Menu

opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma opção:"))
    print("""Menu:
    1 - Ver informação
    2 - Ver média das notas de cada aluno
    3 - Ver média e escalão de cada aluno
    4 - Ver distribuição de alunos por curso
    5 - Ver distribuição de alunos por escalão
    6 - Ver distribuição de alunos através de um gráfico
    7 - Ver distribuição de alunos através de uma tabela
    0 - Sair
    """)
    if opcao == 1:
        print(alunos)
    if opcao == 2:
        mediaNotas(alunos)
    if opcao == 3:
        escalaoPorMedia(listaMedia)
    if opcao == 4:
        distribCurso(alunos)    
    if opcao == 5:
        alunosPorEscalao(alunos)
    if opcao == 6:
        grafico(alunos)
    if opcao == 7:
        tabela(alunos)


