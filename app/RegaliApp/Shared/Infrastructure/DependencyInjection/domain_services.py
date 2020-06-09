from injector import singleton
from app.RegaliApp.List.Domain.Services.GetGiftListByReferenceService import GetGiftListByReferenceService


def configure_services(binder):
    binder.bind(GetGiftListByReferenceService, to=GetGiftListByReferenceService, scope=singleton)