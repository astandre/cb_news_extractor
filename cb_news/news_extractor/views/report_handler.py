from flakon import JsonBlueprint
from cb_news.news_extractor.database import *
from flask import request
import logging

report_handler = JsonBlueprint('report_handler', __name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@report_handler.route('/report', methods=["POST"])
def report_view():
    """Home view.

    This view will return an empty JSON mapping.
    """
    data = request.get_json()
    logger.info("Appending new report  %s", data)
    new_report = Report()

    message = ""

    if "id" in data:
        new_report.id = data["id"]

    if "description" in data:
        new_report.description = data["description"]
        message += "\nDescription updated"

    if "author" in data:
        new_report.author = data["author"]
        message += "\nAuthor updated"

    if "attachment" in data:
        att_list = []
        for att in data["attachment"]:
            att_list.append(Attachment(url=att["url"]))
        print(att_list)
    report = get_or_create_report(new_report)

    return {"id": report.id, "message": message}


@report_handler.route('/report/all', methods=["GET"])
def all_reports():
    return {"reports": get_all_saved_reports()}
