from injector import singleton
from app.RegaliApp.List.Domain.Services.GetGiftListByReferenceService import GetGiftListByReferenceService
from app.RegaliApp.List.Domain.Services.GetAllGiftLists import GetAllGiftLists
from app.RegaliApp.List.Domain.Services.DeleteGiftListByReference import DeleteGiftListByReference
from app.RegaliApp.List.Domain.Services.CreateGiftList import CreateGiftList


def configure_services(binder):
    binder.bind(GetGiftListByReferenceService, to=GetGiftListByReferenceService, scope=singleton)
    binder.bind(GetAllGiftLists, to=GetAllGiftLists, scope=singleton)
    binder.bind(DeleteGiftListByReference, to=DeleteGiftListByReference, scope=singleton)
    binder.bind(CreateGiftList, to=CreateGiftList, scope=singleton)