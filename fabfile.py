import json
import logging
import sys

from fabric.api import local
from fabric.api import task
from elasticsearch import Elasticsearch
from elasticsearch import helpers

@task
def download_musea_galleries():
    local('wget http://open.datapunt.amsterdam.nl/MuseaGalleries.json --output-document MuseaGalleries.json')

@task
def import_es_musea_galleries():
    logging.basicConfig(level=logging.INFO)
    index = "musea_galeries"
    dataset = "MuseaGalleries.json"

    es = Elasticsearch()
    if not es.ping():
        logging.error("fails to connect on elasticsearch (localhost:9200). elasticsearch is probably not running")
        sys.exit(1)

    musea_galeries_json = ""
    with open(dataset, 'r') as fp:
        musea_galeries_json = fp.read()

    musea_galeries_list = json.loads(musea_galeries_json)

    if es.indices.exists(index=index):
        es.indices.delete(index=index)

    actions = []
    bulk_size = 100
    for j in range(0, len(musea_galeries_list), 1):
        action = {
            "_index": index,
            "_type": "musea",
            "_source": musea_galeries_list[j]
        }

        actions.append(action)

        if len(actions) == bulk_size:
            helpers.bulk(es, actions)
            actions = []

    helpers.bulk(es, actions)
    logging.info("{0} museas & galleries has been imported in index {1}".format(len(musea_galeries_list), index))
