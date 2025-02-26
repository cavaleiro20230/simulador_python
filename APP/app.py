from flask import Flask, request, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import logging
import json
import os
from datetime import datetime
import uuid

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("api.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

# Simulação de banco de dados
db = {
    'financeiro': [],
    'contabil': [],
    'fiscal': [],
    'rh': [],
    'compras': [],
    'vendas': [],
    'estoque': [],
    'patrimonio': []
}

# Garantir que o diretório static existe
os.makedirs('static', exist_ok=True)

# Gerar o arquivo swagger.json
def generate_swagger_json():
    swagger_path = os.path.join('static', 'swagger.json')
    with open(swagger_path, 'r') as f:
        swagger_content = json.load(f)
    return swagger_content

# Configuração do Swagger
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Nasajon API Simulation"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Middleware para autenticação
@app.before_request
def authenticate():
    # Ignorar autenticação para swagger e static files
    if request.path.startswith(SWAGGER_URL) or request.path.startswith('/static'):
        return
    
    # Ignorar autenticação para a rota de status
    if request.path == '/api/status':
        return
    
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key != os.environ.get('NASAJON_API_KEY', 'api_key_simulada'):
        return jsonify({"error": "Unauthorized"}), 401

# Rotas para o módulo Financeiro
@app.route('/api/financeiro/lancamentos', methods=['POST'])
def criar_lancamento_financeiro():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['identificador', 'data', 'valor', 'tipo', 'conta']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['financeiro'].append(data)
        
        logging.info(f"Lançamento financeiro criado: {data['identificador']}")
        
        return jsonify({
            "message": "Lançamento financeiro criado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao criar lançamento financeiro: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/api/financeiro/lancamentos', methods=['GET'])
def listar_lancamentos_financeiros():
    try:
        return jsonify(db['financeiro']), 200
    except Exception as e:
        logging.error(f"Erro ao listar lançamentos financeiros: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Contábil
@app.route('/api/contabil/lancamentos', methods=['POST'])
def criar_lancamento_contabil():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['identificador', 'data', 'valor', 'debito', 'credito']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['contabil'].append(data)
        
        logging.info(f"Lançamento contábil criado: {data['identificador']}")
        
        return jsonify({
            "message": "Lançamento contábil criado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao criar lançamento contábil: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Fiscal
@app.route('/api/fiscal/notas-fiscais', methods=['POST'])
def emitir_nota_fiscal():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['numero', 'data', 'valor', 'cliente', 'itens']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['fiscal'].append(data)
        
        logging.info(f"Nota fiscal emitida: {data['numero']}")
        
        return jsonify({
            "message": "Nota fiscal emitida com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao emitir nota fiscal: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo RH
@app.route('/api/rh/funcionarios', methods=['POST'])
def cadastrar_funcionario():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['matricula', 'nome', 'cpf', 'cargo', 'salario']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['rh'].append(data)
        
        logging.info(f"Funcionário cadastrado: {data['nome']}")
        
        return jsonify({
            "message": "Funcionário cadastrado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao cadastrar funcionário: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Compras
@app.route('/api/compras/pedidos', methods=['POST'])
def criar_pedido_compra():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['numero', 'data', 'fornecedor', 'itens']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['compras'].append(data)
        
        logging.info(f"Pedido de compra criado: {data['numero']}")
        
        return jsonify({
            "message": "Pedido de compra criado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao criar pedido de compra: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Vendas
@app.route('/api/vendas/pedidos', methods=['POST'])
def criar_pedido_venda():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['numero', 'data', 'cliente', 'itens']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['vendas'].append(data)
        
        logging.info(f"Pedido de venda criado: {data['numero']}")
        
        return jsonify({
            "message": "Pedido de venda criado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao criar pedido de venda: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Estoque
@app.route('/api/estoque/produtos', methods=['POST'])
def cadastrar_produto():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['codigo', 'descricao', 'unidade', 'preco']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['estoque'].append(data)
        
        logging.info(f"Produto cadastrado: {data['codigo']}")
        
        return jsonify({
            "message": "Produto cadastrado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao cadastrar produto: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rotas para o módulo Patrimônio
@app.route('/api/patrimonio/bens', methods=['POST'])
def cadastrar_bem():
    try:
        data = request.json
        
        # Validação básica
        required_fields = ['codigo', 'descricao', 'valor', 'dataAquisicao']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
        
        # Adiciona ID e timestamp
        data['id'] = str(uuid.uuid4())
        data['timestamp'] = datetime.now().isoformat()
        
        # Salva no "banco de dados"
        db['patrimonio'].append(data)
        
        logging.info(f"Bem patrimonial cadastrado: {data['codigo']}")
        
        return jsonify({
            "message": "Bem patrimonial cadastrado com sucesso",
            "id": data['id']
        }), 201
    except Exception as e:
        logging.error(f"Erro ao cadastrar bem patrimonial: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rota para status da API
@app.route('/api/status', methods=['GET'])
def status():
    try:
        return jsonify({
            "status": "online",
            "timestamp": datetime.now().isoformat(),
            "modules": list(db.keys())
        }), 200
    except Exception as e:
        logging.error(f"Erro ao verificar status: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rota para servir arquivos estáticos
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Cria o diretório static se não existir
    os.makedirs('static', exist_ok=True)
    
    # Inicia o servidor
    app.run(debug=True, host='0.0.0.0', port=5000)