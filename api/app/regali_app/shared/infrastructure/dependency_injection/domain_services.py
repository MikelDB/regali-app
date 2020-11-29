from injector import singleton
from app.regali_app.list.domain.services.get_gift_list_by_reference import GetGiftListByReferenceService
from app.regali_app.list.domain.services.get_all_gift_lists import GetAllGiftLists
from app.regali_app.list.domain.services.delete_gift_list_by_reference import DeleteGiftListByReference
from app.regali_app.list.domain.services.create_gift_list import CreateGiftList


def configure_services(binder):
    binder.bind(GetGiftListByReferenceService, to=GetGiftListByReferenceService, scope=singleton)
    binder.bind(GetAllGiftLists, to=GetAllGiftLists, scope=singleton)
    binder.bind(DeleteGiftListByReference, to=DeleteGiftListByReference, scope=singleton)
    binder.bind(CreateGiftList, to=CreateGiftList, scope=singleton)
