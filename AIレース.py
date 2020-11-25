#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ターミナルで次を実行する必要がある→「pip install japanize-matplotlib」
#!pip install japanize-matplotlib
import japanize_matplotlib


# In[2]:


texts = []


# In[5]:


import requests


# In[4]:


import requests

response = requests.post('https://brdbc.team-nave.com/system/db', 
                         
                         data={'prccd':'select', 'tncid':'poppopoh777@yahoo.co.jp', 'tncpw':'nissy315',
                               'cmd1':'SELECT * FROM OPMST WHERE SOPDT LIKE \'2020%\';'})


# In[6]:


response = requests.post('https://brdbc.team-nave.com/system/db', 
                         data={'prccd':'getcsv', 'tncid':'poppopoh777@yahoo.co.jp', 'tncpw':'nissy315',
                               'qid':qid})
response.encoding = 'shift-jis'
# print(response.status_code)    # HTTPのステータスコード取得
# print(response.text)    # レスポンスのHTMLを文字列で取得

 

text = response.text.split('\r\n')
def split(txt):
    txt = txt.replace('\"', '')
    return txt.split(',')
array = list(map(split, text))
array.pop(-1)
racemst_mst = pd.DataFrame(array[1:], columns=array[0])
racemst_mst


# In[ ]:


print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得

