def wizards(N, start, duels):
    owner = start
    changed_hands = 2
    # print(duels[0][1])
    if duels[0][1] == owner:
        owner=duels[0][0]
    changed_hands +=1
    return owner


winner = wizards(3, "A", ["BA", "CB", "DA"])
print(winner)