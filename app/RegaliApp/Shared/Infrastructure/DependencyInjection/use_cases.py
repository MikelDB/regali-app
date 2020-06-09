from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList


def configure_use_cases(binder):
    binder.bind(GetGiftList.UseCase, to=GetGiftList.UseCase, scope=singleton)