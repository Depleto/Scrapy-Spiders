import scrapy
import json
'''
Identifies which of IMDb's current most popular movies have the provided actor/actors
'''

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    imbd_url = "https://imdb.com{}"
    start_urls = [imbd_url.format("/chart/moviemeter/?ref_=nv_mv_mpm")]

    # List of Actors
    actors = ["Adam Sandler"]
    output_dic = {actor : [] for actor in actors}



    def parse(self, response):
        title_hrefs = response.css("td.titleColumn > a::attr(href)").getall()
        for title in title_hrefs:
            title += "fullcredits"
            yield scrapy.Request(url = self.imbd_url.format(title) , callback = self.parse_actors)



    def parse_actors(self, response):
        cast_list = response.css("td.primary_photo > a > img::attr(title)").getall()
        title = response.css("h3 > a::text").get()


        for actor in self.actors:
            if actor in cast_list:
                with open("log.txt", 'a') as f:
                    f.write(f'Actor: {actor},  Movie: {title}' + "\n")





