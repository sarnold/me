AUTHOR = 'Steve Arnold'
SITENAME = 'me'
SITESUBTITLE = 'On being a developer'
SITEURL = ""

PATH = "content"

TIMEZONE = 'PST8PDT'

SHOW_ARTICLE_AUTHOR = (True)
SHOW_ARTICLE_CATEGORY = (True)

DEFAULT_LANG = 'en'

WEBASSETS = (True)
TYPOGRIFY = (True)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ('Ubuntu PPA', 'https://launchpad.net/~nerdboy/+archive/ubuntu/embedded'),
    ('Gentoo Linux', 'http://www.gentoo.org'),
    ('Yocto Project', 'https://www.yoctoproject.org/'),
    ('OpenSCAP', 'https://www.open-scap.org/'),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ('reStructuredText', 'http://docutils.sourceforge.net/rst.html'),
]

# Social widget
SOCIAL = [
    ('github: Steve', 'https://github.com/sarnold'),
    ('github: Work', 'https://github.com/vctlabs'),
]

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/tuxlite_tbs'

CUSTOM_CSS = 'css/custom.css'
STATIC_PATHS = ['extra', 'images', 'css/custom.css', 'downloads']
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 9

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False

AUTHORS_SAVE_AS = 'authors.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

#ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
