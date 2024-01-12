# E-commerce Dashboard

- E-commerce dashboard project that allows the user to:
	- Dump sales data (.csv or .xlsx format) from an e-commerce platform, and perform an ETL (extract-transform-load) pipeline on the data to use for analytics.
	- Features of the dashboard:
		- Total number of orders.
		- Total items ordered.
		- Total revenue.
		- Average revenue per order.
		- Orders and revenue per day.
		- Orders, revenue and average revenue per country.
		- Orders and revenue per delivery type.
		- Days taken to dispatch orders from the order date.

## Running Locally

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
- Run main script:
	- <code>python3 src/app.py</code>
- Navigate to <code>http://<LOCAL_HOST>:8080/</code> to view the dashboard.
