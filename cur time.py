import pytz
from datetime import datetime
a=pytz.timezone('Asia/Seoul')
b=datetime.now(a)
print (b)