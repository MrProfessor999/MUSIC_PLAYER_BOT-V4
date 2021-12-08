
#  (c) 2020 Stɑrry Shivɑm // This file


from platform import python_version
from telegram import __version__ as _libv_

# Contents
MOVIE_STR = """
️<b>{}</b> : {}

• Status : <pre>{}</pre>
• Genres : <pre>{}</pre>
• Languages : <pre>{}</pre>
• Runtime : <pre>{} minutes</pre>
• Budget : <pre>{}</pre>
• Revenue : <pre>{}</pre>
• Release Date : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Popularity : <pre>{}</pre>

• OverView : <em>{}</em>
"""

TV_STR = """
<b>{}</b>

• Created by : <pre>{}</pre>
• Genres : <pre>{}</pre>
• Languages : <pre>{}</pre>
• Episodes Runtime : <pre>{}</pre>
• First aired : <pre>{}</pre>
• Last aired : <pre>{}</pre>
• Status : <pre>{}</pre>
• Seasons : <pre>{}</pre>
• Total EPs : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Production Company : <pre>{}</pre>

• OverView : <em>{}</em>
"""

ANIME_STR = """
<b>{}</b> | <b>{}</b>

• Category : <pre>{}</pre>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First aired : <pre>{}</pre>
• Last aired : <pre>{}</pre>
• Runtime : <pre>{} minutes</pre>
• No of episodes : <pre>{}</pre>

• Synopsis : <em>{}</em>
"""

MANGA_STR = """
<b>{}</b> | <b>{}</b>
• Type : <pre>{}</pre>
• Average Rating : <pre>{}</pre>
• Status : <pre>{}</pre>
• First release : <pre>{}</pre>
• Last release : <pre>{}</pre>
• Volume count : <pre>{}</pre>
• No of chapters : <pre>{}</pre>
• Serialization : <pre>{}</pre>

• Synopsis : <em>{}</em>
"""

# Inline Content
INLINE_STR = """
• <b>Title</b> : {}
• <b>Release</b> : <pre>{}</pre>
• <b>Popularity</b> : <pre>{}</pre>
• <b>Language</b> : <pre>{}</pre>
• <b>Average Rating</b> : <pre>{}</pre>

• <b>OverView</b> : <em>{}</em>
"""

INLINE_DESC = """
<b>Usage:</b> <pre>&lt;tv&gt; title</pre> <b>or</b> <pre>&lt;movie&gt; title</pre> <b>in inline query.</b>

Examples:
× <pre>&lt;movie&gt; Avengers Endgame</pre>
× <pre>&lt;tv&gt; Breaking Bad</pre>
× <pre>&lt;anime&gt; Attack on Titan</pre>
• You can try on buttons below!
"""


# Start
START_STRING = """
Hey {}, I'm acutebot and i can help you to get \
information about your favorite movies, tv and anime shows, you can also download \
music & can view song lyrics using me! Just click the button \
below to get started with list of possible commands...

You can also search movies, tvshows & \
anime inline! just type <pre>@acutebot</pre> in \
your message box and follow the instructions.

And don't forget to smile, atleast once in a while ;)
"""
START_STRING_GRP = "Hmmm?"


# About
ABOUT_STR = f"""
I'm fully written in \
Python3 by <a href="tg://user?id=894380120">starry</a>, \
feel free to report him if you find any rough edge inside me.

<b>×</b> Bot version : <pre>{__version__}</pre>
<b>×</b> Python version : <pre>{python_version()}</pre>
<b>×</b> Library version : <pre>PTB {_libv_}</pre>
<b>×</b> Movies & TV data : <pre>themoviedb.org</pre>
<b>×</b> Anime data from : <pre>kitsu.io</pre>
<b>×</b> Music data from : <pre>deezer.com</pre>
<b>×</b> Lyrics data from : <pre>genius.com</pre>

If you enjoyed using me & wanna support my creator \
hit the donate button below, since he's just a student so \
every little helps to pay for my server, and ofcourse boosting morale ;)

"""

# Help
HELP_STR = """
Hey there, click on the buttons below to get documentations \
for the related functions.
"""

MOVIE_HELP = """
<b> help for Movies 😉 </b>

<b>×</b> /movies : Search for info about your favorite movies.
"""

ANIME_HELP = """
<b>🗒️ Documentation for Anime & Manga related functionsfunctions:</b>

<b>×</b> /anime : Search for info about your favorite anime titles.
<b>×</b> /manga : Get information about your favorite manga titles.
"""
MUSIC_HELP = """
<b> music & lyrics related functions:</b>

<b>×</b> /music : Download your favorite music in high resolution.
<b>×</b> /lyrics : Get lyrics for your favorite songs.
"""
SUB_HELP = """

<b>×</b> /subtitle : Download subtitles for your movies.
"""

# Errors
API_ERR = "Sorry, couldn't reach API at the moment :("
NOT_FOUND = "Sorry, couldn't find any results for the query :("
INVALIDCAT = "Hmmm.. maybe you've sent wrong category to look for, please try again!"
KEYERROR = "Oops! something went wrong. Please try again :("

# Cancel
CANCEL = "Cancelled the current task!"

# To search
TOSEARCHMOVIE = "Please reply with the movie title you wanna look for."
TOSEARCHTV = "Please reply with the TV title you wanna look for."
TOSEARCH_ANIME = "Please reply with the anime title you want to look for."
TOSEARCH_MANGA = "Please reply with the manga name you wanna look for."

# Subtitles
TOSEARCHSUBS = "Please reply with the Movie | Anime name you want subs for."
SUBS_STR = "🏷 Subtitles for <b>{}</b>.\nClick on buttons below to download!"
