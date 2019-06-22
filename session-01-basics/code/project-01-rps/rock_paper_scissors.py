player1 = input('Player 1 name: ')
player2 = input('Player 2 name: ')

print('Choose r, p, or s')
p1 = input('Player 1 choice: ')
p2 = input('Player 2 choice: ')

if p1 == p2:
    print('tie')

if p1 == 'r':
    if p2 == 'p':
        print(f'{player2} beats rock with paper')
    if p2 == 's':
        print(f'{player1} beats scissors with rock')
if p1 == 'p':
    if p2 == 'r':
        print(f'{player1} beats rock with paper')
    if p2 == 's':
        print(f'{player2} beats paper with scissors')
if p1 == 's':
    if p2 == 'r':
        print(f'{player2} beats rock with paper')
    if p2 == 'p':
        print(f'{player1} beats paper with scissors')