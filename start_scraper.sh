rm -rf output
scrapy crawl countries -o output/countries.json
scrapy crawl regions -o output/regions.json
