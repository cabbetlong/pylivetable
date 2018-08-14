
### API

```python
pylivetable.douyu.room(id='123456')
pylivetable.room(site='douyu', id='123456')

pylivetable.douyu.category(name='lol', rank=10)
pylivetable.category(site='douyu', name='lol', rank=10)```


```python
import requests as rq
import pandas as np
from bs4 import BeautifulSoup
```


```python
# douyu categories
rq.get('https://www.douyu.com/directory')
```




    <Response [200]>




```python
# douyu rooms of a specific category
rq.get('https://www.douyu.com/gapi/rkc/directory/0_0/1')
```




    <Response [200]>




```python
# huya categories
rq.get('https://www.huya.com/g')
```




    <Response [200]>


