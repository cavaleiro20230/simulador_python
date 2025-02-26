"""
Script para iniciar a API e executar a simulação de cliente
"""
import subprocess
import time
import sys
import os

def main():
    # Verifica se o diretório static existe
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Verifica se o arquivo swagger.json existe
    if not os.path.exists('static/swagger.json'):
        print("ERRO: O arquivo swagger.json não foi encontrado em static/")
        print("Certifique-se de que o arquivo foi criado corretamente.")
        return
    
    print("Iniciando o servidor API...")
    
    # Inicia o servidor em um processo separado
    server_process = subprocess.Popen([sys.executable, 'app.py'])
    
    try:
        # Aguarda o servidor iniciar
        print("Aguardando o servidor iniciar (10 segundos)...")
        time.sleep(10)
        
        # Executa o cliente
        print("Executando o cliente de simulação...")
        client_process = subprocess.run([sys.executable, 'client_simulation.py'])
        
        # Verifica se o cliente foi executado com sucesso
        if client_process.returncode != 0:
            print("ERRO: O cliente de simulação encontrou problemas.")
        else:
            print("Cliente de simulação executado com sucesso!")
    
    finally:
        # Encerra o servidor
        print("Encerrando o servidor API...")
        server_process.terminate()
        server_process.wait()
        print("Servidor encerrado.")

if __name__ == "__main__":
    main()