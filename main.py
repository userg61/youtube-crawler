from collections import Counter

from crawler.filter import Filter
from crawler.loaders import Loader, Reloader, YoutubeDlLoader, Tab
from crawler.scrapper import Scrapper
from crawler import parsers

channel_id = 'UCO08VxZ3ZsYi5-TIsO3dvFw'
loader = Loader()
reloader = Reloader()
ydl_loader = YoutubeDlLoader()
filter = Filter()
scrapper = Scrapper(
    loader, reloader, ydl_loader,
    [
        parsers.HomePageParser(),
        parsers.VideosParser(max_page=3),
        parsers.ChannelsParser(max_page=3),
        parsers.AboutParser(),
    ],
    channel_filter=filter
)
descr = scrapper.parse(channel_id)
scrapper.download(descr[Tab.Videos][1]['video_id'])
print(descr)

