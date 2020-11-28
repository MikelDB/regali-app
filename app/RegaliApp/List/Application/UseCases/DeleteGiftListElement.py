from injector import inject
from app.RegaliApp.List.Domain.Services.DeleteGiftListElementByReference import DeleteGiftListElementByReference

class Request:
    def __init__(self, list_reference, element_reference):
        self.list_reference = list_reference
        self.element_reference = element_reference


class UseCase:
    @inject
    def __init__(self, delete_gift_list_element_by_reference: DeleteGiftListElementByReference):
        self.delete_gift_list_element_by_reference = delete_gift_list_element_by_reference

    def execute(self, request):
        self.delete_gift_list_element_by_reference.execute(request.element_reference)
        
