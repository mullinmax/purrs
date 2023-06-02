from setuptools import setup, find_packages

setup(
    name="purrs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "feedparser",
        "feedgenerator",
    ],
    entry_points={
        'console_scripts': [
            'purrs=purrs.reddit_rss:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to fetch RSS feeds and rebroadcast them",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
