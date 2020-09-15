from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Application.UseCases import GetGiftLists
from app.RegaliApp.List.Application.UseCases import DeleteGiftList
from app.RegaliApp.List.Application.UseCases import CreateGiftList


def configure_use_cases(binder):
    binder.bind(GetGiftList.UseCase, to=GetGiftList.UseCase, scope=singleton)
    binder.bind(GetGiftLists.UseCase, to=GetGiftLists.UseCase, scope=singleton)
    binder.bind(DeleteGiftList.UseCase, to=DeleteGiftList.UseCase, scope=singleton)
    binder.bind(CreateGiftList.UseCase, to=CreateGiftList.UseCase, scope=singleton)