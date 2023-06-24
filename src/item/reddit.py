import re
from src.item.generic import GenericItem

class RedditItem(GenericItem):
    def get_short_url(self):
        reddit_match = re.search(r'reddit\.com(/r/\w+|/u/\w+)', self.url)
        
        if reddit_match:
            return reddit_match.group(1)
            
        return super().get_short_url()

