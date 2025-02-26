import requests
import json
import os
import time
from datetime import datetime

# URL base da API
BASE_URL = "http://localhost:5000/api"

# Chave de API simulada
API_KEY = os.environ.get("NASAJON_API_KEY", "api_key_simulada")

# Headers para autenticação
headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

def check_api_status():
    """Verifica o status da API"""
    try:
        response = requests.get(f"{BASE_URL}/status", headers=headers)
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique se a API está rodando")
        return None
    except Exception as e:
        print(f"Erro ao verificar status: {str(e)}")
        return None

def criar_lancamento_financeiro(lancamento):
    """Cria um lançamento financeiro"""
    try:
        response = requests.post(
            f"{BASE_URL}/financeiro/lancamentos",
            headers=headers,
            json=lancamento
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao criar lançamento financeiro: {str(e)}")
        return {"error": str(e)}, 500

def criar_lancamento_contabil(lancamento):
    """Cria um lançamento contábil"""
    try:
        response = requests.post(
            f"{BASE_URL}/contabil/lancamentos",
            headers=headers,
            json=lancamento
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao criar lançamento contábil: {str(e)}")
        return {"error": str(e)}, 500

def emitir_nota_fiscal(nota_fiscal):
    """Emite uma nota fiscal"""
    try:
        response = requests.post(
            f"{BASE_URL}/fiscal/notas-fiscais",
            headers=headers,
            json=nota_fiscal
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao emitir nota fiscal: {str(e)}")
        return {"error": str(e)}, 500

def cadastrar_funcionario(funcionario):
    """Cadastra um funcionário"""
    try:
        response = requests.post(
            f"{BASE_URL}/rh/funcionarios",
            headers=headers,
            json=funcionario
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao cadastrar funcionário: {str(e)}")
        return {"error": str(e)}, 500

def criar_pedido_compra(pedido):
    """Cria um pedido de compra"""
    try:
        response = requests.post(
            f"{BASE_URL}/compras/pedidos",
            headers=headers,
            json=pedido
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao criar pedido de compra: {str(e)}")
        return {"error": str(e)}, 500

def cadastrar_produto(produto):
    """Cadastra um produto"""
    try:
        response = requests.post(
            f"{BASE_URL}/estoque/produtos",
            headers=headers,
            json=produto
        )
        return response.json(), response.status_code
    except Exception as e:
        print(f"Erro ao cadastrar produto: {str(e)}")
        return {"error": str(e)}, 500

def esperar_api_iniciar(max_tentativas=5, intervalo=2):
    """Espera a API iniciar antes de prosseguir"""
    print("Verificando se a API está online...")
    for tentativa in range(max_tentativas):
        status = check_api_status()
        if status and status.get('status') == 'online':
            print(f"API online após {tentativa + 1} tentativa(s)")
            return True
        print(f"API não está online. Tentativa {tentativa + 1}/{max_tentativas}")
        time.sleep(intervalo)
    return False

def simular_operacoes():
    """Simula operações em todos os módulos"""
    print("=== Simulação de Integração com Nasajon ===")
    
    # Espera a API iniciar
    if not esperar_api_iniciar():
        print("Não foi possível conectar à API. Verifique se o servidor está rodando.")
        return
    
    # Verifica status da API
    status = check_api_status()
    print(f"Status da API: {status['status']}")
    print(f"Módulos disponíveis: {', '.join(status['modules'])}")
    print("\n")
    
    # 1. Financeiro - Criar lançamento
    lancamento_financeiro = {
        "identificador": "LF001",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "valor": 1500.00,
        "tipo": "RECEITA",
        "conta": "1001",
        "descricao": "Venda à vista"
    }
    
    resultado, status_code = criar_lancamento_financeiro(lancamento_financeiro)
    print(f"Financeiro - Criar lançamento: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    # 2. Contábil - Criar lançamento
    lancamento_contabil = {
        "identificador": "LC001",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "valor": 1500.00,
        "debito": "1001",
        "credito": "2001",
        "historico": "Venda à vista"
    }
    
    resultado, status_code = criar_lancamento_contabil(lancamento_contabil)
    print(f"Contábil - Criar lançamento: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    # 3. Fiscal - Emitir nota fiscal
    nota_fiscal = {
        "numero": "NF001",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "valor": 1500.00,
        "cliente": {
            "cnpj": "12345678000100",
            "nome": "Cliente Exemplo"
        },
        "itens": [
            {
                "codigo": "001",
                "descricao": "Produto A",
                "quantidade": 1,
                "valorUnitario": 1500.00
            }
        ]
    }
    
    resultado, status_code = emitir_nota_fiscal(nota_fiscal)
    print(f"Fiscal - Emitir nota fiscal: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    # 4. RH - Cadastrar funcionário
    funcionario = {
        "matricula": "F001",
        "nome": "João Silva",
        "cpf": "12345678900",
        "cargo": "Analista",
        "salario": 5000.00,
        "dataAdmissao": datetime.now().strftime("%Y-%m-%d")
    }
    
    resultado, status_code = cadastrar_funcionario(funcionario)
    print(f"RH - Cadastrar funcionário: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    # 5. Compras - Criar pedido
    pedido_compra = {
        "numero": "PC001",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "fornecedor": {
            "cnpj": "98765432000100",
            "nome": "Fornecedor Exemplo"
        },
        "itens": [
            {
                "codigo": "001",
                "descricao": "Material de escritório",
                "quantidade": 10,
                "valorUnitario": 50.00
            }
        ]
    }
    
    resultado, status_code = criar_pedido_compra(pedido_compra)
    print(f"Compras - Criar pedido: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    # 6. Estoque - Cadastrar produto
    produto = {
        "codigo": "P001",
        "descricao": "Produto Teste",
        "unidade": "UN",
        "preco": 100.00
    }
    
    resultado, status_code = cadastrar_produto(produto)
    print(f"Estoque - Cadastrar produto: {status_code}")
    print(f"Resultado: {json.dumps(resultado, indent=2)}")
    print("\n")
    
    print("=== Simulação concluída com sucesso ===")

if __name__ == "__main__":
    simular_operacoes()