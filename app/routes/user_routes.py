from flask import Blueprint, jsonify, request
from app.models.user import User
from app import db

user_bp = Blueprint('user', __name__, url_prefix='/api')


@user_bp.route('/')
def welcome():
    """
    Bem vindo endpoint
    ---
    responses:
      200:
        description: Mensagem de boas-vindas
    """
    return {"message": "Bem-vindo à API de Usuários"}


@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Lista todos os usuários
    ---
    parameters:
      - name: search
        in: query
        type: string
        required: false
        description: Busca usuários pelo nome
    responses:
      200:
        description: Lista de usuários
    """
    search = request.args.get('search')

    if search:
        users = User.query.filter(User.name.like(f'%{search}%')).all()
    else:
        users = User.query.all()

    return jsonify([{"id": user.id, "name": user.name, "age": user.age} for user in users])


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
   Obtém um usuário
   ---
   parameters:
     - name: user_id
       in: path
       type: integer
       required: true
   responses:
     200:
       description: Detalhes do usuário
   """
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "age": user.age})


@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Cria um novo usuário
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      201:
        description: Usuário criado
    """
    data = request.get_json()
    user = User(name=data['name'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "age": user.age}), 201


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Atualiza um usuário
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            age:
              type: integer
    responses:
      200:
        description: Usuário atualizado
    """
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data['name']
    user.age = data['age']
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "age": user.age})


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Remove um usuário
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Usuário removido
    """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
