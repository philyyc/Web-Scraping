import scrapy


class FinancemodelingSpider(scrapy.Spider):
    name = 'FinanceModeling'
    # Set the name of the spider
    allowed_domains = ['site.financialmodelingprep.com']
    # Limit the domains

    def __init__(self, **kwargs):
        # Define the initialisation to include an optional argument which determins the company to search

        super().__init__(**kwargs)
        # Inherit the base class FinancemodelingSpider, with an optional argument
        self.start_urls = [f'https://site.financialmodelingprep.com/search?q={self.company}']
        # Set the start url based on the user's company name input

    def parse(self, response):
        table = response.css("tbody tr.search-page__item")
        # Look for the table containing search results

        if len(table) == 0:
            print("Error, company is not found")
            yield{}
            # Error message and empty output if the table of search results is empty (company not found)
        
        for company in table:
            data = dict()
            # Initialise a dictionary for storing various stock market attributes of a company
            data["type"] = company.css("td::text")[0].get()
            data["abbreviation"] = company.css("td::text")[1].get()
            data["name"] = company.css("td::text")[2].get()
            data["price"] = "${price}".format(price=company.css("td::text")[3].get())
            # Get the type, abbreviation, name and price of each search result

            if len(company.css("td span::text")) == 3:
                data["change"] = str(company.css("td span::text")[0].get()) + "$" +str(company.css("td span::text")[1].get())
                data["perc_change"] = company.css("td span::text")[2].get()
            else:
                data["change"] = "-${price}".format(price=company.css("td span::text")[0].get()[1:])
                data["perc_change"] = company.css("td span::text")[1].get()
            # The website displays positive and negative values differently, this is dealt with with an if...else... statement

            individual_url = "https://site.financialmodelingprep.com/financial-summary/{url}".format(url=data["abbreviation"])
            # Get the URL of the insight page of each search result

            if data["type"] == "Stock":
                yield response.follow(individual_url, callback=self.parse_stock, meta={"data": data})
                # Only allow the spider to enter insight pages of stocks, not funds or cryptocurrencies
                # parse_stock function is used to parse each insight page
                # Meta allows data to be passed from the main parse function to the sub-parse function
    
    def parse_stock(self, response):
        data = response.meta.get("data")
        # Get the data from meta
        tables = response.css(".table")
        # Look for the table containing statistics

        if len(tables) == 0:
            print("Error, company is not found")
            data["avg_vol"] = ""
            data["mark_cap"] = ""
            data["roe"] = ""
            data["roa"] = ""
            data["PtoE"] = ""
            data["PtoB"] = ""

            yield data
            # Error message and half-empty output if the insight page is not found

        data["avg_vol"] = tables[0].css("tr")[3].css("td::text").get()
        data["mark_cap"] = tables[0].css("tr")[4].css("td::text").get()
        data["roe"] = tables[1].css("tr")[2].css("td span::text").get()
        data["roa"] = tables[1].css("tr")[3].css("td span::text").get()
        data["PtoE"] = tables[1].css("tr")[6].css("td::text").get()
        data["PtoB"] = tables[1].css("tr")[7].css("td::text").get()
        # Get the average volume, market cap, return on equity, return on assets, price-to-earnings ratio and price-to-book ratio

        yield data

