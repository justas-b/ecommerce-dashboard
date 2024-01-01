# E-commerce Dashboard

- E-commerce dashboard project that allows the user to:
	- Dump sales data (.csv or .xlsx format) from an e-commerce platform (currently only Etsy), and perform an ETL (extract-transform-load) pipeline on the data.
	- Dashboard that displays data using the cleaned data:
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
- Dump data file into file into **src/data/**.
- Run main script:
	- <code>python3 src/app.py</code>
- Navigate to <code>http://<LOCAL_HOST>:8080/</code> to view the dashboard.
