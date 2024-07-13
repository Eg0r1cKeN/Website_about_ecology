import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class UserFile(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'files'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    heading = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    owner = sqlalchemy.Column(sqlalchemy.Integer)
    directory = sqlalchemy.Column(sqlalchemy.String)
    hash = sqlalchemy.Column(sqlalchemy.String)