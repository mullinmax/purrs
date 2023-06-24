import re

class RedditItem(URLItem):
    def get_short_url(self):
        reddit_match = re.search(r'reddit\.com(/r/\w+|/u/\w+)', self.url)
        
        if reddit_match:
            return reddit_match.group(1)
            
        return super().get_short_url()

