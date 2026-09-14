meme_dict = {
            'FARMAR AURA': 'Tirar onda em algo',
            'SIX SEVEN': 'Algo sem sentido(não tente entender o que é)',
            'GAG': 'Ficar surpreso com algo',
            'JURO': 'Geralmente é usado para dar ênfase em algo, mas depende do contexto'
            }
for i in range(5):
    word = input('Digite uma palavra para descobrir o significado dela')
    if word in meme_dict.keys():
        print(word +': ' + meme_dict[word])
    else:
        print('A palavra não existe no dicionário')
