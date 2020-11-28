from injector import singleton
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository
from app.RegaliApp.List.Domain.Repositories.GiftListElementRepository import GiftListElementRepository

from app.RegaliApp.List.Infrastructure.Repositories.AlchemyGiftListRepository import AlchemyGiftListRepository
from app.RegaliApp.List.Infrastructure.Repositories.AlchemyGiftListElementRepository import AlchemyGiftListElementRepository


def configure(binder):
    binder.bind(GiftListRepository, to=AlchemyGiftListRepository, scope=singleton)
    binder.bind(GiftListElementRepository, to=AlchemyGiftListElementRepository, scope=singleton)