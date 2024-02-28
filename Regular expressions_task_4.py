import re
#Очистите следующий твит, чтобы он содержал только одно сообщение
#пользователя. То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to
code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub('http\S+\s*', '', tweet)
tweet = re.sub('RT|cc', '', tweet)
tweet = re.sub('#\S+', '', tweet)
tweet = re.sub('@\S+', '', tweet)
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
tweet = re.sub('\s+', ' ', tweet)
print(tweet)