from time import sleep

# Simulação de um banco de dados simples em memória para usuários cadastrados

usuarios_cadastrados = {}

print('\33[33m-=-'*30 + '\33[m')
print('\33[34m-=-'*11 + '   Bem vindos ao Game   ' + '-=-'*11 + '\33[m')
print('\33[33m-=-'*30 + '\33[m')

print('Vamos começar seu cadastro!')

email = ''

# Verificação do e-mail
while '@' not in email or '.com' not in email:
    email = str(input('Digite seu e-mail:   ')).lower()
    print('\33[34m Processando ...' + '\33[m')
    sleep(1)
    if '@' not in email or '.com' not in email:
        print('\33[31m E-mail incorreto, preencha algo como: xxxxxxx@xxx.com  \33[m')

remail = ''
while remail != email:
    remail = str(input('Confirme seu e-mail:   ')).lower()
    print('\33[34m Processando ...' + '\33[m')
    sleep(1)   
    if remail != email:
        print('\33[31m O e-mail deve ser identico ao digitado anteriormente  \33[m')

nome = str(input('Digite seu nome:   ')).title()
user = str(input('Digite seu usuário para login:   ')).lower()

# Verifica se o usuário já existe
if user in usuarios_cadastrados:
    print("\33[31mUsuário já existe! Tente outro nome.\33[m")
else:
    print('\33[33m Carregando 🕑' + '\33[m')
    sleep(2)

    print('Vamos definir uma senha.')
    print('\33[36m Sua senha deve conter no mínimo 8 caracteres, uma maiúscula e minúscula, um dígito e um caracter especial \33[m')

    def validar_senha(senha):
        if len(senha) < 8:
            return "\33[31mSenha muito curta! Deve ter pelo menos 8 caracteres.\33[m"
        if not any(char.isdigit() for char in senha):
            return "\33[31mSenha deve conter pelo menos um número.\33[m"
        if not any(char.isupper() for char in senha):
            return "\33[31mSenha deve conter pelo menos uma letra maiúscula.\33[m"
        if not any(char.islower() for char in senha):
            return "\33[31mSenha deve conter pelo menos uma letra minúscula.\33[m"
        if not any(char in "!@#$%^&*()-_+=<>?/" for char in senha):
            return "\33[31mSenha deve conter pelo menos um caractere especial.\33[m"
        return "Senha válida!"  # Retorno fixado para comparação no loop

    senha = ""
    while True:  # Loop infinito até a senha ser válida
        senha = input("Digite sua senha:   ")
        resultado = validar_senha(senha)
        if resultado == "Senha válida!":
            print("\33[34mSenha salva!\33[m")  # Mensagem para senha válida
            repeatsenha = ''
            while repeatsenha != senha:
                repeatsenha = str(input('Confirme sua senha:   '))
                print('\33[34m Processando ...' + '\33[m')
                sleep(1)   
                if repeatsenha != senha:
                    print('\33[31m A senha deve ser a mesma digitada anteriormente  \33[m')
            print('Vamos realizar seu primeiro login')
            sleep(3)
            usuarios_cadastrados[user] = senha  # Armazena o usuário e a senha no banco de dados
            break  # Sai do loop se a senha for válida
        else:
            print(resultado)  # Mostra o erro e continua pedindo

print('.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n')

# Processo de login
luser = str(input('Digite seu usuário:   '))

lsenha = ''

if luser in usuarios_cadastrados:  # Verifica se o usuário existe
    while lsenha != usuarios_cadastrados[luser]:
        lsenha = input('Digite sua senha:   ')
        print('\33[34m Processando ...' + '\33[m')
        sleep(1)
        if lsenha != usuarios_cadastrados[luser]:
            print('\33[31m Senha incorreta, tente novamente:   \33[m')
    print('Bem vindo(a) {}!' .format(nome))
else:
    print("\33[31mUsuário não encontrado. Faça o cadastro primeiro.\33[m")