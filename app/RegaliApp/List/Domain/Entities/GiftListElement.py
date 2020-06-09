class GiftListElement:
    def __init__(self, id, reference, list_id, name, url, updated_at, created_at):
        self.id = id
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

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False