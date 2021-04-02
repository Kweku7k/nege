from app import db

class Courses(db.Model):
    tablename = ['Vendor']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    startDate = db.Column(db.dateTime)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_ended = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Vendor('{self.id}', '{self.name}')"
