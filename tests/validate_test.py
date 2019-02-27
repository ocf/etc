import json
import os

import jsonschema
import yaml
from pyfakefs.fake_filesystem_unittest import Pause


def test_validate(fs):
    configs = yaml.safe_load(open('/etc/ocf/validate.yaml')).items()

    for shortname, metadata in configs:
        schema_filename = os.path.join('schemas', metadata['schema'])
        config_filename = os.path.join('/etc/ocf', shortname + '.yaml')

        # PyYAML reads YAML date objects as Python date objects, which confuses
        # jsonschema. To get around this, we convert the object to and from
        # JSON, using the str function to convert the date objects to strings.
        config = json.loads(
            json.dumps(yaml.safe_load(open(config_filename)), default=str),
        )

        with Pause(fs):
            schema = json.load(open(schema_filename))

        jsonschema.validate(config, schema)
