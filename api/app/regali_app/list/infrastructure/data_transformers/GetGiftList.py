from app.regali_app.list.application.use_cases.get_gift_list import DataTransformer

class ToDictDataTransformer(DataTransformer):
    def transform(self, list):
        transformedList = {
            'name': list.name,
            'reference': list.reference,
            'created_at': list.created_at,
            'active': list.active,
            'elements': self.transformGiftListElements(list.elements),
        }

        return transformedList

    def transformGiftListElements(self, gift_list_elements):
        tranformedGiftListElements = []

        for gift_list_element in gift_list_elements:
            tranformedGiftListElements.append({
                'name': gift_list_element.name,
                'url': gift_list_element.url,
                'reference': gift_list_element.reference
            })

        return tranformedGiftListElements