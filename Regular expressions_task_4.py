import re
#Очистите следующий твит, чтобы он содержал только одно сообщение
#пользователя. То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to
code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub('http\S+\s*', '', tweet) # удалит URL
tweet = re.sub('RT|cc', '', tweet) # удалит RT и cc
tweet = re.sub('#\S+', '', tweet) # удалит хештеги
tweet = re.sub('@\S+', '', tweet) # удалит упоминани
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet) # удалит символы пунктуации
tweet = re.sub('\s+', ' ', tweet) # заменит пробельные символы на 1 пробел
print(tweet)