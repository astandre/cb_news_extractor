from flakon import JsonBlueprint
from cb_news.news_extractor.services import *
from cb_news.news_extractor.database import *

news_handler = JsonBlueprint('news_handler', __name__)


@news_handler.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping.
    """
    return {}


@news_handler.route('/extract/news', methods=["GET"])
def extract_news():
    noticias = get_posts()
    cont_not = 0
    print(noticias)
    if len(noticias) > 0:
        for noticia in noticias:
            # print(noticia)
            new_noticia = get_post(noticia["id"])
            print(new_noticia)
            if new_noticia["is_published"]:
                if "message" in new_noticia:
                    new_notic_obj = Noticia(post_id=new_noticia["id"],
                                            message=new_noticia["message"],
                                            permalink_url=new_noticia["permalink_url"],
                                            )

                    if "full_picture" in new_noticia:
                        new_notic_obj.full_picture = new_noticia["full_picture"]

                    if "shares" in new_noticia:
                        new_notic_obj.shares = new_noticia["shares"]["count"]

                    if get_or_create_news(new_notic_obj):
                        cont_not += 1

    message = f"news found: {cont_not}"

    return {"message": message}


@news_handler.route('/all/news', methods=["GET"])
def get_all_news():
    return {"news": get_all_saved_news()}


@news_handler.route('/today/news', methods=["GET"])
def get_today_news():
    return {"news": get_today_news_db()}

# @news_handler.route('/top/today/news', methods=["GET"])
# def get_top_today_news():
#     return {"news": get_all_saved_news()}
