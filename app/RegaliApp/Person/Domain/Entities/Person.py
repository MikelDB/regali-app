class Person:
    def __init__(self, id, public_id, google_id, name, email, is_active, is_authenticated, profile_pic, password):
        self.id = id
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

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
