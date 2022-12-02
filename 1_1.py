# A rock
# B paper
# C Scissors

# X rock
# Y paper 
# Z Scissors

# rock = 1
# pape = 2
# Sc = 3
# +0, 3 = tie, 6 = win

LOSS = 0
TIE = 3
WIN = 6
ROCK = 1
PAPER = 2
SC = 3

score = 0

with open("input.txt", "r") as opp:
    for line in opp:
        reg = line.split()
        
        print(score)

        opp = reg[0]
        player = reg[1]

        if opp == "A":
            if player == "X":
                score+= TIE
                score += ROCK
                continue
                
            if player == "Y":
                score+= WIN
                score += PAPER
                continue
            else: 
                score += LOSS
                score += SC
                continue
        if opp == "B":
            if player == "X":
                score += LOSS
                score += ROCK
                continue
            if player == "Y":
                score += TIE
                score += PAPER
                continue
            else:
                score += WIN
                score += SC
                continue

        if opp == "C":

            if player == "X":
                score += WIN
                score += ROCK
                continue

            if player == "Y":
                score += LOSS
                score += PAPER
                continue

            else:
                score += TIE
                score += SC
                continue

print(score)

        


