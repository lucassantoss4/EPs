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