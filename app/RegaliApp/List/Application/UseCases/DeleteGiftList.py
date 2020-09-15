from injector import inject
from app.RegaliApp.List.Domain.Services.DeleteGiftListByReference import DeleteGiftListByReference

class Request:
    def __init__(self, list_reference):
        self.list_reference = list_reference


class UseCase:
    @inject
    def __init__(self, delete_gift_list_by_reference: DeleteGiftListByReference):
        self.delete_gift_list_by_reference = delete_gift_list_by_reference

    def execute(self, request):
        self.delete_gift_list_by_reference.execute(request.list_reference)
        
