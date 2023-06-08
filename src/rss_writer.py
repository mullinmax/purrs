"""
This module provides functionality to write RSS feed using the Atom1Feed class from feedgenerator.
"""

from feedgenerator import Atom1Feed  

def write_feed(entries, filename):  
    """
    Writes RSS feed to a file.

    Args:
        entries: A list of RSS entries.
        filename: The name of the file to write the feed.
    """
    feed = Atom1Feed(  
        title="My Feed",  
        link="http://example.com/feed/",  
        description="A feed of various RSS entries, sorted and categorized",  
    )  

    for entry in entries:  
        feed.add_item(  
            title=entry.title,  
            link=entry.link,  
            description=entry.description,  
        )  

    with open(filename, 'w', encoding='utf-8') as file:  
        feed.write(file, 'utf-8')
