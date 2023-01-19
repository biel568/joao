


import os


def prosesar_resposta(resposta, nome):
    if resposta == '1':
        print(f' {os.linesep}{nome} que bom espero seja cada vez melhor.<:{os.linesep}  ')

    if resposta == '2':
        print(f"{os.linesep}{nome} espero que melhore seu dia. \:{os.linesep}  ")


def start():
    # apresentar a manu 'bot'
    print(f'olá me chamo manu. {os.linesep} ')
    # nome do user
    nome = input('digite seu nome  ' )
    # email do user


    # menu de respostas
    resposta = input(f'como vai seu dia?{os.linesep} [1] -- meu dia vai bem. {os.linesep} [2] -- meu dia não vai bem. {os.linesep}')
    # prosesar a resposta enviada
    prosesar_resposta(resposta,nome)


if __name__ == '__main__':
    start()
