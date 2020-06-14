from injector import inject
from app.RegaliApp.List.Domain.Services.GetAllGiftLists import GetAllGiftLists

class DataTransformer:
    def transform(self, list):
        pass


class UseCase:
    @inject
    def __init__(self, get_all_gift_lists: GetAllGiftLists, data_transformer: DataTransformer):
        self.get_all_gift_lists = get_all_gift_lists
        self.data_transformer = data_transformer

    def execute(self):
        return self.data_transformer.transform(
            self.get_all_gift_lists.execute()
        )
