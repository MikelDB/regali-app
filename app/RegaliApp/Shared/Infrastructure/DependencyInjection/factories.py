from injector import singleton
from app.RegaliApp.List.Domain.Factories.GiftListFactory import GiftListFactory
from app.RegaliApp.List.Domain.Factories.GiftListElementFactory import GiftListElementFactory

from app.RegaliApp.List.Infrastructure.Factories.AlchemyGiftListFactory import AlchemyGiftListFactory
from app.RegaliApp.List.Infrastructure.Factories.AlchemyGiftListElementFactory import AlchemyGiftListElementFactory



def configure_factories(binder):
    binder.bind(GiftListFactory, to=AlchemyGiftListFactory, scope=singleton)
    binder.bind(GiftListElementFactory, to=AlchemyGiftListElementFactory, scope=singleton)
