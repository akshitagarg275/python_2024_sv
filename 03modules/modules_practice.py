import random

# random.seed(3)

# Math.floor(random.random() * ten )
# print(random.random() )

# print(random.randint(3,9))

# print(random.choices(["red","green", "yellow"],[20,40,90]))

import sys
# print(sys.version)

# import datetime
# cur_date = datetime.date.today()
# print(cur_date)


# import json

# data = '{"name": "Alice", "age": 30}'
# parsed_data = json.loads(data)
# print(type(parsed_data))
# print(parsed_data['name']) 


import re
pattern = r'\b\w+\b'  # Match whole words
text = 'Python is awesome'
matches = re.findall(pattern, text)
print(matches)