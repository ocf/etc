import json
import os

import jsonschema
import yaml


def validate(data_filename, schema_filename):
    # PyYAML reads YAML date objects as Python date objects, which confuses
    # jsonschema. To get around this, we convert the object to and from JSON,
    # using the str function to convert the date objects to strings.
    data = json.loads(
        json.dumps(yaml.safe_load(open(data_filename)), default=str),
    )

    schema = json.load(open(schema_filename))

    return jsonschema.validate(data, schema)


def main():
    configs = yaml.safe_load(open('configs/validate.yaml')).items()
    for shortname, metadata in configs:
        print(shortname + ' ... ', end='')

        schema_filename = os.path.join('schemas', metadata['schema'])

        data_filename = os.path.join('configs', shortname + '.yaml')
        try:
            validate(data_filename, schema_filename)
            print('OK')
        except Exception:
            print('FAIL')
            raise


if __name__ == '__main__':
    main()
