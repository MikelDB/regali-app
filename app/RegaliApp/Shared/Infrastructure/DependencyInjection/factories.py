from injector import singleton
from app.RegaliApp.List.Domain.Factories.GiftListFactory import GiftListFactory
from app.RegaliApp.List.Infrastructure.Factories.AlchemyGiftListFactory import AlchemyGiftListFactory


def configure_factories(binder):
    binder.bind(GiftListFactory, to=AlchemyGiftListFactory, scope=singleton)
