# jinja2-templatize
This is a simple application that accepts input of a variables file, a template parameterized with Jinja2, and outputs the result. 


## Usage

```
usage: main.py [-h] [-v VALUES] [-t TEMPLATEFILE]

Uses Jinja2 to replace template values.

optional arguments:
  -h, --help            show this help message and exit
  -v VALUES, --values VALUES
                        Relative path to the manifest file including the filename.
  -t TEMPLATEFILE, --templatefile TEMPLATEFILE
                        Relative path where the template file resides.
```

## Examples


### YAML

```
$ python3 jinja2_templatize/main.py -v example/Values.yaml -t ./example/yaml-template-example.yaml 
TemplateName: "ExampleOne"
Description: "This is example one that uses yaml."
Parameters:
  Environment: "dev"
  Owner: "John Doe"
  Application: "ExampleOne"
```

### JSON

```
$ python3 jinja2_templatize/main.py -v example/Values.yaml -t ./example/json-template-example.json 
{
    "TemplateName": "ExampleTwo",
    "Description": " This is example one that uses json.",
    "Parameters": {
        "Environment": "dev",
        "Owner": "Jane Doe",
        "Application": "ExampleTwo"
    }
}
```