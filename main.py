from colorama import Fore, init
init()
print(Fore.MAGENTA +''' ██████   ██████                     █████      ███                █████████  ██████████ ██████   █████''')
print(Fore.WHITE +''' ██████   ██████                     █████      ███                █████████  ██████████ ██████   █████''')
print(Fore.RED +''' ░███░█████░███   ██████   ████████  ░███████  ████   ██████     ███     ░░░  ░███  █ ░  ░███░███ ░███ 
 ░███░░███ ░███  ░░░░░███ ░░███░░███ ░███░░███░░███  ███░░███   ░███          ░██████    ░███░░███░███ 
 ░███ ░░░  ░███   ███████  ░███ ░░░  ░███ ░███ ░███ ░███ ░███   ░███    █████ ░███░░█    ░███ ░░██████ ''')
print(Fore.MAGENTA +''' ░███      ░███  ███░░███  ░███      ░███ ░███ ░███ ░███ ░███   ░░███  ░░███  ░███ ░   █ ░███  ░░█████ ''')
print(Fore.WHITE +''' █████     █████░░████████ █████     ████████  █████░░██████     ░░█████████  ██████████ █████  ░░█████''')
print(Fore.RED +'''░░░░░     ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░░░░  ░░░░░  ░░░░░░       ░░░░░░░░░  ░░░░░░░░░░ ░░░░░    ░░░░░ ''')
print(Fore.RED +'''========================================================''')
print(Fore.CYAN +'''                Coded By Marbio34''')
print(Fore.CYAN +'''            discord.gg/safo''')
print(Fore.RED +'''========================================================''')
print(Fore.GREEN +'''      ''')
import random, string
amount = int(input('Escoge el monto +250 que quieres generar: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    value += 1
    print(Fore.RED +'''Marbio34 is here (codigos guardados en codes.txt''')
