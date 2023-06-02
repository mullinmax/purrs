from feedgenerator import Atom1Feed

def write_feed(entries, filename):
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

    with open(filename, 'w') as f:
        feed.write(f, 'utf-8')
