from app import db
from app.models import Partnum
db.create_all()
db.session.add(Partnum("wr30x10093","S",2,"none"))
db.session.commit()