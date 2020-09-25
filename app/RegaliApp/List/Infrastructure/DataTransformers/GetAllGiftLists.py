from app.RegaliApp.List.Application.UseCases.GetGiftLists import DataTransformer

class ToDictDataTransformer(DataTransformer):
    def transform(self, lists):
        transformedLists = {
            'lists': []
        }

        for GiftList in lists:
            transformedLists['lists'].append({
                'name': GiftList.name,
                'reference': GiftList.reference,
                'created_at': GiftList.created_at,
                'active': GiftList.active
            })

        return transformedLists