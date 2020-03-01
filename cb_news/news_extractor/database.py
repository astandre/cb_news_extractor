from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()


class Noticia(db.Model):
    """Agent
    """
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(80), nullable=False)
    permalink_url = db.Column(db.String(80), unique=True, nullable=False)
    full_picture = db.Column(db.String(80), unique=True, nullable=True)
    shares = db.Column(db.String(80), nullable=True)
    extracted_time = db.Column(db.DateTime, default=datetime.now())
    # This fields need approval
    reactions = db.Column(db.String(80), nullable=True)
    likes = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f"<Noticia {self.post_id}>"


def get_or_create_news(new_noticia):
    noticia_exists = Noticia.query.filter_by(post_id=new_noticia.post_id).first()
    if noticia_exists is None:
        db.session.add(new_noticia)
        db.session.commit()
        return True
    else:
        return False


def get_all_saved_news():
    noticias = Noticia.query.all()
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
        Noticia.extracted_time).limit(5).all()
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
