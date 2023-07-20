import pandas as pd
import numpy as np
from datetime import datetime
import random

def date_list2():
  start_date = datetime.strptime("2022-02-01", "%Y-%m-%d")
  end_date = datetime.strptime("2022-02-28", "%Y-%m-%d")
  D = "D"
  date_list = pd.date_range(start_date, end_date, freq = D)
  return date_list

def jmena2():
  dluznici = ['Bryan Welker', 'John Sharpe', 'Randy Jebb', 'Elsa Hill', 'John Merrell']
  jmena = []
  for i in range(0,len(date_list2())):
    jmena.append(random.choice(dluznici))
  return jmena

def pujcka2():
  pujcka = []
  for i in range(0,len(date_list2())):
    pujcka.append(random.randint(1000,10000)) 
  return pujcka

def dat_dati2():
  dat_dati = []
  for i in range (0,len(date_list2())):
    dat_dati.append(bool(random.randint(0,1)))  
  return dat_dati

jmena2()
date_list2()
pujcka2()
dat_dati2()


lichva = pd.DataFrame(
    data = {
        "datum": date_list2(),
        "seznam_jmen": jmena2(),
        "pujcka": pujcka2(),
        "splatil": dat_dati2()
        }
)
myhtml = lichva.style.set_properties(**{'font-size': '11pt', 'font-family': 'Calibri','border-collapse': 'collapse','border': '1px solid black'}).render()

with open('myhtml.html','w') as f:
    f.write(myhtml) 
    
lichva.to_html('myhtml.html')
pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
html_string="""
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    {table}
  </body>
</html>.
"""
# OUTPUT AN HTML FILE
with open('myhtml.html', 'w') as f:
    f.write(html_string.format(table=lichva.to_html(classes='mystyle')))

