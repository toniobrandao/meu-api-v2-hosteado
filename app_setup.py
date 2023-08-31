from db import db
from models import PackModel

def create_initial_packs():
    initial_pack_data = [
        {"name": "Acampamento"},
        {"name": "Casa de Campo"},
        {"name": "Casa de Amigo"},
        {"name": "Hostel"},
        {"name": "Hotel"},
        {"name": "Resort"},
        {"name": "AirBnb"},
    ]

    try:
        for pack_data in initial_pack_data:
            pack = PackModel(**pack_data)
            db.session.add(pack)

        db.session.commit()
        print("Initial packs added successfully.")
    except Exception as e:
        db.session.rollback()  # Rollback changes on exception
        print("Error adding initial packs:", e)
