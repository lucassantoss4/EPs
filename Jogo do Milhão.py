def transforma_base(lista):
    questoes_por_nivel = {}

    for questao in lista:
        nivel = questao['nivel']

        if nivel not in questoes_por_nivel:
            questoes_por_nivel[nivel] = []
        questoes_por_nivel[nivel].append(questao)

    return questoes_por_nivel

def valida_questao (questao):

    dicio_erros = {}
    opcoes_esperadas = ['A', 'B', 'C', 'D']
    chaves_esperadas = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves_esperadas:
        if chave not in questao:
            dicio_erros[chave] = 'nao_encontrado'

        if 'correta' not in questao:
            dicio_erros['correta'] = 'nao_encontrado'

        else:
            if  questao['correta'] not in opcoes_esperadas:
                dicio_erros['correta'] = 'valor_errado'

        if len(questao) != 4:
            dicio_erros['outro'] = 'numero_chaves_invalido'

        if 'titulo' in questao:
            if len(questao['titulo'].strip()) == 0:
                dicio_erros['titulo'] = 'vazio'

        if 'nivel' in questao:
            nivel = questao['nivel']
            if nivel != 'facil' and nivel != 'medio' and nivel != 'dificil':
                dicio_erros['nivel'] = 'valor_errado'

        if 'opcoes' in questao:
            if len(questao['opcoes']) != 4:
                dicio_erros['opcoes'] = 'tamanho_invalido'

            else:
                dicio_2 = {}
                if 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
                    dicio_erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                
                else:
                    if len(questao['opcoes']['A'].strip()) == 0:
                        dicio_2['A'] = 'vazia'
                    if len(questao['opcoes']['B'].strip()) == 0:
                        dicio_2['B'] = 'vazia'
                    if len(questao['opcoes']['C'].strip()) == 0:
                        dicio_2['C'] = 'vazia'
                    if len(questao['opcoes']['D'].strip()) == 0:
                        dicio_2['D'] = 'vazia'
                    if len(dicio_2) > 0:
                        dicio_erros['opcoes'] = dicio_2
                        
    return dicio_erros

def valida_questoes(questoes: list) -> list:
    correcao = []

    for questao in questoes:
        erros = valida_questao(questao)
        if not erros:
            correcao.append({})
        else:
            correcao.append(erros)
        
    return correcao

import random
def sorteia_questao (dicio_questao,nivel):
    if nivel in dicio_questao:
        lista_questoes = dicio_questao[nivel]
        indice = random.randint(0,len(lista_questoes)-1)
        return lista_questoes[indice]
    else:
        return None
    
def sorteia_questao_inedita(dicio_quest, nivel, lista_questoes_ja_sorteada):
    questao = sorteia_questao(dicio_quest, nivel)
    while questao in lista_questoes_ja_sorteada:
        questao = sorteia_questao(dicio_quest, nivel)
    lista_questoes_ja_sorteada.append(questao)
    return questao


def questao_para_texto(questao, id):
    titulo = questao['titulo']
    nivel = questao['nivel']
    opcoes = questao['opcoes']

    texto_formatado = f"----------------------------------------\nQUESTAO {id}\n\n{titulo}\n\nRESPOSTAS:\n"

    for i in opcoes:
        resposta = opcoes[i]
        texto_formatado += f"{i}: {resposta}\n"

    return texto_formatado


def gera_ajuda(dicio_quest):
    letra_correta = dicio_quest['correta']
    opcao_correta = dicio_quest['opcoes'][letra_correta]
    letras_incorretas = []
    for letra_incorreta in dicio_quest['opcoes']:
        if letra_incorreta != letra_correta:
            letras_incorretas.append(letra_incorreta)

    
    
    qtd_dicas = random.randint(1, 2)
    if qtd_dicas == 1:
        le_incorreta = random.choice(letras_incorretas)
        opcao_incorreta = dicio_quest['opcoes'][le_incorreta]
        return f'DICA:\nOpções certamente erradas: {opcao_incorreta}'
    
    else:
        le_incorreta1 = random.choice(letras_incorretas)
        le_incorreta2 = random.choice(letras_incorretas)
        opcao_incorreta1 = dicio_quest['opcoes'][le_incorreta1]
        opcao_incorreta2 = dicio_quest['opcoes'][le_incorreta2]
        return f'DICA:\nOpções certamente erradas: {opcao_incorreta1} | {opcao_incorreta2} '

lista_questoes = [
    {
        'titulo': 'Qual o resultado da operação 57 + 32?',
        'nivel': 'facil',
        'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
        'correta': 'C'
    },
    {
        'titulo': 'Qual a capital do Brasil?',
        'nivel': 'facil',
        'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
        'correta': 'A'
    },
    {
        'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
        'nivel': 'medio',
        'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
        'correta': 'C'
    }
]

continuar = True
while continuar:
    dicio_questoes_por_nivel = transforma_base(lista_questoes)
    aprensetacao = 'Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer! '
    print(aprensetacao)

    nome = input('Qual seu nome? ')
    if nome == 'exit':
        break

    else:
        print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
        print('                                                     ')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        print('                                                     ')
        
        print('Aperte ENTER para continuar...') 

        play = input()

        if play.strip() == "":
            print('O jogo já vai começar! Lá vem a primeira questão! ')
            print('                                                     ')

            print('Vamos começar com questões do nível FACIL!  ')
            print('Aperte ENTER para continuar...  ')

            play = input()


            if play.strip() == "":
                while True:
                    premiacao = 0
                    pulos_restantes = 3
                    ajudas_restantes = 2
                    lista_questoes_ja_sorteada = []
                    questao = sorteia_questao_inedita(dicio_questoes_por_nivel, 'facil', lista_questoes_ja_sorteada)
                    print(questao_para_texto(questao, 1))
                    resposta = input('Sua resposta: ').strip().upper()

                    if resposta == 'PULA':
                        if pulos_restantes > 0:
                            pulos_restantes -= 1
                            print(f'Você pulou a questão! Restam {pulos_restantes} pulos.')
                            break
                        else:
                            print('Você já usou todos os seus pulos disponíveis!')

                    elif resposta == 'AJUDA':
                        if ajudas_restantes > 0:
                            ajudas_restantes -= 1
                            dica = gera_ajuda(questao)
                            print(dica)
                        else:
                            print('Você já usou todas as suas ajudas disponíveis!')

                    elif resposta == 'PARAR':
                        print(f'{nome}, sua pontuação final é: {premiacao}')
                        break

                    elif resposta not in ['A', 'B', 'C', 'D']:
                        print('Opção inválida! Digite novamente.')

                    else:
                        if resposta == questao['correta']:
                            premiacao += 1000
                            print('Resposta correta!')
                            print(f'Você acertou! Seu prêmio atual é de R$ {premiacao}\n')
                            
                        else:
                            print('Que pena! Você errou e vai sair sem nada :( ')
                            premiacao = 0
                            break

            
            