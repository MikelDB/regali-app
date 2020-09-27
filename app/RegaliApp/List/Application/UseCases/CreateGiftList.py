from injector import inject
import sys
from app.RegaliApp.List.Domain.Services.CreateGiftList import CreateGiftList
from app.RegaliApp.List.Domain.Factories.GiftListFactory import GiftListFactory

class Request:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class UseCase:
    @inject
    def __init__(self, create_gift_list_service: CreateGiftList, gift_list_factory: GiftListFactory):
        print('Pre', file=sys.stdout)
        self.create_gift_list_service = create_gift_list_service
        self.gift_list_factory = gift_list_factory
        print('Created', file=sys.stdout)

    def execute(self, request: Request):
        gift_list = self.gift_list_factory.build_gift_list_from_parameters(request.user_id, request.name)
        return self.create_gift_list_service.execute(gift_list)