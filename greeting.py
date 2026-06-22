
from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'

    final_massage = message + ', ' + name + '-san!'
    print(final_message)



greet('Inoue')
