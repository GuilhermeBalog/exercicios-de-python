from time import sleep
import emoji
cor = {
    1: '30',
    2: '31',
    3: '32',
    4: '34',
    5: '33',
    6: '35',
    7: '36',
    8: '37',
    9: '7;30',
    10: '7;33'
}
for c in range(10, -1, -1):
    print('\033[{}m{}!\033[m'.format(cor[c], c))
    sleep(1)
print(emoji.emojize('\033[1;33m:collision: FELIZ ANO NOVO!!:collision:'))
