import re

def preprocess_message(message):
    message = re.sub('[\:\_=\#\@\$\%\$\\(\)\~\@\;\'\|\<\>\]\[\"\–“”…*]', ' ', message)
    message = message.lower()
    message = message.replace(',', ' , ')
    message = message.replace('.', ' . ')
    message = message.replace('!', ' ! ')
    message = message.replace('&', ' & ')
    message = message.replace('?', ' ? ')
    message = message.replace('(', ' ( ')
    message = message.replace(')', ' ) ')
    message = message.replace('+', ' + ')
    return message