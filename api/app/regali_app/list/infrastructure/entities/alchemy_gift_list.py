# pylint: disable=E1101
from datetime import datetime
from sqlalchemy.orm import mapper, relationship

from app.regali_app.list.domain.entities.gift_list import GiftList
from app.regali_app.list.domain.entities.gift_list_element import GiftListElement

from app import db


metadata = db.MetaData()

class AlchemyGiftList(GiftList):
    pass

class AlchemyGiftListElement(GiftListElement):
    pass

alchemy_gift_list = db.Table(
    'list',
    metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('reference', db.String(50)),
    db.Column('user_id', db.Integer),
    db.Column('name', db.String(64)),
    db.Column('public', db.Boolean),
    db.Column('active', db.Boolean),
    db.Column('updated_at', db.DateTime, default=datetime.now, onupdate=datetime.now),
    db.Column('created_at', db.DateTime, default=datetime.now)
)

alchemy_gift_list_element = db.Table(
    'list_element',
    metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('reference', db.String(50)),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id')),
    db.Column('name', db.String(64)),
    db.Column('url', db.Text),
    db.Column('updated_at', db.DateTime, default=datetime.now, onupdate=datetime.now),
    db.Column('created_at', db.DateTime, default=datetime.now)
)

mapper(AlchemyGiftList, alchemy_gift_list, properties={
    'elements': relationship(
        AlchemyGiftListElement,
        backref='list_element',
        order_by=alchemy_gift_list_element.c.id,
        cascade="save-update, merge, delete"
    )
})

mapper(AlchemyGiftListElement, alchemy_gift_list_element)
