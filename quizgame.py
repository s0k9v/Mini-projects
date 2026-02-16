# python quiz game

questions = ("Kuinka monesti tapio pommitti ranska?: ",
             "Mitä tapahtuu kun pommittaa israelin '2090'?: ",
             "Mikä eläin kantaa taloa selässään?: ",
             "Montako mannerta maapallolla on (jos Etelämantere ei ota lomaa)?: ",
             "Mikä on luvun 64 neliöjuuri (älä huijaa laskimella)?: ")
options = (("A. 19", "B. 4", "C. 1", "D. 3"),
                     ("A. israel pamahtaa", "B. ei mitään", "C. F. He torjuvat pommit", "D. J.K. älä huoli, se on vain pommi"),
                     ("A. Etana", "B. Kilpikonna", "C. Kettu", "D. Orava"),
                     ("A. 5", "B. 6", "C. 7", "D. 8"),
                     ("A. 6", "B. 7", "C. 8", "D. 9"))

answers = ("C", "A", "A", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions: 
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Syötä (A B C D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Oikein!")
    else:
        print("Väärin!")
        print(f"{answers[question_num]} on oikea vastaus")
    question_num += 1

print("---------------------------")
print("----------TULOKSET----------")
print("---------------------------")

print("Oikeat vastaukset: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Sinun vastauksesi: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Pistemääräsi: {score}%")