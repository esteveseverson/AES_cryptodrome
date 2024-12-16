from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import secrets
import inquirer  # Usando o inquirer para a interface interativa

# Função para gerar uma chave aleatória de 128 bits (16 bytes)
def gerar_chave_aleatoria():
    return secrets.token_bytes(16)  # 128 bits = 16 bytes

# Função para cifrar a mensagem
def cifrar_mensagem(mensagem, chave):
    iv = get_random_bytes(16)  # Gerar um vetor de inicialização (IV) aleatório de 16 bytes
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    
    mensagem_padded = pad(mensagem.encode(), AES.block_size)  # Adicionar padding
    mensagem_cifrada = cipher.encrypt(mensagem_padded)
    
    return base64.b64encode(iv + mensagem_cifrada).decode()  # Codificar a mensagem cifrada em base64

# Função para decifrar a mensagem
def decifrar_mensagem(mensagem_cifrada, chave):
    dados_decodificados = base64.b64decode(mensagem_cifrada)  # Decodificar a base64
    iv = dados_decodificados[:16]  # Extrair o IV
    mensagem_cifrada = dados_decodificados[16:]  # Extrair a mensagem cifrada
    
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    mensagem_decifrada = unpad(cipher.decrypt(mensagem_cifrada), AES.block_size)  # Remover o padding
    
    return mensagem_decifrada.decode()  # Retornar a mensagem decifrada como string

def exibir_mensagem_cifrada(mensagem_cifrada):
    print(f"[Mensagem Cifrada]: {mensagem_cifrada}")

def exibir_mensagem_decifrada(mensagem_decifrada):
    print(f"[Mensagem Decifrada]: {mensagem_decifrada}")

def exibir_erro(mensagem_erro):
    print(f"[Erro]: {mensagem_erro}")

# Função principal que executa o loop interativo
def main():
    chave = gerar_chave_aleatoria()  # Gerar a chave aleatória
    chave_base64 = base64.b64encode(chave).decode()  # Mostrar chave em base64
    
    # Mensagem de boas-vindas
    print(f"Chave Aleatória gerada (base64): {chave_base64}\n")

    while True:
        # Usando inquirer para criar uma interface amigável
        perguntas = [
            inquirer.List('opcao',
                          message="Escolha uma opção",
                          choices=['Cifrar uma mensagem', 'Decifrar uma mensagem', 'Sair'],
                          ),
        ]
        
        resposta = inquirer.prompt(perguntas)
        
        if resposta['opcao'] == 'Cifrar uma mensagem':
            # Usando inquirer.Text para melhorar a entrada do usuário
            mensagem = inquirer.prompt([
                inquirer.Text('mensagem', message="Digite a mensagem para cifrar", validate=lambda _, x: len(x) > 0 or "A mensagem não pode ser vazia!")
            ])['mensagem']
            mensagem_cifrada = cifrar_mensagem(mensagem, chave)
            exibir_mensagem_cifrada(mensagem_cifrada)
        
        elif resposta['opcao'] == 'Decifrar uma mensagem':
            # Melhorando o prompt para decifrar a mensagem
            mensagem_cifrada = inquirer.prompt([
                inquirer.Text('mensagem_cifrada', message="Digite a mensagem cifrada (base64) para decifrar", validate=lambda _, x: len(x) > 0 or "A mensagem não pode ser vazia!")
            ])['mensagem_cifrada']
            try:
                mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
                exibir_mensagem_decifrada(mensagem_decifrada)
            except Exception as e:
                exibir_erro(str(e))
        
        elif resposta['opcao'] == 'Sair':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
