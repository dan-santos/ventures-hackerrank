# https://www.youtube.com/watch?v=iSNsgj1OCLA

# Criar lista com 100 números e ordenar aleatoriamente

# Loop 1 - para cada simulação
#   Loop 2 - para percorrer cada prisioneiro
#       Loop 3 - para cada prisioneiro individualmente percorrendo as caixas
#           Verificar se o número que ele encontrou é o número dele
#               Se ele encontrou (prisioneiro x abriu a caixa com número X), ele pode sair Loop 3 (Flag sucesso?)
#               Se ele não encontrou, ele se pega o número da ficha e abre a caixa com esse número.
#               Variável de contagem ++
#               Se essa variável for igual ao limite de tentativas, ele fracassou

from random import shuffle

n = 100
prisioneiros = list(range(n))

simulacoes = int(input('Qtd de simulações: '))

caixas = prisioneiros.copy()
sucessos = 0

for iteracao in range(simulacoes):
    flag_prisioneiros = True
    shuffle(caixas)
    for prisioneiro in prisioneiros:
        flag_prisioneiro = False
        tentativa = prisioneiro

        for i in range(n//2): # = Metade do número de prisioneiros
            # Verifica se o conteúdo da caixa é igual ao seu próprio número
            if caixas[tentativa] == prisioneiro:
                flag_prisioneiro = True            
                break
            # Caso contrário, a próxima caixa é a caixa com o número descoberto na caixa anterior
            else:
                tentativa = caixas[tentativa]

        if flag_prisioneiro is False:
            flag_prisioneiros = False
            break

    if flag_prisioneiros:
        sucessos += 1

print(f'Taxa de sucesso: {(sucessos/simulacoes)*100}')
