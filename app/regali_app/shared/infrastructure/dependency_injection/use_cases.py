from injector import singleton
from app.regali_app.list.application.use_cases import get_gift_list
from app.regali_app.list.application.use_cases import get_gift_lists
from app.regali_app.list.application.use_cases import delete_gift_list
from app.regali_app.list.application.use_cases import create_gift_list
from app.regali_app.list.application.use_cases import delete_gift_list_element


def configure_use_cases(binder):
    binder.bind(get_gift_list.UseCase, to=get_gift_list.UseCase, scope=singleton)
    binder.bind(get_gift_lists.UseCase, to=get_gift_lists.UseCase, scope=singleton)
    binder.bind(delete_gift_list.UseCase, to=delete_gift_list.UseCase, scope=singleton)
    binder.bind(create_gift_list.UseCase, to=create_gift_list.UseCase, scope=singleton)
    binder.bind(delete_gift_list_element.UseCase, to=delete_gift_list_element.UseCase, scope=singleton)
