import PySimpleGUI as sg
import hashlib

def hash_senha(senha):
    # Função para criar o hash da senha (pode ser aprimorada em um aplicativo real)
    return hashlib.sha256(senha.encode()).hexdigest()

# Layout da janela
layout = [
    [sg.Text('Nome de usuário:'), sg.InputText(key='usuario')],
    [sg.Text('Senha:'), sg.InputText(key='senha', password_char='*')],
    [sg.Checkbox('Salvar senha', key='salvar_senha')],
    [sg.Button('Submeter')],
    [sg.Text('', size=(20, 2), key='saida')]
]

janela = sg.Window('Login', layout)

# Dados de usuário (pode ser substituído por um banco de dados ou outra fonte de dados)
dados_usuario = {'usuario': 'jeandelavega', 'senha': hash_senha('123456')}

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Submeter':
        usuario_digitado = valores['usuario']
        senha_digitada = hash_senha(valores.get('senha', ''))

        if usuario_digitado == dados_usuario['usuario'] and senha_digitada == dados_usuario['senha']:
            janela['saida'].update(f'Bem-vindo, {usuario_digitado}!')
        else:
            janela['saida'].update('Usuário ou senha incorretos. Tente novamente.')

        if valores['salvar_senha']:
            # Aqui você pode adicionar código para salvar a senha, se necessário
            pass

janela.close()
