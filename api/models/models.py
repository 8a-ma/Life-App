from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DailyToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    date_start = db.Column(db.Date, nullable=False)
    date_finish = db.Column(db.Date)
    completed = db.Column(db.Boolean, nullable=False)
    


class YearAgenda(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)


class AnnualEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)




class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)



class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(10), nullable=False)
    progress = db.Column(db.Integer, nullalble=False)

class Courses_Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    course_id = db.Column(db.Integer, db.ForeignKey(Courses.id))
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

class Companys(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

class WorkJournal(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    id_company = db.Column(db.Integer, db.ForeignKey(Companys.id))
    title = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    description = db.Column(db.Text)


