## Motivation

Elasticsearch works on json datasets. I want a dataset that represents a document based on several
attributes.

That's why I have import the list of Amsterdam museum & galleries released in OpenData by .
http://open.datapunt.amsterdam.nl/MuseaGalleries.json

I think those data are released in the public domain or through a common creative licenses

## Synopsis

Import a public dataset from Amsterdam into elasticsearch accessible through localhost:9200.
You can use the VM configured in [vagrant-elasticsearch](https://github.com/Esme-Sudria-Database/vagrant-elasticsearch)

## The latest version

You can find the latest version to ...

    git clone https://github.com/Esme-Sudria-Database/dojo_elasticsearch.git

## Usage

You can import the dataset in elasticsearch in the index ``musea_galeries``.

```bash
$ source venv/bin/activate
(venv) $ fab import_es_musea_galleries
```
If the dataset is out of date, you can redownload it :

```bash
$ source venv/bin/activate
(venv) $ fab download_musea_galleries
```

## Installation

To set up the python environments (venv, pip dependency, ...) :

```bash
bash setup.sh
```

## Tests
## Contributors

* Fabien Arcellier

## License
