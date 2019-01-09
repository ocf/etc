# ocf-etc

This repo contains configuration files which are replicated to and
automatically updated on every OCF host at `/etc/ocf/`. Configuration files are
written in YAML and have schemas defined in the `schemas` folder.

To validate the files, simply run:

```
make
```

Additionally, you can lint the Python `validate.py` by running `make lint`.

# Adding a new configuration file

To add a new configuration file:

* Create the data file (`yourconfig.yaml`).
* Create the schema file (`schemas/yourconfig.schema.json`).
* Add your file to `validate.yaml`, and associate it with its schema.
