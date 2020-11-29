class GiftListElement:
    def __init__(self, gift_list_element_id, reference, list_id, name, url, updated_at, created_at):
        # pylint: disable=C0103 # for now is necessary for sql alchemy
        self.id = gift_list_element_id
        self.reference = reference
        self.list_id = list_id
        self.name = name
        self.url = url
        self.updated_at = updated_at
        self.created_at = created_at

    def __repr__(self):
        return '<GiftListElement {}>'.format(self.id)

    def get_id(self):
        return self.id

    @staticmethod
    def is_anonymous():
        """False, as anonymous users aren't supported."""
        return False
