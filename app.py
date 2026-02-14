from flask import Flask, request

app = Flask(__name__)


INTERFACE = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Gestão de Dados</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 380px; border-top: 6px solid #ff6600; }
        h2 { text-align: center; color: #333; }
        .field { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; color: #555; font-size: 14px; }
        input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 12px; background-color: #ff6600; border: none; color: white; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 10px; }
        button:hover { background-color: #e65c00; }
    </style>
</head>
<body>
    <div class="container">
        <h2>CADASTRO DE USUÁRIO</h2>
        <form method="POST" action="/cadastrar">
            <div class="field">
                <label>Nome Completo</label>
                <input type="text" name="nome" required>
            </div>
            <div class="field">
                <label>E-mail Corporativo</label>
                <input type="email" name="email" required>
            </div>
            <div class="field">
                <label>Senha</label>
                <input type="password" name="senha" required>
            </div>
            <button type="submit">EFETUAR REGISTRO</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return INTERFACE


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    
 
    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome} | Email: {email}\n")
    
    return f"<h1>Completo,</h1><p>O usuário <b>{nome}</b> foi registrado no sistema.</p><a href='/'>Voltar</a>"

if __name__ == '__main__':

    app.run(debug=True)
