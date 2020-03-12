from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()


class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(400), nullable=False)
    permalink_url = db.Column(db.Text, unique=True, nullable=False)
    full_picture = db.Column(db.Text, unique=True, nullable=True)
    shares = db.Column(db.Integer, nullable=True, default=0)
    extracted_time = db.Column(db.DateTime, default=datetime.now())
    todays_story = db.Column(db.Boolean, default=False)
    # This fields need approval
    reactions = db.Column(db.String(80), nullable=True)
    likes = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f"<Noticia {self.post_id}>"


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), default="Anonimo")
    resolved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Report {self.description[0:100]}>"


class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'),
                          nullable=False)
    report = db.relationship('Report', backref=db.backref('attachments', lazy=True))

    def __repr__(self):
        return f"<Attachment {self.id}>"


def get_or_create_news(new_noticia):
    noticia_exists = Noticia.query.filter_by(post_id=new_noticia.post_id).first()
    if noticia_exists is None:
        db.session.add(new_noticia)
        db.session.commit()
        return True
    else:
        noticia_exists.message = new_noticia.message
        noticia_exists.shares = new_noticia.shares
        noticia_exists.full_picture = new_noticia.full_picture
        db.session.commit()
        return False


def get_or_create_report(new_report):
    report_exists = Report.query.filter_by(id=new_report.id).first()
    if report_exists is None:
        db.session.add(new_report)
        db.session.commit()
        return new_report
    else:
        report_exists.author = new_report.author
        db.session.commit()
        return report_exists


def get_all_saved_reports():
    reports = Report.query.filter_by(resolved=False).all()
    result = []
    for report in reports:
        # print(noticia)
        json_report = {
            "description": report.description,
            "author": report.author,
            "id": report.id,
        }

        print(report.attachments)
        result.append(json_report)
    return result


def get_all_saved_news():
    noticias = Noticia.query.filter_by(todays_story=False).all()
    result = []
    for noticia in noticias:
        # print(noticia)
        result.append({
            "post_id": noticia.post_id,
            "message": noticia.message,
            "permalink_url": noticia.permalink_url,
            "full_picture": noticia.full_picture,
            "shares": noticia.shares,
            "extracted_time": noticia.extracted_time
        })
    return result


def get_today_news_db():
    # todays_datetime = datetime(datetime.today().year, datetime.today().month, datetime.today().day - 1)
    todays_datetime = datetime.today() - timedelta(days=1)
    # print(todays_datetime)
    noticias = Noticia.query.filter(Noticia.extracted_time > todays_datetime).order_by(
        Noticia.extracted_time).filter_by(todays_story=False).limit(5).all()
    result = []
    for noticia in noticias:
        result.append({
            "post_id": noticia.post_id,
            "message": noticia.message,
            "permalink_url": noticia.permalink_url,
            "full_picture": noticia.full_picture,
            "shares": noticia.shares,
            "extracted_time": noticia.extracted_time
        })
    return result


def get_todays_story():
    todays_datetime = datetime.today() - timedelta(days=1)
    t_story = Noticia.query.filter(Noticia.extracted_time > todays_datetime).order_by(
        Noticia.extracted_time).filter_by(todays_story=False).first()
    return {
            "post_id": t_story.post_id,
            "message": t_story.message,
            "permalink_url": t_story.permalink_url,
            "full_picture": t_story.full_picture,
            "shares": t_story.shares,
            "extracted_time": t_story.extracted_time
        }
