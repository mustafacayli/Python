#Step 5

import random
#adam asmaca kelimeleri dosyasından kelimeler import edilir
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#adam asmaca resim klasöründen logo çekilir
from hangman_art import logo
print(logo)


#boş liste oluşturulur
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #önceden girdiği harfi tekrar girerse geri bildirim yap
    if guess in display:
        print(f"You've already guessed {guess}")

    #tahmin edilen harf kontrol edilir
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #yanlış harf girmişse
    if guess not in chosen_word:
        #tahmindeki harf seçilen kelimede yoksa canının gittiğini geri bildirim olarak ver
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"Chosen word is: {chosen_word}")

    #her harfi string yap
    print(f"{' '.join(display)}")

    #her harf tamamlanmış mı kontrol et
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #adam asmacadaki resmi kalan can hakkına göre yazdır
    from hangman_art import stages
    print(stages[lives])