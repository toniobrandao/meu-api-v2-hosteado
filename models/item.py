# Essa instância do SQLAlchemy tem propriedades que nós vamos usar para definir quais tabelas vamos usar em nossa
# aplicação e quais colunas essas tabelas vão ter. Além disso, o SQLAlchemy também vai transformar, para as classes que vamos criar,
# as linhas em objetos do python.
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(80), unique=False, nullable=False)

    # A pack_id é usada como chave estrangeira da coluna id da tabela pack.
    pack_id = db.Column(db.Integer, db.ForeignKey(
        "packs.id"), nullable=False)
    
    # Queremos que seja pego o objeto da loja que possua esse pack_id.
    pack = db.relationship(
        "PackModel", back_populates="items", uselist=False)
