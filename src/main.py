import sys
from crawler import Crawler

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = "https://fintel.io/zh-hant/s/br/nvdc34"
    crawler = Crawler()
    article = crawler.crawl(url)
    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(article.to_markdown())