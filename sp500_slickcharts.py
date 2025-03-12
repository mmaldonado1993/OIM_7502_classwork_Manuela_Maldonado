import scrapy


class Sp500SlickchartsSpider(scrapy.Spider):
    name = "sp500_slickcharts"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://slickcharts.com"]

    def parse(self, response):
        pass

import scrapy
import csv

class Sp500SlickchartsSpider(scrapy.Spider):
    name = "sp500_slickcharts"
    allowed_domains = ["slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        """
        This function scrapes data from the S&P 500 performance table.
        """

        # Locate all table rows using CSS selector
        rows = response.css("table.table tbody tr")

        # Create a list to store scraped data
        data = []
        for row in rows:
            number = row.css("td:nth-child(1)::text").get()  # Rank number
            company = row.css("td:nth-child(2) a::text").get()  # Company Name
            symbol = row.css("td:nth-child(3) a::text").get()  # Stock Symbol
            ytd_return = row.css("td:nth-child(6)::text").get()  # Year-To-Date Return

            # Append data to list as a dictionary
            data.append({
                "Rank": number,
                "Company": company,
                "Symbol": symbol,
                "YTD Return": ytd_return
            })

        # Save data to a CSV file
        with open("sp500_performance.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Rank", "Company", "Symbol", "YTD Return"])
            writer.writeheader()
            writer.writerows(data)

        self.log("Data successfully saved to sp500_performance.csv")

