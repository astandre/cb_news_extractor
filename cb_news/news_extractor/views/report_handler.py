from flakon import JsonBlueprint
from cb_news.news_extractor.database import *
from flask import request

report_handler = JsonBlueprint('report_handler', __name__)


@report_handler.route('/report', methods=["POST"])
def report_view():
    """Home view.

    This view will return an empty JSON mapping.
    """
    data = request.get_json()
    new_report = Report()

    if "id" in data:
        new_report.id = data["id"]

    if "description" in data:
        new_report.description = data["description"]

    if "author" in data:
        new_report.author = data["author"]

    if "attachment" in data:
        att_list = []
        for att in data["attachment"]:
            att_list.append(Attachment(url=att["url"]))
        print(att_list)
    report = get_or_create_report(new_report)

    return {"id": report.id}


@report_handler.route('/report/all', methods=["GET"])
def all_reports():
    return {"reports": get_all_saved_reports()}
