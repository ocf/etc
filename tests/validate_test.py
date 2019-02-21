import json
import os

import jsonschema
import pytest
import yaml

# Disable pyfakefs
@pytest.fixture
def etc():
    pass


def test_validate():
    configs = yaml.safe_load(open('configs/validate.yaml')).items()

    for shortname, metadata in configs:
        schema_filename = os.path.join('schemas', metadata['schema'])
        config_filename = os.path.join('configs', shortname + '.yaml')

        # PyYAML reads YAML date objects as Python date objects, which confuses
        # jsonschema. To get around this, we convert the object to and from
        # JSON, using the str function to convert the date objects to strings.
        config = json.loads(
            json.dumps(yaml.safe_load(open(config_filename)), default=str),
        )

        schema = json.load(open(schema_filename))

        jsonschema.validate(config, schema)
