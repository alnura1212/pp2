import datetime
from datetime import timedelta
x = datetime.datetime.today() - timedelta(days=1)
y = datetime.datetime.today()
z = datetime.datetime.today() + timedelta(days=1)
print(x)
print(y)
print(z)

