# Pedra, Papel e Tesoura com "IA Gulosa" 

# Precisamos do 'random' só para o computador "se virar"
# nas primeiras rodadas, antes de ter dados sobre você.
import random

# 1. PREPARAÇÃO
print("Vamos jogar Pedra, Papel e Tesoura!")
print("Eu sou uma IA de Python, e vou te vencer!: vou tentar descobrir seu padrão e te vencer.")

opcoes = ['pedra', 'papel', 'tesoura']

# Este é o "cérebro" da nossa IA.
# É um dicionário (dict) que vai guardar a CONTAGEM de quantas vezes você jogou cada opção.
historico_jogador = {
    'pedra': 0,
    'papel': 0,
    'tesoura': 0
}

# Este dicionário é um "mapa" que nos diz o que ganha de quê.
# A "chave" (esquerda) é a jogada, o "valor" (direita) é o que ganha dela.
o_que_ganha = {
    'pedra': 'papel',      # Papel ganha de Pedra
    'papel': 'tesoura',    # Tesoura ganha de Papel
    'tesoura': 'pedra'     # Pedra ganha de Tesoura
}

# O loop principal do jogo, para jogar várias vezes
while True:

    # 2. PEGANDO A JOGADA DO USUÁRIO
    usuario = input("\nEscolha Pedra, Papel ou Tesoura (ou 'sair'): ").lower()

    if usuario == 'sair':
        print("Até a próxima! Foi um bom jogo.")
        break

    if usuario not in opcoes:
        print(f"'{usuario}' não é válido. Tente 'pedra', 'papel' ou 'tesoura'.")
        continue

    # 3. AQUI COMEÇA O ALGORITMO GULOSO
    
    # Vamos decidir a jogada do computador.
    # Primeiro, vamos ver se o histórico tem alguma coisa.
    # 'sum(historico_jogador.values())' soma todas as contagens.
    # Se for 0, é a primeira rodada!
    if sum(historico_jogador.values()) == 0:
        # Na primeira rodada, o computador não tem dados.
        # Ele joga aleatoriamente.
        computador = random.choice(opcoes)
        print("Primeira rodada... vou chutar!")
    
    else:
        # A partir da segunda rodada, a IA GULOSA começa!
        
        # 1. ANALISAR DADOS ATUAIS:
        # Esta linha encontra a "chave" (pedra, papel ou tesoura)
        # que tem o MAIOR "valor" (a contagem) no nosso dicionário.
        # 'key=historico_jogador.get' diz ao 'max' para olhar os valores, não os nomes.
        jogada_mais_frequente = max(historico_jogador, key=historico_jogador.get)
        
        # 2. FAZER A ESCOLHA:
        # A IA assume que você vai repetir sua jogada mais frequente.
        # Então, ela joga o que GANHA dessa jogada.
        # Nós usamos nosso mapa 'o_que_ganha' para descobrir.
        jogada_gulosa = o_que_ganha[jogada_mais_frequente]
        
        computador = jogada_gulosa
        print(f"Notei que você gosta de jogar '{jogada_mais_frequente}'...")


    # 4. EXIBIR JOGADAS E VERIFICAR O VENCEDOR
    
    print(f"\nVocê jogou: {usuario}")
    print(f"O computador jogou: {computador}\n")

    if usuario == computador:
        print("Foi um empate!")
    
    # A lógica de vitória é checar se a jogada do computador está no nosso mapa 'o_que_ganha' como a vencedora da jogada do usuário.
    elif computador == o_que_ganha[usuario]:
        print("Ah, não... O computador ganhou!")
    
    else:
        # Se não foi empate e o computador não ganhou, você ganhou.
        print("Você ganhou! Parabéns!")

    # 5. FIM DO ALGORITMO
    # ATUALIZAR O HISTÓRICO para a próxima rodada.
    # Pegamos a jogada que o usuário acabou de fazer...
    # E somamos +1 na contagem dela no nosso "cérebro".
    historico_jogador[usuario] += 1
    
    # Mostra o "cérebro" do computador em ação (opcional, mas legal)

    print(f"Placar do seu histórico: {historico_jogador}")
