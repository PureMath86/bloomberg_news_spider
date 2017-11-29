from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Bloomberg(BasePortiaSpider):
    name = "www.bloomberg.com"
    allowed_domains = [u'www.bloomberg.com']
    start_urls = [u'https://www.bloomberg.com/view/topics/law']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.article_158LU',
                [
                    Field(
                        u'topic',
                        '.topic_3cwIs > a *::text',
                        []),
                    Field(
                        u'author',
                        '.content_23myt > .authors_3ICjQ > .inline_3EZyl > .byline_2y1Ql *::text',
                        []),
                    Field(
                        u'link',
                        '.content_23myt > .title_3Ob7U > a::attr(href)',
                        []),
                    Field(
                        u'title',
                        '.content_23myt > .title_3Ob7U > a *::text',
                        [])])]]
