# ocf-etc

This repo contains configuration files which are replicated to and
automatically updated on every OCF host at `/etc/ocf/`. Configuration files are
written in YAML and have schemas defined in the `schemas` folder.

To validate the files, simply run:

```
make
```

# Adding a new configuration file

To add a new configuration file:

1. Create the data file (`yourconfig.yaml`).
2. Create the schema file (`schemas/yourconfig.schema.json`).
3. Add your file to `validate.yaml`, and associate it with its schema.
4. Commit changes to this repo
5. Add ocflib functions to read your config file
6. Add tests in this repo that ensure the ocflib functions won't throw
   exceptions.
