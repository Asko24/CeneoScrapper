#import bibliotek
import requests
from bs4 import BeautifulSoup


#adres URL strony z opiniami
url = "https://www.ceneo.pl/76891701#tab=reviews"


#pobranie kodu HTML strony z adresu URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')


#wybranie z kodu strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")

#ekstrakcja składowych dla pierwszej opinii z listy
opinion = opinions[0]
opinion_id = opinion["data-entry-id"]
print(opinion_id)
author = opinion("div.reviewer-name-line").pop().string
recommendation = opinion.select('div.product-reviewer-summary > em').pop().string
stars = opinion.select('span.review-score-count').pop().string
#confirmed = opinion.select('div.product-review-pz').pop().string
#wystawienie = opinion.select('span.review-time > time[datetime] - pierwsze wystapienie').pop().string
#purchased = opinion.select('span.review-time > time[datetime] - drugie wystapienie').pop().string
useful = opinion.select('button.votes-yes').pop()["data.total-vote"]s
useless = opinion.select('button.votes-no').pop()["data.total-vote"]
content = opinion.select('p.product-review-body').pop().get_text
#wady = opinion.select('div.cons-cell > ul')
#zalety = opinion.select('div.pros-cell > ul')
print(useless)


#ekstrakcja składowych dla pierwszej opinii z listy

