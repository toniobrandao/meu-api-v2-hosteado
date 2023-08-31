# Essa instância do SQLAlchemy tem propriedades que nós vamos usar para definir quais tabelas vamos usar em nossa
# aplicação e quais colunas essas tabelas vão ter. Além disso, o SQLAlchemy também vai transformar, para as classes que vamos criar,
# as linhas em objetos do python.
from db import db

class PackModel(db.Model):
    __tablename__ = "packs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # cria uma relação na base de dados onde os "items" estão associados ao modelo "ItemModel" por meio do campo "pack",
    # permitindo acesso flexível e dinâmico aos itens relacionados.
    items = db.relationship(
        "ItemModel", back_populates="pack", lazy=True, cascade="all,delete")  # cascade = all, delete, deleta todos os items da pack após deletar a pack.



