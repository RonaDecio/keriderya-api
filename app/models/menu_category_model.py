import uuid

from sqlalchemy.dialects.mysql import CHAR

from app.extension import db

class MenuCategoryModel(db.Model):
    __tablename__ = "menu_category"

    menu_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
