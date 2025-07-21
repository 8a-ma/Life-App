from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DailyToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.Date, nullable=False)


class YearAgenda(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    year = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)


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
    # archived = db.Column(db.Boolean, nullable=True)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    # archived = db.Column(db.Boolean, nullable=True)



class CourseList(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    course_list_id = db.Column(db.Integer, db.ForeignKey(CourseList.id))
    notes_id = db.Column(db.Integer, db.ForeignKey(Notes.id))
    name = db.Column(db.String(100))
    status = db.Column(db.String(10))
    # progress = Column(Integer)



class WorkList(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    company = db.Column(db.String(50))
    cargo = db.Column(db.String(50))

class WorkJournal(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    works_list_id = db.Column(db.Integer, db.ForeignKey(WorkList.id))
    title = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    content = db.Column(db.Text)


