# AWS-Lambda-Python-Example

AWS Lambda for Python Examples

## Setup

```bash
$ pyenv install 2.7.10

or 

$ cd ~/.pyenv
$ git pull origin master
$ pyenv install 2.7.9
```

```
$ pyenv virtualenv 2.7.9 aws-lambda-example
$ pyenv local aws-lambda-example
```

## Development
```bash
$ mkdir -p ~/path/to/repo/AWS-Lambda-Python-Example
$ cd ~/path/to/repo/AWS-Lambda-Python-Example
$ pip install beautifulsoup4 -t . 
$ vi main.py
```

```python
import urllib2
from bs4 import BeautifulSoup

print("load function")

SCRAPING_URL = "https://news.google.com/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"


def lambda_handler(event, context):
    request = urllib2.Request(SCRAPING_URL)
    request.add_header('User-agent', USER_AGENT)

    html = urllib2.urlopen(request).read()
    bs = BeautifulSoup(html)

    print("finish function")
    return [x.text for x in bs.find_all(class_="titletext")]
```

## Upload 
```bash
$ pwd
$ /Users/teitei/path/to/repo/AWS-Lambda-Python-Example
$ zip -r AWS-Lambda-Python.zip *
$ aws lambda create-function --region us-west-2 --function-name main --zip-file fileb://AWS-Lambda-Python-Example.zip --role arn:aws:iam::0000000:role/lambda_basic_execution --handler main.lambda_handler --runtime python2.7 --timeout 15 --memory-size 12
```
