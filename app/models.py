from app import db

class Partnum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partnumber = db.Column(db.String(64), index=True)
    location = db.Column(db.String(10))
    quantity = db.Column(db.Integer)
    description = db.Column(db.String(128))

    def __repr__(self):
       return '<Partnum {}>'.format(self.partnumber)