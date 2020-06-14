from injector import singleton
from app.RegaliApp.List.Domain.Services.GetGiftListByReferenceService import GetGiftListByReferenceService
from app.RegaliApp.List.Domain.Services.GetAllGiftLists import GetAllGiftLists


def configure_services(binder):
    binder.bind(GetGiftListByReferenceService, to=GetGiftListByReferenceService, scope=singleton)
    binder.bind(GetAllGiftLists, to=GetAllGiftLists, scope=singleton)