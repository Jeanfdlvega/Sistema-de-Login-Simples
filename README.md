Sistema de Login Simples
Este é um sistema de login simples desenvolvido em Python usando a biblioteca PySimpleGUI. O programa permite que os usuários ingressem um nome de usuário e senha. Se a senha estiver correta, uma mensagem de boas-vindas será exibida. Caso contrário, será exibida uma mensagem de erro.

Requisitos
Python 3.x
PySimpleGUI (pode ser instalado usando pip install PySimpleGUI)
Uso
Clone o repositório:

bash
Copy code
git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:

bash
Copy code
cd seu-repositorio
Execute o programa:

bash
Copy code
python login.py
Insira o nome de usuário e a senha nos campos correspondentes.

Clique no botão "Submeter" para verificar as credenciais.

Detalhes do Código
login.py: Contém o código principal do programa.
hashlib: Função para criar o hash da senha.
PySimpleGUI: Biblioteca gráfica usada para criar a interface do usuário.
Notas Adicionais
Este é um exemplo educacional e não deve ser utilizado em ambientes de produção sem as devidas melhorias de segurança.
As senhas são armazenadas como hashes para demonstrar uma prática mais segura de armazenamento de senhas.
