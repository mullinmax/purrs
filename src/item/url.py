from previewlink import preview_link
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests

class URLItem:
    def __init__(self, url):
        self.url = url
        self.html = self._get_html()
        self.short_url = self._get_short_url()
        self.metadata = self._get_preview_metadata()
        self.title = self._get_title()
        self.description = self._get_description()
        self.image = self._get_image()

    def _get_short_url(self):
        return urlparse(self.url).netloc

    def _get_html(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text

    def _get_preview_metadata(self):
        return preview_link(self.url)

    def _get_title(self):
        return self.metadata.get('title')

    def _get_description(self):
        return self.metadata.get('description')

    def _get_image(self):
        # Get image from metadata
        if self.metadata.get('image'):
            return self._resolve_url(self.metadata.get('image'))

        # If not available, fetch from HTML
        soup = BeautifulSoup(self.html, 'html.parser')

        # Try to find favicon
        icon_link = soup.find("link", rel="icon")
        if icon_link:
            return self._resolve_url(icon_link['href'])

        # As a last resort, use any image available in the HTML
        img_tag = soup.find("img")
        if img_tag:
            return self._resolve_url(img_tag['src'])

        return None

    def _resolve_url(self, url):
        return urljoin(self.url, url)

    def __repr__(self):
        return f'URLItem("{self.url}")'

    def __str__(self):
        return f'URL: {self.url}\nShort URL: {self.short_url}\nTitle: {self.title}\nDescription: {self.description}\nImage: {self.image}'