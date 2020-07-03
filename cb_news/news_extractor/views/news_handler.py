from flakon import JsonBlueprint
from cb_news.news_extractor.services import *
from cb_news.news_extractor.database import *
from cb_news.news_extractor.utils import *
import logging

news_handler = JsonBlueprint('news_handler', __name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@news_handler.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping.
    """
    return {}


@news_handler.route('/extract/news', methods=["GET"])
def extract_news():
    noticias = get_posts()
    logger.info("Retrieving posts  %s", len(noticias))
    cont_not = 0
    cont = 0
    # print(noticias)
    if len(noticias) > 0:
        for noticia in noticias:
            # print(noticia)
            new_noticia = get_post(noticia["id"])
            # print(new_noticia)
            logger.info("Appending post  %s", new_noticia)
            if new_noticia["is_published"] and "message" in new_noticia:
                post_type = classify_post(new_noticia["message"])
                noticia_str = clean_input(new_noticia["message"])
                if post_type != 'publicidad':
                    new_notic_obj = Noticia(post_id=new_noticia["id"],
                                            message=noticia_str,
                                            permalink_url=new_noticia["permalink_url"])

                    if post_type == 'historia':
                        new_notic_obj.todays_story = True

                    if "full_picture" in new_noticia:
                        new_notic_obj.full_picture = new_noticia["full_picture"]

                    if "shares" in new_noticia:
                        new_notic_obj.shares = new_noticia["shares"]["count"]

                    if get_or_create_news(new_notic_obj):
                        cont_not += 1
                    else:
                        cont += 1

    message = f"news found: {cont_not} \nnews updated: {cont}"

    return {"message": message}


@news_handler.route('/all/news', methods=["GET"])
def get_all_news():
    return {"news": get_all_saved_news()}


@news_handler.route('/today/news', methods=["GET"])
def get_today_news():
    return {"news": get_today_news_db()}


@news_handler.route('/today/top/news', methods=["GET"])
def get_top_news():
    return {"news": get_top_news_db()}


@news_handler.route('/today/story', methods=["GET"])
def get_today_story_view():
    return {"news": get_todays_story()}

# @news_handler.route('/top/today/news', methods=["GET"])
# def get_top_today_news():
#     return {"news": get_all_saved_news()}
