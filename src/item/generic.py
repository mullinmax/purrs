from previewlink import preview_link
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests
from src.database.item import ItemModel

class GenericItem:
    def __init__(self, url, published_date=None, author=None, title=None, description=None, image=None):
        self.url = url
        self._html = None
        self.short_url = self._get_short_url()
        self.metadata = self._get_preview_metadata()
        self.title = title or self._get_title()
        self.description = description or self._get_description()
        self.image = image or self._get_image()
        self.published_date = published_date
        self.author = author

    def _get_short_url(self):
        return urlparse(self.url).netloc

    @property
    def html(self):
        if self._html is None:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            self._html = response.text
        return self._html

    def _get_preview_metadata(self):
        return preview_link(self.url)

    def _get_title(self):
        return self.metadata.get('title')

    def _get_description(self):
        return self.metadata.get('description')

    def _get_image(self):
        if self.metadata.get('image'):
            return self._resolve_url(self.metadata.get('image'))

        soup = BeautifulSoup(self.html, 'html.parser')
        icon_link = soup.find("link", rel="icon")
        if icon_link:
            return self._resolve_url(icon_link['href'])

        img_tag = soup.find("img")
        if img_tag:
            return self._resolve_url(img_tag['src'])

        return None

    def _resolve_url(self, url):
        return urljoin(self.url, url)

    def __repr__(self):
        return f'GenericItem("{self.url}")'

    def __str__(self):
        return f'URL: {self.url}\nShort URL: {self.short_url}\nTitle: {self.title}\nDescription: {self.description}\nImage: {self.image}\nPublished Date: {self.published_date}\nAuthor: {self.author}'

    def save_to_db(self, sqlalchemy_session):
        item_model = ItemModel(
            url=self.url,
            short_url=self.short_url,
            title=self.title,
            description=self.description,
            image=self.image,
            published_date=self.published_date,
            author=self.author
        )
        sqlalchemy_session.add(item_model)
        sqlalchemy_session.commit()

    @classmethod
    def load_from_db(cls, sqlalchemy_session, id):
        item_model = sqlalchemy_session.query(ItemModel).get(id)
        if item_model:
            return cls(
                url=item_model.url,
                short_url=item_model.short_url,
                title=item_model.title,
                description=item_model.description,
                image=item_model.image,
                published_date=item_model.published_date,
                author=item_model.author
            )