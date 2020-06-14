from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Application.UseCases import GetGiftLists


def configure_use_cases(binder):
    binder.bind(GetGiftList.UseCase, to=GetGiftList.UseCase, scope=singleton)
    binder.bind(GetGiftLists.UseCase, to=GetGiftLists.UseCase, scope=singleton)