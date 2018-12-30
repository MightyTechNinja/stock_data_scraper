import time
from bs4 import BeautifulSoup
import urllib.request as urllib2

# List of stocks and technicals to pull using the program. All the data will be stored in a dict.
stock_list = ['aapl', 'tsla', 'ge']
interested = ['Market Cap (intraday)', 'Return on Equity', 'Revenue', 'Quarterly Revenue Growth']
technicals = {}


def scrape_yahoo(stock):
	try:
		url = ('http://finance.yahoo.com/q/ks?s='+stock)
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		tables = soup.findAll('table', {"class" : 'table-qsp-stats'})	# Found using page inpection
		for table in tables:
			table_body = table.find('tbody')
			rows = table_body.find_all('tr')

			for row in rows:
				col_name = row.find_all('span')							# Use span to avoid supscripts
				col_name = [cell.text.strip() for cell in col_name]
				col_val = row.find_all('td')
				col_val = [cell.text.strip() for cell in col_val]
				technicals[col_name[0]] = col_val[1]					# col_val[0] is the name cell (with subscript)
	except Exception as e:
		print('failed in the main loop',str(e))


def main():

	for each_stock in stock_list:
		scrape_yahoo(each_stock)
		print(each_stock)
		for ind in interested:
			print(ind + ": "+ technicals[ind])
		print("------")
		time.sleep(1)													# Use delay to avoid getting flagged as bot


if __name__ == "__main__":
	main()

