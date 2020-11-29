from app.regali_app.list.application.use_cases.create_gift_list import RequestDataTransformer, Request, ResponseDataTransformer, Response

class FlaskRequestToCreateGiftListRequest(RequestDataTransformer):
    def transform(self, user_id, request) -> Request:
        return Request(
            user_id,
            request.json['name'],
            self.transformElements(request.json['elements'])
        )

    @staticmethod
    def transformElements(elements):
        transformedElements = []

        for element in elements:
            transformedElements.append(
                {
                    'id' : element['id'] if ('id' in element) else None,
                    'name' : element['name'],
                    'url' : element['url'],
                }
            )
        
        return transformedElements

class ToDictDataTransformer(ResponseDataTransformer):
    def transform(self, response: Response):
        return {
            'name': response.gift_list.name,
            'active': response.gift_list.active,
            'reference': response.gift_list.reference,
            'created_at': response.gift_list.created_at,
            'elements': self.transformElements(response.gift_list.elements)
        }

    @staticmethod
    def transformElements(elements):
        transformedElements = []

        for element in elements:
            transformedElements.append(
                {
                    'reference' : element.reference,
                    'name' : element.name,
                    'url' : element.url,
                }
            )
        
        return transformedElements
