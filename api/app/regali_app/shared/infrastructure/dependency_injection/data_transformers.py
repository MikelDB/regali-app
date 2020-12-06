# pylint: disable=C0301
from injector import singleton
from app.regali_app.list.application.use_cases import get_gift_list
from app.regali_app.list.infrastructure.data_transformers.get_gift_list import ToDictDataTransformer

from app.regali_app.list.application.use_cases import get_gift_lists
from app.regali_app.list.infrastructure.data_transformers import get_all_gift_lists

from app.regali_app.list.application.use_cases import create_gift_list
from app.regali_app.list.infrastructure.data_transformers.create_gift_list import FlaskRequestToCreateGiftListRequest
from app.regali_app.list.infrastructure.data_transformers.create_gift_list import ToDictDataTransformer as CreateGiftListToDictDataTransformer

from app.regali_app.list.application.use_cases import create_gift_list_element

def configure_data_transformers(binder):
    binder.bind(get_gift_list.DataTransformer, to=ToDictDataTransformer, scope=singleton)
    binder.bind(get_gift_lists.DataTransformer, to=get_all_gift_lists.ToDictDataTransformer, scope=singleton)
    binder.bind(create_gift_list.RequestDataTransformer, to=FlaskRequestToCreateGiftListRequest, scope=singleton)
    binder.bind(create_gift_list.ResponseDataTransformer, to=CreateGiftListToDictDataTransformer, scope=singleton)
    binder.bind(create_gift_list_element.ResponseDataTransformer, to=CreateGiftListToDictDataTransformer, scope=singleton)
