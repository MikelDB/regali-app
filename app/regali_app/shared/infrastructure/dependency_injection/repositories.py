# pylint: disable=C0301
from injector import singleton
from app.regali_app.list.domain.repositories.gift_list_repository import GiftListRepository
from app.regali_app.list.domain.repositories.gift_list_element_repository import GiftListElementRepository

from app.regali_app.list.infrastructure.repositories.alchemy_gift_list_repository import AlchemyGiftListRepository
from app.regali_app.list.infrastructure.repositories.alchemy_gift_list_element_repository import AlchemyGiftListElementRepository


def configure(binder):
    binder.bind(GiftListRepository, to=AlchemyGiftListRepository, scope=singleton)
    binder.bind(GiftListElementRepository, to=AlchemyGiftListElementRepository, scope=singleton)
