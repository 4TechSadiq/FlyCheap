from datetime import datetime, timedelta

date = datetime.now().date()
months_after = date + timedelta(days=30*6)
print(months_after)
