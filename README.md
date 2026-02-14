Sistema de Cadastro Flask
Este projeto é uma aplicação web para captura e armazenamento de dados desenvolvida em Python.

O sistema utiliza o framework Flask para gerenciar as rotas. A rota principal entrega a interface, enquanto a rota de cadastro processa as requisições. O servidor opera via protocolo HTTP na porta 5000.
a interface foi construída com HTML e CSS integrados. O envio de informações é feito através do método POST, o que isola os dados do formulário da URL da aplicação, seguindo as práticas de submissão de dados sensíveis.
O armazenamento utiliza manipulação de arquivos (File I/O). Os dados capturados pelo formulário são escritos em um arquivo de texto chamado cadastros.txt. Foi utilizado o modo de abertura "a" (append), que permite anexar novos registros ao final do arquivo sem apagar os dados existentes.

Instruções de Execução

Para rodar o projeto, é necessário instalar o Flask via terminal com o comando: pip install flask. Após a instalação, execute o script com o comando: python app.py. O acesso é feito pelo endereço localhost:5000 no navegador.
