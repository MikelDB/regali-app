from app.RegaliApp.List.Application.UseCases.GetGiftList import DataTransformer

class ToDictDataTransformer(DataTransformer):
    def transform(self, list):
        transformedList = {
            'name': list.name,
            'reference': list.reference,
            'created_at': list.created_at,
            'active': list.active
        }

        return transformedList