def wizards(N, start, duels):
    owner = start
    num_owners = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner=duels[i][0]
            num_owners +=1
    print(owner, num_owners)

winner = wizards(3, "A", ["BA", "CB", "DA"])
print(winner)