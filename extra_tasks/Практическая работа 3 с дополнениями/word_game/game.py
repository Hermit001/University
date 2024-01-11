from word_game.word_list import load_word_list, select_random_word
from word_game.score import update_score

def main():
    # Инициализация
    words = load_word_list()
    score = 0
    lives = 5

    while lives > 0:
        # Выбор случайного слова из списка
        word_to_guess = select_random_word(words)
        guessed_word = ["\u25A0"] * len(word_to_guess)
        guessed = False

        print(" ".join(guessed_word))

        while not guessed and lives > 0:
            user_input = input("Введите букву или слово целиком: ")

            if user_input == word_to_guess:
                guessed = True
            elif len(user_input) == 1 and user_input in word_to_guess:
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == user_input:
                        guessed_word[i] = user_input
                print(" ".join(guessed_word))
            else:
                lives -= 1
                print(f"Неверно! У вас осталось {lives} жизней.")

        if guessed:
            score = update_score(score, 1)
            print("Правильно!")
            print(f"Ваш текущий счет: {score}")
        else:
            print(f"Игра окончена. Правильное слово было: {word_to_guess}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            break

    print(f"Игра окончена. Ваш итоговый счет: {score}")

if __name__ == "__main__":
    main()
