from injector import inject
import sys
from app.RegaliApp.List.Domain.Services.CreateGiftList import CreateGiftList
from app.RegaliApp.List.Domain.Factories.GiftListFactory import GiftListFactory
from app.RegaliApp.List.Domain.Entities.GiftList import GiftList

class Request:
    def __init__(self, user_id, name, list_elements):
        self.user_id = user_id
        self.name = name
        self.list_elements = list_elements


class RequestDataTransformer:
    def transform(self, user_id, request) -> Request:
        pass

class Response:
    def __init__(self, gift_list):
        self.gift_list = gift_list

class ResponseDataTransformer:
    def transform(self, response) -> dict:
        pass

class UseCase:
    @inject
    def __init__(self, create_gift_list_service: CreateGiftList, gift_list_factory: GiftListFactory, response_data_transformer: ResponseDataTransformer):
        self.create_gift_list_service = create_gift_list_service
        self.gift_list_factory = gift_list_factory
        self.response_data_transformer = response_data_transformer

    def execute(self, request: Request) -> dict:
        gift_list = self.gift_list_factory.build_gift_list_from_parameters(request.user_id, request.name, request.list_elements)
        return self.response_data_transformer.transform(
            Response(
                self.create_gift_list_service.execute(gift_list)
            )
        )