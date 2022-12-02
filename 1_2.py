# A rock
# B paper
# C Scissors


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
        

# X lose, Y draw, Z win
        opp = reg[0]
        player = reg[1]

        if opp == "A":
            if player == "X":
                score+= LOSS
                score += SC
                continue
                
            if player == "Y":
                score+= TIE
                score += ROCK
                continue
            else: 
                score += WIN
                score += PAPER
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
                score += LOSS
                score += PAPER
                continue

            if player == "Y":
                score += TIE
                score += SC
                continue

            else:
                score += WIN
                score += ROCK
                continue

print(score)

        


