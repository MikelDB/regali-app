class GiftList:
    def __init__(self, gift_list_id, reference, user_id, name, active, public, updated_at, created_at):
        # pylint: disable=C0103 #id is a requirement for sqlalchemy
        self.id = gift_list_id
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

    @staticmethod
    def is_anonymous():
        """False, as anonymous users aren't supported."""
        return False
