from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Infrastructure.DataTransformers.GetGiftList import ToDictDataTransformer


def configure_data_transformers(binder):
    binder.bind(GetGiftList.DataTransformer, to=ToDictDataTransformer, scope=singleton)