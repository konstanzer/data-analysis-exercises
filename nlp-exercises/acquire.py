import pandas as pd
from bs4 import BeautifulSoup
from requests import get

hdr = {'User-Agent': 'Codeup Data Science'}

def get_codeup_articles():
    """Scrape codeup.com
    Args: List of strings
    Out: List of dictionaries
    """
    dicts = []
    titles = ["codeups-data-science-career-accelerator-is-here",
              "data-science-myths",
              "data-science-vs-data-analytics-whats-the-difference",
              "10-tips-to-crush-it-at-the-sa-tech-job-fair",
              "competitor-bootcamps-are-closing-is-the-model-in-danger"]
    for t in titles:
        response = get("https://codeup.com/data-science/"+t, headers=hdr)
        soup = BeautifulSoup(response.text, "html5lib")
        content = soup.select('div[class*="post_content"]')[0].find_all('p')
        body = ""
        for c in content: body += " "+c.text
        dicts.append({'title': soup.find("h1").text, 'content': body})
    return pd.DataFrame(dicts)

def get_inshorts_articles():
    """Scrape inshorts.com
    Args: List of strings 
    Out: List of dictionaries
    """
    dicts = []
    topics = ["business","sports","technology","entertainment"]
    for t in topics:
        response = get("https://inshorts.com/en/read/"+t, headers=hdr)
        soup = BeautifulSoup(response.text, "html5lib")
        titles = soup.find_all('span', itemprop='headline', text=True)
        contents = soup.find_all('div', itemprop='articleBody', text=True)
        for title, content in zip(titles, contents):
            dicts.append({'title': title.text, 'content': content.text, 'category': t})
    return pd.DataFrame(dicts)

                     
def parse_gulde_article(article):
    title = article.h2.text
    date, author = article.select('.italic')[0].find_all('p')
    return {'title': title, 'date': date.text, 'author': author.text}

def gulde_articles():
    response = requests.get('https://web-scraping-demo.zgulde.net/news')
    soup = BeautifulSoup(response.text, "html5lib")
    articles = soup.select('.grid.gap-y-12 > div')
    print(pd.DataFrame([parse_gulde_article(article) for article in articles]).head())

    
if __name__ == "__main__":
    df = get_codeup_articles()
    print(df.head())
    #df.to_csv("codeuparticles.csv", index=0)
    df = get_inshorts_articles()
    print(df.head())
    #df.to_csv("shortarticles.csv", index=0)
