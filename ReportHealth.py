import requests
from datetime import datetime
from configparser import ConfigParser

today = datetime.now().strftime("%Y/%m/%d")
# today = datetime(year=2022,month=4,day=2).strftime("%Y/%m/%d")
config = ConfigParser(interpolation=None)
config.read('config.ini',encoding='utf-8')
mail = config['mail']['mail']
site = config['site']['site']
name = config['empname']['name']
empid = config['empid']['empid']
way = config['way']['way']

url_POST_login='https://familyweb.wistron.com/whrs/login_act.aspx'
url_POST_data='https://familyweb.wistron.com/whrs/temperature_addnew_act.aspx'
ID={'userpass':'10709055'}
#https://familyweb.wistron.com/whrs/temperature_addnew_act.aspx
data={
'bformdata':'1',
'email': mail,
'site': site,
'empname': name,
'survey': '0',
'empid': empid,
'eventid': '1',
'measure_date': today,
'symptom': '1',
'vaccine_date': '',
'vaccine_brand': '0',
'commute_way': '1',
'tour': '1',
'spot': '0',
'homedate': '',
'trip': '1',
'area': '0',
'backdate': '',
'travel': '1',
'country': '3',
'countryname':'' ,
'region': '',
'finishdate': '',
'notice': '1',
'notice_home': '1',
'family': '2',
'relation1': '',
'country1': '',
'city1': '',
'backdate1': '2020/1/1',
'backdate2': '2020/1/1',
'backdate3': '2020/1/1',
'bevent': '0'
}

session = requests.Session()

login=session.post(url_POST_login,data=ID)


if login.url == 'https://familyweb.wistron.com/whrs/temperature_formdata.aspx' :
    session.post(url_POST_data,data=data)


