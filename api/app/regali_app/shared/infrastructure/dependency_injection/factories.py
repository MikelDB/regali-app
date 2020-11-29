from injector import singleton
from app.regali_app.list.domain.factories.gift_list_factory import GiftListFactory
from app.regali_app.list.domain.factories.gift_list_element_factory import GiftListElementFactory

from app.regali_app.list.infrastructure.factories.alquemy_gift_list_factory import AlchemyGiftListFactory
from app.regali_app.list.infrastructure.factories.alchemy_gift_list_element_factory import AlchemyGiftListElementFactory



def configure_factories(binder):
    binder.bind(GiftListFactory, to=AlchemyGiftListFactory, scope=singleton)
    binder.bind(GiftListElementFactory, to=AlchemyGiftListElementFactory, scope=singleton)
