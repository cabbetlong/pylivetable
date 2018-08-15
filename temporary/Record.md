
### API

```python
pylivetable.douyu.room(id='123456')
pylivetable.room(site='douyu', id='123456')

pylivetable.douyu.category(name='lol', rank=10)
pylivetable.category(site='douyu', name='lol', rank=10)```


```python
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
```


```python
# douyu categories
cate_html = rq.get('https://www.douyu.com/directory').text
soup1 = BeautifulSoup(cate_html, 'lxml')

cate_names = []
cate_datark = []
cate_href = []

for a in soup.select('.unit a'):
    cate_names.append(a.p.get_text())
    cate_datark.append(a['data-tid'])
    cate_href.append(a['href'])
```


```python
categories = pd.DataFrame(data={'Name': cate_names, 'data_rk': cate_datark, 'href': cate_href})
categories.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>data_rk</th>
      <th>href</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>刺激战场</td>
      <td>350</td>
      <td>/g_jdqscjzc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>绝地求生</td>
      <td>270</td>
      <td>/g_jdqs</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王者荣耀</td>
      <td>181</td>
      <td>/g_wzry</td>
    </tr>
    <tr>
      <th>3</th>
      <td>英雄联盟</td>
      <td>1</td>
      <td>/g_LOL</td>
    </tr>
    <tr>
      <th>4</th>
      <td>主机游戏</td>
      <td>19</td>
      <td>/g_TVgame</td>
    </tr>
  </tbody>
</table>
</div>




```python
# douyu rooms of a specific category
rq.get('https://www.douyu.com/gapi/rkc/directory/0_0/1')
```




```python
# huya categories
rq.get('https://www.huya.com/g')
```




```python
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
```


```python
res = rq.get('https://www.huya.com/g')
```


```python
soup = BeautifulSoup(res.text, 'lxml')

cate_names = []
cate_datark = []
cate_href = []

for li in soup.select('.game-list-item'):
    cate_names.append(li.a.h3.get_text())
    cate_datark.append(li['gid'])
    cate_href.append(li.a['href'])
```


```python
categories = pd.DataFrame(data={'Name': cate_names, 'data_rk': cate_datark, 'href': cate_href})
categories.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>data_rk</th>
      <th>href</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>英雄联盟</td>
      <td>1</td>
      <td>https://www.huya.com/g/lol</td>
    </tr>
    <tr>
      <th>1</th>
      <td>绝地求生</td>
      <td>2793</td>
      <td>https://www.huya.com/g/2793</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王者荣耀</td>
      <td>2336</td>
      <td>https://www.huya.com/g/wzry</td>
    </tr>
    <tr>
      <th>3</th>
      <td>刺激战场</td>
      <td>3203</td>
      <td>https://www.huya.com/g/3203</td>
    </tr>
    <tr>
      <th>4</th>
      <td>星秀</td>
      <td>1663</td>
      <td>https://www.huya.com/g/xingxiu</td>
    </tr>
  </tbody>
</table>
</div>