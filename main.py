import os
import requests
import socket
from time import sleep

def main():
    os.system("clear")
    print("""\033[1;95m
██╗██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
██║██╔══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║██╔═══╝ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║██║     ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                \033[1;102m\033[1;30m_Cyber security_\033[0;0m

\033[1;96m[\033[1;92m1\033[1;96m] \033[1;95m<-|-> \033[1;92mConsultar IP
\033[1;96m[\033[1;92m2\033[1;96m] \033[1;95m<-|-> \033[1;92mConsultar meu IP
\033[1;96m[\033[1;92m3\033[1;96m] \033[1;95m<-|-> \033[1;92mChecar porta
\033[1;96m[\033[1;92m4\033[1;96m] \033[1;95m<-|-> \033[1;92mSair
""")

    es = input('\033[1;95m-->\033[1;92m ')

    if es == '1' or es == '01':

        os.system('clear')
        ip = input('\033[1;95mDigite o IP \033[1;92m--> \033[1;93m')
        request = requests.get(f'http://ip-api.com/json/{ip}')
        json_api = request.json()

        if 'message' not in json_api:

            os.system('clear')

            print('\033[1;94mResultados abaixo :)\n')
            print('\033[1;93mIp: {}'.format(json_api['query']))
            print('Pais: {}'.format(json_api['country']))
            print('Estado: {}'.format(json_api['regionName']))
            print('Cidade: {}'.format(json_api['city']))
            print('Zip: {}'.format(json_api['zip']))
            print('Longitude: {}'.format(json_api['lon']))
            print('Latitude: {}'.format(json_api['lat']))
            print('Timezone: {}'.format(json_api['timezone']))
            print('Provedor: {}'.format(json_api['isp']))
            print('Organização: {}\n'.format(json_api['org']))

        else:

            print('\n\033[1;91mIP invalido\n')

        print('\033[1;102m\033[1;30m1 = Sair | 2 = Voltar ao menu\n\033[0;0m')
        sair = input('\033[1;95m-->\033[1;92m ')

        if sair == '01' or sair == '1':

            os.system('clear')
            print('\033[1;102m\033[1;91m_Cyber Security_\033[0;0m\n')
            exit()

        else:

            main()

    elif es == '2' or es == '02':

        os.system('clear')

        request = requests.get('http://ip-api.com/json/?')
        json_api = request.json()

        print('\033[1;94mResultados abaixo :) \n')
        print('\033[1;93mIp: {}'.format(json_api['query']))
        print('Pais: {}'.format(json_api['country']))
        print('Estado: {}'.format(json_api['regionName']))
        print('Cidade: {}'.format(json_api['city']))
        print('Zip: {}'.format(json_api['zip']))
        print('Longitude: {}'.format(json_api['lon']))
        print('Latitude: {}'.format(json_api['lat']))
        print('Timezone: {}'.format(json_api['timezone']))
        print('Provedor: {}'.format(json_api['isp']))
        print('Organização: {}\n'.format(json_api['org']))

        print('\033[1;102m\033[1;30m1 = Sair | 2 = Voltar ao menu\033[0;0m\n')
        sair = input('\033[1;95m-->\033[1;92m ')

        if sair == '1' or sair == '01':

            os.system('clear')
            print('\033[1;102m\033[1;91m_Cyber Security_\033[0;0m\n')
            exit()

        else:

            main()

    elif es == '3' or es == '03':

        cnx = socket.socket()
        os.system('clear')
        ip = input('\033[1;95mDigite um IP \033[1;92m-->\033[1;93m ')
        porta = int(input('\033[1;95mDigite uma porta \033[1;92m-->\033[1;93m '))
        time = 1

        cnx.settimeout(time)
        n = cnx.connect_ex((ip,porta))

        if n == 0:

            print('\n\033[1;92mPorta aberta\n')

        else:

            print('\nP\033[1;915morta fechada\n')

        print('\033[1;102m\033[1;30m1 = Sair | 2 = Voltar ao menu\033[0;0m\n')
        sair = input('\033[1;95m-->\033[1;92m ')

        if sair == '1' or sair == '01':

            os.system('clear')
            print('\033[102m\033[1;30m_Cyber Security_\033[0;0m\n')
            exit()

        else:

            main()

    elif es == '4' or es == '04':

        os.system('clear')
        print('\033[1;102m\033[1;30m_Cyber Security_\033[0;0m\n')
        exit()

    else:

        os.system('clear')
        print('\033[1;91mOpção invalida')
        sleep(2)
        main()

main()
