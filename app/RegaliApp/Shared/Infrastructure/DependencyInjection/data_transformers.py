from injector import singleton
from app.RegaliApp.List.Application.UseCases import GetGiftList
from app.RegaliApp.List.Infrastructure.DataTransformers.GetGiftList import ToDictDataTransformer

from app.RegaliApp.List.Application.UseCases import GetGiftLists
from app.RegaliApp.List.Infrastructure.DataTransformers import GetAllGiftLists 

from app.RegaliApp.List.Application.UseCases import CreateGiftList
from app.RegaliApp.List.Infrastructure.DataTransformers.CreateGiftList import FlaskRequestToCreateGiftListRequest
from app.RegaliApp.List.Infrastructure.DataTransformers.CreateGiftList import ToDictDataTransformer as CreateGiftListToDictDataTransformer

from app.RegaliApp.List.Application.UseCases import CreateGiftListElement

def configure_data_transformers(binder):
    binder.bind(GetGiftList.DataTransformer, to=ToDictDataTransformer, scope=singleton)
    binder.bind(GetGiftLists.DataTransformer, to=GetAllGiftLists.ToDictDataTransformer, scope=singleton)
    binder.bind(CreateGiftList.RequestDataTransformer, to=FlaskRequestToCreateGiftListRequest, scope=singleton)
    binder.bind(CreateGiftList.ResponseDataTransformer, to=CreateGiftListToDictDataTransformer, scope=singleton)
    binder.bind(CreateGiftListElement.ResponseDataTransformer, to=CreateGiftListToDictDataTransformer, scope=singleton)