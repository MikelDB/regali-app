from app.regali_app.list.application.use_cases.get_gift_lists import DataTransformer

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