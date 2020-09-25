from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Infrastructure.DataTransformers.GetGiftList import ToDictDataTransformer

from app.RegaliApp.List.Application.UseCases import GetGiftLists
from app.RegaliApp.List.Infrastructure.DataTransformers import GetAllGiftLists 


def configure_data_transformers(binder):
    binder.bind(GetGiftList.DataTransformer, to=ToDictDataTransformer, scope=singleton)
    binder.bind(GetGiftLists.DataTransformer, to=GetAllGiftLists.ToDictDataTransformer, scope=singleton)
    