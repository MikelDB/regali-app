from injector import inject
from app.regali_app.list.domain.services.create_gift_list_element import CreateGiftListElement
from app.regali_app.list.domain.factories.gift_list_element_factory import GiftListElementFactory
from app.regali_app.list.domain.services.get_gift_list_by_reference import GetGiftListByReferenceService


class Request:
    def __init__(self, list_reference, url):
        self.list_reference = list_reference
        self.url = url

class Response:
    def __init__(self, gift_list):
        self.gift_list = gift_list

class ResponseDataTransformer:
    def transform(self, response) -> dict:
        pass

class UseCase:
    @inject
    def __init__(
        self, create_gift_list_element_service: CreateGiftListElement,
        gift_list_element_factory: GiftListElementFactory,
        response_data_transformer: ResponseDataTransformer,
        get_gift_list_by_reference_service: GetGiftListByReferenceService
    ):
        self.create_gift_list_element_service = create_gift_list_element_service
        self.gift_list_element_factory = gift_list_element_factory
        self.response_data_transformer = response_data_transformer
        self.get_gift_list_by_reference_service = get_gift_list_by_reference_service

    def execute(self, request: Request) -> dict:
        gift_list = self.get_gift_list_by_reference_service.execute(request.list_reference)

        gift_list_element = self.gift_list_element_factory.build_gift_list_element_from_parameters(
            gift_list.id,
            request.url
        )

        self.create_gift_list_element_service.execute(gift_list_element)

        return self.response_data_transformer.transform(
            Response(
                self.get_gift_list_by_reference_service.execute(request.list_reference)
            )
        )
