class GiftList:
    def __init__(self, id, reference, user_id, name, active, public, updated_at, created_at):
        self.id = id
        self.reference = reference
        self.user_id = user_id
        self.name = name
        self.active = active
        self.public = public
        self.updated_at = updated_at
        self.created_at = created_at
        self.elements = []

    def __repr__(self):
        return '<GiftList {}>'.format(self.id)

    def get_id(self):
        return self.id

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False