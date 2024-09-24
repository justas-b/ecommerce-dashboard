# [WIP] NOTE: 
- **This is something that I'm currently not working on, it is just a personal project that I started. If anyone is interested in this, please [contact me](https://www.linkedin.com/in/justasbauras/)!**

## Features
- Runs _any_ (**subject to complete date - see below**) dumped data from an e-commerce platform (CSV [.csv] or Excel [.xlsx] format), and performs an ETL pipeline on the data for use in analysis.
- Generator class that can be used to generate _random_ data to experiment with/to use if the user is unable to acquire their data.
- Analytics and data for the time range spanned by the data:
	- Dashboard (**general**):
		- General sales information  e.g., order and item counts, total revenue, average revenue (per order).
  	- Dashboard (**timeline analytics**):
  		- Selection of order and revenue counts for a variable granularity (daily, weekly and monthly).
  	- Dashboard (**destination country analytics**):
  		- Selection of best and worst (limit of 10) performing countries for the number of orders, total and average revenue.
  	- Dashboard (**delivery type analytics**):
  		- Distribution of the delivery types (pair or free) across orders and revenue.
  	- Dashboard (**to dispatch distribution**):
  		- Distribution of the number of days taken to dispatch orders from the sale date.

## Data Requirements
- Currently, the data that is needed for this dashboard to run successfully **must** contain the sale date (the date the order was made), quantity (number of items in the order), price (total price of the order - including shipping and fees), post date (the date that the order was dispatched), country (destination country) and the delivery cost (cost of delivery).
- If you are unable to acquire sales data, you can leave the <code>FILENAME</code> value in <code>config.json</code> <code>null</code> and this will generate random data for you to experiment with. An example of what the generator class outputs (the ideal form of the data) is:
  
	| sale_date  | quantity | price  | post_date  | country   | delivery_cost |
	|------------|----------|--------|------------|-----------|---------------|
	| 01/01/2023 | 3        | 62.58  | 06/01/2023 | Macedonia | 0             |
	| 01/01/2023 | 3        | 100.62 | 04/01/2023 | Laos      | 20.12         |
	| 01/01/2023 | 2        | 60.16  | 07/01/2023 | Chile     | 12.03         |

## Setup (Local)
- RECOMMENDED: Create a virtual environment to run the application:
	- <code>python3 -m venv venv</code>
	- <code>source ./venv/bin/activate</code>
- Install required dependencies:
	- <code>pip3 install -r requirements.txt</code>
- Dump data file into file into <code>src/data/</code>.
- Configure the application by editing the values in <code>config.json</code> to reflect the data you have:
	- <code>FILENAME</code>: The name of your data file dumped in <code>src/data/</code>.
	- <code>SALE_DATE</code>: Column name of the column that has the date of the sale.
	- <code>QUANTITY</code>: Column name of the column that has the number of items bought for an order.
	- <code>PRICE</code>: Column name of the column that has the total that a customer has paid for the order.
	- <code>POSTED_DATE</code>: Column name of the column that has the date that the order was dispatched.
	- <code>COUNTRY</code>: Column name of the column that has the destination country.
	- <code>DELIVERY_COST</code>: Column name of the column that has the delivery charge of the order.

## Usage (Local)
- Run main script:
	- <code>python3 src/app.py</code>
- Navigate to <code>http://<LOCAL_HOST>:8080/</code> to view and use the dashboard.
