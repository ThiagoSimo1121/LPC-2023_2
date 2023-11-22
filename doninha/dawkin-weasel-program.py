import string
import random
import time

caracteres = string.ascii_uppercase + ' '
objetivo = "METHINKS IT IS LIKE A WEASEL"


# Gera uma string aléatoria de 28 caracters
def gerador_de_strings(tamanho=28):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


# Função para verificar se ocorre mutação com base em uma taxa
def checar_taxa_de_mutacao(mutacao):
    return random.random() <= mutacao


# Altera os caracteres de uma string se passar no resultado da mutação
def alterar_caracteres_da_string(original):
    alterar_caracteres = []
    for index in original:
        if checar_taxa_de_mutacao(0.05):
            alterar_caracteres.append(random.choice(caracteres))
        else:
            alterar_caracteres.append(index)
    return ''.join(alterar_caracteres)


# Função identifica a quantidade de pontos feitos na string
def contar_pontos(string):
    soma_de_pontos = 0
    for caractere_string, caractere_objetivo in zip(string, objetivo):
        if caractere_string == caractere_objetivo:
            soma_de_pontos += 1
    return soma_de_pontos


# Função principal que implementa o algoritimo
def programa_weasel():
    string_atual = gerador_de_strings()
    geracao = 1

    while True:
        # Gera uma lista de 100 filhos para o melhor mutado ser escolhido
        filhos = []
        for _ in range(100):
            filhos.append(alterar_caracteres_da_string(string_atual))

        # Calcula as pontuações para cada filho para escolher o melhor
        pontos = []
        for string_atual in filhos:
            pontos.append(contar_pontos(string_atual))

        # Seleciona o filho com a pontuação mais alta para a próxima iteração
        melhor_posicao = pontos.index(max(pontos))
        string_atual = filhos[melhor_posicao]

        # Exibe informações sobre a geração atual
        print(f"Geração {geracao}: {string_atual} (pontuação: {max(pontos)})")
        time.sleep(0.1)

        # Verifica se uma correspondência perfeita foi encontrada
        if max(pontos) == len(objetivo):
            print('-'*64)
            print(f"Geração perfeita encontrada {geracao}: {string_atual}")
            print('-'*64)
            break

        geracao += 1


# Roda o programa e perunta se quer continuar ao finalizar
if __name__ == "__main__":
    programa_weasel()
    while True:
        testar_novamente = str(input("Deseja testar novamente, digite (S/N) \n")).strip().upper()
        if testar_novamente == 'S':
            programa_weasel()
        if testar_novamente == 'N':
            break
