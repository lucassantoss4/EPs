def transforma_base(lista):
    questoes_por_nivel = {}

    for questao in lista:
        nivel = questao['nivel']

        if nivel not in questoes_por_nivel:
            questoes_por_nivel[nivel] = []
        questoes_por_nivel[nivel].append(questao)

    return questoes_por_nivel