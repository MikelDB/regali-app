class Person:
    def __init__(
        self,
        person_id,
        public_id,
        google_id,
        name,
        email,
        is_active,
        is_authenticated,
        profile_pic,
        password
    ):
        # pylint: disable=C0103 #id is a requirement for sqlalchemy
        self.id = person_id
        self.public_id = public_id
        self.google_id = google_id
        self.name = name
        self.email = email
        self.is_active = is_active
        self.is_authenticated = is_authenticated
        self.profile_pic = profile_pic
        self.password = password

    def __repr__(self):
        return '<Person {}>'.format(self.id)

    def get_id(self):
        return self.id

    @staticmethod
    def is_anonymous():
        """False, as anonymous users aren't supported."""
        return False
