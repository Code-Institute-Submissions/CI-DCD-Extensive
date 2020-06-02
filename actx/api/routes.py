from flask import jsonify, Blueprint, request
from actx.models.entities import Band, Towns

api = Blueprint('api', __name__)

@api.route("/genres")
def list_genres():
    aggregation = list(Band.objects.aggregate([
        {"$unwind": "$genres"},
        {"$group": { "_id": "$genres"} }
    ]))
    genres = []
    for genre in aggregation:
        for k,v in genre.items():
            genres.append(v)
    return ",".join(genres)


@api.route('/town/<county>')
def get_towns(county):
    # [(otown.town, otown.town) for otown in Towns.objects(county="Antrim")]
    towns = Towns.objects(county=county)

    townsArray = []

    for town in towns:
        townObj = {}
        townObj["val"] = town.town
        townObj["name"] = town.town
        townsArray.append(townObj)

    return jsonify({"towns": townsArray})