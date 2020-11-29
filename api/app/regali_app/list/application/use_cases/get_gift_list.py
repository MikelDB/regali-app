from injector import inject
from app.regali_app.list.domain.services.get_gift_list_by_reference import GetGiftListByReferenceService

class Request:
    def __init__(self, list_reference):
        self.list_reference = list_reference


class DataTransformer:
    def transform(self, gift_list):
        pass


class UseCase:
    @inject
    def __init__(self, get_gift_list_by_reference: GetGiftListByReferenceService, data_transformer: DataTransformer):
        self.get_gift_list_by_reference = get_gift_list_by_reference
        self.data_transformer = data_transformer

    def execute(self, request):
        return self.data_transformer.transform(
            self.get_gift_list_by_reference.execute(request.list_reference)
        )
