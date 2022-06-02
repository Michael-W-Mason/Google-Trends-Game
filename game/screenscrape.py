from requests_html import HTMLSession

def trend_now_by_country(country_code='US'):
    url = f'https://trends.google.com/trends/trendingsearches/daily?geo={country_code}'
    asession = HTMLSession()
    resp = asession.get(url)
    resp.html.render()

    css_selector = "div.details > div.details-top > div.title > span > a"
    all_elements = resp.html.find(css_selector)
    result = []
    for element in all_elements:
        result.append(element.text)
    return result

if __name__ == "__main__":
    trend_now_by_country()