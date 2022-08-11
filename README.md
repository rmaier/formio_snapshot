# JSON Snapshot tool

## Concept

* input array / file &rarr; variables, urls, etc...
* functions

  * main: curl &rarr; date_time_proj_form_opt

  * zip / git / NC upload
* manual 'commit' option for certain milestones / versions 

## Input

CSV file with following information: 

```
fname: input.csv with header line

Project Name; Form Name; URL dev
```

example:

```
Project Name; Form Name; URL dev
Umgang mit XXX; Beseitigungspflicht Formular; https://backend-govforms.service.wirtschaft.nrw/dev-xxx
```

questions: 

* do I need any authentication to access the form.io site? 

## Functions

### main

### read_csv

### get_json

### write_json

---

## Snippets

```python
python -i file.py # opens script in the python interpreter

type()
```

datetime: [from](https://www.programiz.com/python-programming/datetime/strftime)

```python
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)
```



