from art import logo, vs
from game_data import data
import random

def rep():
    print("\n" * 15)
    print(logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
    print(vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")

def end():
    print("\n" * 15)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


A = random.choice(data)
B = random.choice(data)
while A == B:
    B = random.choice(data)
print(logo)
print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")
print(vs)
print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
player = input("Who has more followers? Type 'A' or 'B': ").upper()

game_over =  False
score = 0
while not game_over:
    if A["follower_count"] > B ["follower_count"]:
        answer = "A"
    else:
        answer = "B"
    if answer == player:
        score += 1
        A = B
        B = random.choice(data)
        while A == B:
            B = random.choice(data)
        rep()
        player = input("Who has more followers? Type 'A' or 'B': ").upper()
    else:
        game_over = True
        end()
