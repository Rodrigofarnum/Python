import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# Escolhendo a palavra aleatória da lista
chosen_word = random.choice(word_list)
print(chosen_word)

# Criando o espaço reservado para a palavra
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Palavra para adivinhar: " + placeholder)

game_over = False
correct_letters = []
all_letters = []
vidas = 6

# Loop do jogo
while not game_over:
    guess = input("Adivinhe uma letra: ").lower()
    all_letters.append(guess)
    display = ""

    # Resposta errada
    if guess not in chosen_word:
        print(f"Você errou {guess}, essa letra não está na palavra. Você perdeu uma vida.")
        vidas -= 1

        # Verifica se as vidas chegaram a zero e termina o jogo
        if vidas == 0:
            print(f"****************************A PALAVRA ERA {chosen_word}! VOCÊ PERDEU****************************")
            game_over = True
            break  # Isso sai do loop enquanto o jogo estiver terminado

    elif guess in correct_letters or guess in all_letters:
        print(f"Você já adivinhou {guess}")

    # Resposta certa
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Imprime a parte do boneco (hangman) de acordo com as vidas restantes
    print(stages[vidas])
    print(f"**************************** {vidas}/6 VIDAS RESTANTES****************************")
    print("Palavra para adivinhar: " + display)

    # Verifica se a palavra foi completamente adivinhada
    if display == chosen_word:
        print(f"Parabéns! Você adivinhou a palavra '{chosen_word}'!")
        game_over = True
