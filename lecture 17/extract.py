from requests_html import HTMLSession
from rake_nltk import Rake


def extract_text():
    s = HTMLSession()
    url = "https://www.musicradar.com/reviews/tech/akg-c214-172209"
    response = s.get(url)
    return response.html.find('div#article-body', first=True).text


print(extract_text())

#r = Rake()
#r.extract_keywords_from_text(extract_text)
#print(r.get_ranked_phrases_with_scores())