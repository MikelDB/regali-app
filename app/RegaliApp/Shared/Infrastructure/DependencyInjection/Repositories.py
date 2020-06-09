from injector import singleton
from app.RegaliApp.List.Domain.Repositories.GiftListRepository import GiftListRepository
from app.RegaliApp.List.Infrastructure.Repositories.AlchemyGiftListRepository import AlchemyGiftListRepository


def configure(binder):
    binder.bind(GiftListRepository, to=AlchemyGiftListRepository, scope=singleton)