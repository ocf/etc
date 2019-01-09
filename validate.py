import json
import os

import jsonschema
import yaml


def validate(data_filename, schema_filename):
    # Convert to and from JSON so we can turn date objects into strings
    data = json.loads(json.dumps(yaml.load(open(data_filename)), default=str))

    schema = json.load(open(schema_filename))

    return jsonschema.validate(data, schema)


def main():
    for shortname, metadata in yaml.load(open('validate.yaml')).items():
        print(shortname + ' ... ', end='', flush=True)

        schema_filename = os.path.join(
            'schemas', shortname + '.schema.json'
        )

        data_filename = shortname + '.yaml'
        try:
            validate(data_filename, schema_filename)
            print('OK')
        except:  # noqa: E722
            print('FAIL')
            raise


if __name__ == '__main__':
    main()
