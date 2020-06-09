from injector import singleton
from app.RegaliApp.List.Application.UseCases.GetGiftList.GetGiftList import GetGiftListUseCase


def configure_use_cases(binder):
    binder.bind(GetGiftListUseCase, to=GetGiftListUseCase, scope=singleton)