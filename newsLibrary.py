import requests

def get_news_titles():
    api_key = None
    r = requests.get(
        f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey={api_key}",
        timeout=5
    )

    if r.status_code != 200:
        return []

    data = r.json()
    articles = data.get("articles", [])

    titles = []
    for article in articles[:5]:
        title = article.get("title")
        if title:
            titles.append(title)

    return titles