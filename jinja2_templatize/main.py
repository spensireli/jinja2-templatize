
"""
Jinja2-templatize is a simple script that uses jinja2
to substitute the values for either yaml or json from
an inputs values file in yaml format.
"""
import argparse
import yaml
from jinja2 import Template

parser = argparse.ArgumentParser(description='Uses Jinja2 to replace template values.')
parser.add_argument('-v', '--values', type=str, help='Relative path to the manifest file including the filename.')
parser.add_argument('-t', '--templatefile', type=str, help='Relative path where the template file resides.')
args = parser.parse_args()
manifestfile = args.values
templatepath = args.templatefile

if __name__ == "__main__":
    config_data = yaml.load(open(manifestfile), Loader=yaml.BaseLoader)
    with open(templatepath) as file_:
        template = Template(file_.read())
    print(template.render(config_data))
