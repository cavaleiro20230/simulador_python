import json
import uuid
from datetime import datetime
import os
import time

class SimulacaoNasajon:
    """Simulação local da API Nasajon"""
    
    def __init__(self):
        # Simulação de banco de dados em memória
        self.db = {
            'financeiro': [],
            'contabil': [],
            'fiscal': [],
            'rh': [],
            'compras': [],
            'vendas': [],
            'estoque': [],
            'patrimonio': []
        }
        # Diretório para logs e arquivos gerados
        os.makedirs('logs', exist_ok=True)
        self.log_file = os.path.join('logs', f'simulacao_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        
        # Inicializa o log
        self.log("Simulação Nasajon iniciada")
    
    def log(self, mensagem):
        """Registra mensagens no log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {mensagem}"
        print(log_entry)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + "\n")
    
    def validar_campos(self, dados, campos_obrigatorios):
        """Valida se todos os campos obrigatórios estão presentes"""
        for campo in campos_obrigatorios:
            if campo not in dados:
                raise ValueError(f"Campo obrigatório ausente: {campo}")
        return True
    
    def criar_lancamento_financeiro(self, lancamento):
        """Cria um lançamento financeiro"""
        try:
            # Validação básica
            self.validar_campos(lancamento, ['identificador', 'data', 'valor', 'tipo', 'conta'])
            
            # Adiciona ID e timestamp
            lancamento['id'] = str(uuid.uuid4())
            lancamento['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['financeiro'].append(lancamento)
            
            self.log(f"Lançamento financeiro criado: {lancamento['identificador']}")
            
            return {
                "message": "Lançamento financeiro criado com sucesso",
                "id": lancamento['id']
            }
        except Exception as e:
            self.log(f"Erro ao criar lançamento financeiro: {str(e)}")
            raise
    
    def criar_lancamento_contabil(self, lancamento):
        """Cria um lançamento contábil"""
        try:
            # Validação básica
            self.validar_campos(lancamento, ['identificador', 'data', 'valor', 'debito', 'credito'])
            
            # Adiciona ID e timestamp
            lancamento['id'] = str(uuid.uuid4())
            lancamento['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['contabil'].append(lancamento)
            
            self.log(f"Lançamento contábil criado: {lancamento['identificador']}")
            
            return {
                "message": "Lançamento contábil criado com sucesso",
                "id": lancamento['id']
            }
        except Exception as e:
            self.log(f"Erro ao criar lançamento contábil: {str(e)}")
            raise
    
    def emitir_nota_fiscal(self, nota_fiscal):
        """Emite uma nota fiscal"""
        try:
            # Validação básica
            self.validar_campos(nota_fiscal, ['numero', 'data', 'valor', 'cliente', 'itens'])
            
            # Adiciona ID e timestamp
            nota_fiscal['id'] = str(uuid.uuid4())
            nota_fiscal['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['fiscal'].append(nota_fiscal)
            
            self.log(f"Nota fiscal emitida: {nota_fiscal['numero']}")
            
            # Gera arquivo da nota fiscal
            self.gerar_arquivo_nota_fiscal(nota_fiscal)
            
            return {
                "message": "Nota fiscal emitida com sucesso",
                "id": nota_fiscal['id']
            }
        except Exception as e:
            self.log(f"Erro ao emitir nota fiscal: {str(e)}")
            raise
    
    def gerar_arquivo_nota_fiscal(self, nota_fiscal):
        """Gera um arquivo JSON com os dados da nota fiscal"""
        try:
            os.makedirs('notas_fiscais', exist_ok=True)
            arquivo = os.path.join('notas_fiscais', f"NF_{nota_fiscal['numero']}.json")
            
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(nota_fiscal, f, indent=2, ensure_ascii=False)
            
            self.log(f"Arquivo da nota fiscal gerado: {arquivo}")
        except Exception as e:
            self.log(f"Erro ao gerar arquivo da nota fiscal: {str(e)}")
    
    def cadastrar_funcionario(self, funcionario):
        """Cadastra um funcionário"""
        try:
            # Validação básica
            self.validar_campos(funcionario, ['matricula', 'nome', 'cpf', 'cargo', 'salario'])
            
            # Adiciona ID e timestamp
            funcionario['id'] = str(uuid.uuid4())
            funcionario['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['rh'].append(funcionario)
            
            self.log(f"Funcionário cadastrado: {funcionario['nome']}")
            
            return {
                "message": "Funcionário cadastrado com sucesso",
                "id": funcionario['id']
            }
        except Exception as e:
            self.log(f"Erro ao cadastrar funcionário: {str(e)}")
            raise
    
    def criar_pedido_compra(self, pedido):
        """Cria um pedido de compra"""
        try:
            # Validação básica
            self.validar_campos(pedido, ['numero', 'data', 'fornecedor', 'itens'])
            
            # Adiciona ID e timestamp
            pedido['id'] = str(uuid.uuid4())
            pedido['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['compras'].append(pedido)
            
            self.log(f"Pedido de compra criado: {pedido['numero']}")
            
            return {
                "message": "Pedido de compra criado com sucesso",
                "id": pedido['id']
            }
        except Exception as e:
            self.log(f"Erro ao criar pedido de compra: {str(e)}")
            raise
    
    def criar_pedido_venda(self, pedido):
        """Cria um pedido de venda"""
        try:
            # Validação básica
            self.validar_campos(pedido, ['numero', 'data', 'cliente', 'itens'])
            
            # Adiciona ID e timestamp
            pedido['id'] = str(uuid.uuid4())
            pedido['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['vendas'].append(pedido)
            
            self.log(f"Pedido de venda criado: {pedido['numero']}")
            
            return {
                "message": "Pedido de venda criado com sucesso",
                "id": pedido['id']
            }
        except Exception as e:
            self.log(f"Erro ao criar pedido de venda: {str(e)}")
            raise
    
    def cadastrar_produto(self, produto):
        """Cadastra um produto"""
        try:
            # Validação básica
            self.validar_campos(produto, ['codigo', 'descricao', 'unidade', 'preco'])
            
            # Adiciona ID e timestamp
            produto['id'] = str(uuid.uuid4())
            produto['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['estoque'].append(produto)
            
            self.log(f"Produto cadastrado: {produto['codigo']}")
            
            return {
                "message": "Produto cadastrado com sucesso",
                "id": produto['id']
            }
        except Exception as e:
            self.log(f"Erro ao cadastrar produto: {str(e)}")
            raise
    
    def cadastrar_bem(self, bem):
        """Cadastra um bem patrimonial"""
        try:
            # Validação básica
            self.validar_campos(bem, ['codigo', 'descricao', 'valor', 'dataAquisicao'])
            
            # Adiciona ID e timestamp
            bem['id'] = str(uuid.uuid4())
            bem['timestamp'] = datetime.now().isoformat()
            
            # Salva no "banco de dados"
            self.db['patrimonio'].append(bem)
            
            self.log(f"Bem patrimonial cadastrado: {bem['codigo']}")
            
            return {
                "message": "Bem patrimonial cadastrado com sucesso",
                "id": bem['id']
            }
        except Exception as e:
            self.log(f"Erro ao cadastrar bem patrimonial: {str(e)}")
            raise
    
    def exportar_dados(self):
        """Exporta todos os dados para arquivos JSON"""
        try:
            os.makedirs('dados_exportados', exist_ok=True)
            
            for modulo, dados in self.db.items():
                if dados:  # Só exporta se tiver dados
                    arquivo = os.path.join('dados_exportados', f"{modulo}.json")
                    
                    with open(arquivo, 'w', encoding='utf-8') as f:
                        json.dump(dados, f, indent=2, ensure_ascii=False)
                    
                    self.log(f"Dados do módulo {modulo} exportados para {arquivo}")
            
            return {"message": "Dados exportados com sucesso"}
        except Exception as e:
            self.log(f"Erro ao exportar dados: {str(e)}")
            raise
    
    def gerar_relatorio(self):
        """Gera um relatório com estatísticas dos dados"""
        try:
            relatorio = {
                "timestamp": datetime.now().isoformat(),
                "estatisticas": {}
            }
            
            for modulo, dados in self.db.items():
                relatorio["estatisticas"][modulo] = {
                    "total_registros": len(dados)
                }
                
                # Estatísticas específicas por módulo
                if modulo == 'financeiro' and dados:
                    total_receitas = sum(item['valor'] for item in dados if item['tipo'] == 'RECEITA')
                    total_despesas = sum(item['valor'] for item in dados if item['tipo'] == 'DESPESA')
                    relatorio["estatisticas"][modulo].update({
                        "total_receitas": total_receitas,
                        "total_despesas": total_despesas,
                        "saldo": total_receitas - total_despesas
                    })
                
                elif modulo == 'fiscal' and dados:
                    total_valor = sum(item['valor'] for item in dados)
                    relatorio["estatisticas"][modulo].update({
                        "total_valor_notas": total_valor,
                        "media_valor": total_valor / len(dados) if dados else 0
                    })
            
            # Salva o relatório
            os.makedirs('relatorios', exist_ok=True)
            arquivo = os.path.join('relatorios', f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
            
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(relatorio, f, indent=2, ensure_ascii=False)
            
            self.log(f"Relatório gerado: {arquivo}")
            
            return {
                "message": "Relatório gerado com sucesso",
                "arquivo": arquivo
            }
        except Exception as e:
            self.log(f"Erro ao gerar relatório: {str(e)}")
            raise


def simular_operacoes():
    """Executa a simulação de operações com o Nasajon"""
    print("=== Simulação de Integração com Nasajon (Local) ===")
    
    # Inicializa a simulação
    nasajon = SimulacaoNasajon()
    
    try:
        # 1. Financeiro - Criar lançamento (receita)
        lancamento_financeiro_receita = {
            "identificador": "LF001",
            "data": datetime.now().strftime("%Y-%m-%d"),
            "valor": 1500.00,
            "tipo": "RECEITA",
            "conta": "1001",
            "descricao": "Venda à vista"
        }
        
        resultado = nasajon.criar_lancamento_financeiro(lancamento_financeiro_receita)
        print(f"Financeiro - Criar lançamento (receita): {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # Financeiro - Criar lançamento (despesa)
        lancamento_financeiro_despesa = {
            "identificador": "LF002",
            "data": datetime.now().strftime("%Y-%m-%d"),
            "valor": 500.00,
            "tipo": "DESPESA",
            "conta": "2001",
            "descricao": "Pagamento de fornecedor"
        }
        
        resultado = nasajon.criar_lancamento_financeiro(lancamento_financeiro_despesa)
        print(f"Financeiro - Criar lançamento (despesa): {json.dumps(resultado, indent=2)}")
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
        
        resultado = nasajon.criar_lancamento_contabil(lancamento_contabil)
        print(f"Contábil - Criar lançamento: {json.dumps(resultado, indent=2)}")
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
        
        resultado = nasajon.emitir_nota_fiscal(nota_fiscal)
        print(f"Fiscal - Emitir nota fiscal: {json.dumps(resultado, indent=2)}")
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
        
        resultado = nasajon.cadastrar_funcionario(funcionario)
        print(f"RH - Cadastrar funcionário: {json.dumps(resultado, indent=2)}")
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
        
        resultado = nasajon.criar_pedido_compra(pedido_compra)
        print(f"Compras - Criar pedido: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # 6. Vendas - Criar pedido
        pedido_venda = {
            "numero": "PV001",
            "data": datetime.now().strftime("%Y-%m-%d"),
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
        
        resultado = nasajon.criar_pedido_venda(pedido_venda)
        print(f"Vendas - Criar pedido: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # 7. Estoque - Cadastrar produto
        produto = {
            "codigo": "P001",
            "descricao": "Produto Teste",
            "unidade": "UN",
            "preco": 100.00
        }
        
        resultado = nasajon.cadastrar_produto(produto)
        print(f"Estoque - Cadastrar produto: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # 8. Patrimônio - Cadastrar bem
        bem = {
            "codigo": "B001",
            "descricao": "Computador",
            "valor": 3000.00,
            "dataAquisicao": datetime.now().strftime("%Y-%m-%d")
        }
        
        resultado = nasajon.cadastrar_bem(bem)
        print(f"Patrimônio - Cadastrar bem: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # Exportar dados
        resultado = nasajon.exportar_dados()
        print(f"Exportação de dados: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        # Gerar relatório
        resultado = nasajon.gerar_relatorio()
        print(f"Geração de relatório: {json.dumps(resultado, indent=2)}")
        print("\n")
        
        print("=== Simulação concluída com sucesso ===")
    
    except Exception as e:
        print(f"ERRO: {str(e)}")
        print("Simulação interrompida devido a um erro.")


if __name__ == "__main__":
    simular_operacoes()