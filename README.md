# Secret Santa game

![](https://img.shields.io/badge/python-v3.7.3-brightgreen.svg)

Secret Santa game programmed for fun!
Just list your friend names and emails and let the script do the toss for you.

***

## REQUIREMENTS

- Python3
- `pip3 install -r requirements.txt`
- A Google account
- Go to https://myaccount.google.com/lesssecureapps and enable the **Less secure option**. Disable the option when finished.
- Needs a list of names & emails NAME_LIST.csv using a `','` as delimiter as follows:

~~~csv
NAME,EMAIL
John,john@doe.com
Alice,alice@mail.com
~~~

***

## USAGE

The program will ask for a gmail username and password. Provide the username without the `@gmail.com`. The password won't be shown.

~~~bash
python3 secret_santa.py -f NAME_LIST.csv

Username: myusername
Pass: XXXX
~~~
