import re
<<<<<<< HEAD
from english_stopwords import STOPWORDS
=======
from english_stopwords import regexps_to_change
>>>>>>> improve

with open('./hamlet.txt') as f:
    hamlet = f.read()

<<<<<<< HEAD
for stopword in STOPWORDS:
    hamlet = re.sub(
        r'[\s\W]+(' + stopword + r')[\s\W]+', ' DELETED ', hamlet, flags=re.IGNORECASE
=======
for (regexp, to_change) in regexps_to_change:
    print(regexp)
    hamlet = re.sub(
        regexp, to_change, hamlet, flags=re.IGNORECASE
>>>>>>> improve
    )

with open('./hamlet_no_stopwords.txt', 'w') as f:
    f.write(hamlet.strip())
