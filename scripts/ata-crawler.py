import requests
from bs4 import BeautifulSoup
import html2text


def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.text


def extract_article(html):
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")  # 可根据目标站点改为 div.class 等
    return str(article) if article else ""


def html_to_markdown(html_content):
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # 可选：保留链接
    return converter.handle(html_content)


def save_as_mdx(md_content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)


if __name__ == "__main__":
    url = "https://example.com/your-blog-post"
    html = fetch_html(url)
    article_html = extract_article(html)
    markdown = html_to_markdown(article_html)
    save_as_mdx(markdown, "post.mdx")
