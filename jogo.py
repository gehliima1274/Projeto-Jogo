# Pedra, Papel e Tesoura com "IA Gulosa" 
# Esse é um jogo de Pedra, Papel e Tesoura onde o computador tenta me vencer usando uma estratégia simples.

# Usamos o random só para o computador chutar uma jogada na primeira rodada, porque ainda não tem histórico.
import random

# Aqui mostramos a mensagem de boas-vindas e defino as três jogadas possíveis.
print("Vamos jogar Pedra, Papel e Tesoura!")
print("Eu sou uma IA de Python, e vou te vencer!: vou tentar descobrir seu padrão e te vencer.")

opcoes = ['pedra', 'papel', 'tesoura']

# Esse dicionário guarda quantas vezes eu joguei cada opção. Ele é o ‘cérebro’ do computador para aprender meu padrão.
historico_jogador = {
    'pedra': 0,
    'papel': 0,
    'tesoura': 0
}

# Esse mapa diz qual jogada vence outra. Por exemplo, papel vence pedra, tesoura vence papel e pedra vence tesoura.
o_que_ganha = {
    'pedra': 'papel',      # Papel ganha de Pedra
    'papel': 'tesoura',    # Tesoura ganha de Papel
    'tesoura': 'pedra'     # Pedra ganha de Tesoura
}

#O jogo roda dentro desse loop, pedindo minha jogada a cada rodada. O .lower() transforma a resposta em minúscula para facilitar a comparação.
while True:

    usuario = input("\nEscolha Pedra, Papel ou Tesoura (ou 'sair'): ").lower()

# Se eu digitar ‘sair’, o jogo termina.
    if usuario == 'sair':
        print("Até a próxima! Foi um bom jogo.")
        break
        
#Se eu digitar algo que não seja pedra, papel ou tesoura, o programa avisa e pede para tentar de novo.
    if usuario not in opcoes:
        print(f"'{usuario}' não é válido. Tente 'pedra', 'papel' ou 'tesoura'.")
        continue

    
    if sum(historico_jogador.values()) == 0:
        computador = random.choice(opcoes)
        print("Primeira rodada... vou chutar!")
# Na primeira rodada, como o histórico está zerado, o computador escolhe aleatoriamente.
    
    else:
        
        jogada_mais_frequente = max(historico_jogador, key=historico_jogador.get)
        jogada_gulosa = o_que_ganha[jogada_mais_frequente]
        computador = jogada_gulosa
        print(f"Notei que você gosta de jogar '{jogada_mais_frequente}'...")
# Depois da primeira rodada, o computador olha qual jogada eu mais repeti e escolhe o que vence essa jogada.
    
    print(f"\nVocê jogou: {usuario}")
    print(f"O computador jogou: {computador}\n")
# Mostra as jogadas do jogador e do computador.
    
    if usuario == computador:
        print("Foi um empate!")
# Se as jogadas forem iguais, é empate.
    
   
    elif computador == o_que_ganha[usuario]:
        print("Ah, não... O computador ganhou!")
# Se a jogada do computador vence a minha, ele ganha.
    
    else:
        print("Você ganhou! Parabéns!")
# Se não é empate e o computador não venceu, significa que eu ganhei.

    historico_jogador[usuario] += 1
    print(f"Placar do seu histórico: {historico_jogador}")
# No final de cada rodada, o computador atualiza meu histórico, guardando minha jogada para tentar prever melhor na próxima rodada.
