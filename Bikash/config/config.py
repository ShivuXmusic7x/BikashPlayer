# Powered By @BikashHalder @AdityaHalder

import os
import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


if os.path.exists("Internal"):
  load_dotenv("Internal")


API_ID = int(getenv("API_ID", "f57f42e575437906b2be2e05f85ea977"))
API_HASH = getenv("API_HASH","f57f42e575437906b2be2e05f85ea977")
BOT_TOKEN = getenv("BOT_TOKEN""5791501037:AAEAe93nq-e5PZ-UJc_J6Who8GX84xMzdtg")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ziddiboy1762:ziddiboy1762@cluster0.yhk3i4m.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001466357800"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "QUEEN VC PLAYER")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1670396841").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY""42857c75-932e-4b3f-9287-e3cfc67b5840")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME""ShivuXmusic7x)
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/TEJXOS/ADITYAPLAYER",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bikash")
GIT_TOKEN = getenv("GIT_TOKEN","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")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/techSquad7x")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Fake_feelings7x")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/BikashHalder")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID","ca15fc236f4c4fe98ae8c02418ce58ee")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "db45af1a62d542faab7f473d51aa8b5d")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "25"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))


# Pyrogram String Sessions (Multi-Client)

STRING1 = getenv("STRING_SESSION", "BQBCCLZ5esdBmN0uJdj54Px6dmJrciMBbKO9knxt2NMOp8UGtSxIxiFdAJXwJHvR_CArGmf7WcTskp4HKBnwO4ZOknrZlC6Stq0igQ461IvmG-8t_-6AYVc9kQv8gpqAA-CAg54NfRXlPfgCqfHO8VzrIY2PJyxTX0BOc_YkoL3Jp1yjIIENN31DcTsC0_iTHUl4ozccLwz0ih4-lNGhivKeMyzbQ2i23ZAsZFfWVeaf5n958nhxPs1P9oo6FEhRBKfiiiQHBHEp00ts3etyzs3LBLrZDvhVr0bitrG-O5p_h8spiBqFqiB143dMRZ3pdFsy1So4TflREsLzbO55VKmnAAAAAThX180A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



### Do Not Touch Or Edit Codes After This Line
############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(1670396841)
############################
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################
LOG = 2
YTDOWNLOADER = 1
BANNED_USERS = filters.user()
LOG_FILE_NAME = "bikashlogs.txt"
############################


# All Images Of Bikash Aditya Player // @BIKASHHALDER @AdityaHalder
START_IMG_URL = getenv("START_IMG_URL", f"https://te.legra.ph/file/99d0261f0aa5512ad6753.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "resource/ping.jpeg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "resource/playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "resource/global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "resource/stats.jpeg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "resource/audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "resource/video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "resource/stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "resource/soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "resource/youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "resource/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "resource/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "resource/spotifyplaylist.jpeg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "resource/ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "resource/playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "resource/global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "resource/stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "resource/audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "resource/stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "resource/soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "resource/youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "resource/video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
