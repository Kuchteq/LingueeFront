import asyncio
from linguee_api.config import settings
from linguee_api.downloaders.httpx_downloader import HTTPXDownloader
from linguee_api.downloaders.memory_cache import MemoryCache
from linguee_api.downloaders.sqlite_cache import SQLiteCache
from linguee_api.linguee_client import LingueeClient
from linguee_api.parsers import XExtractParser
from linguee_api.models import (
    FollowCorrections,
)
page_downloader = MemoryCache(
    upstream=SQLiteCache(
        cache_database=settings.cache_database,
        upstream=HTTPXDownloader(),
    )
)

client = LingueeClient(page_downloader=page_downloader, page_parser=XExtractParser())



def GetWord(word):
    result = asyncio.run(client.process_search_result(
        query=word,
        src="de",
        dst="en",
        guess_direction=True,
        follow_corrections=FollowCorrections.ALWAYS,
    ))
    return result
#print(prepareForDisplay())






