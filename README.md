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
fname: input.csv

Project Name; Form Name; URL dev
```

example:

```
Project Name; Form Name; URL dev
Umgang mit Tiernebenprodukten; Beseitigungspflicht Ausnahmegenehmigung; https://backend-govforms.service.wirtschaft.nrw/dev-qxixbggyuynfgel/umgangmittiernebenproduktenbeseitigungspflichtausnahmegenehmigung

... tbc
```

questions: 

* do I need any authentication to access the form.io site? 

## Functions

### main

### read

[easy http read](https://requests.readthedocs.io/en/latest/):

```python
import requests

r = requests.get('https://backend-govforms.service.wirtschaft.nrw/dev-qxixbggyuynfgel/umgangmittiernebenproduktenbeseitigungspflichtausnahmegenehmigung') #, auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
# --> " " gets ' ' , see 
```

### write

```python
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

```



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

```python
# call
a = 2
b = 3
testfun_res = tesfun(a, b)

def testfun(a,b): 
    c=a*b
    return c
```

