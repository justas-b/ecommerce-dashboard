# E-commerce Dashboard

- E-commerce dashboard project that allows the user to:
	- Dump sales data (CSV format) from an e-commerce platform (currently only Etsy), and performs an ETL (extract-transform-load) pipeline on the data
	- Dashboard that displays data using the cleaned data:
		- Total number of orders
		- Total items ordered
		- Total revenue
		- Average revenue per order
		- Orders and revenue per day
		- Orders, revenue and average revenue per country
		- Orders and revenue per delivery type
		- Days took to dispatch orders from the order date

## Running Locally

- Download entire <code>ecommerce-dashboard/</code> folder
- RECOMMENDED: Create a virtual environment to run the application
- Install required libraries
	- <code>pip3 install -r requirements.txt</code>
- Drop a CSV file into the parent directory (named <code>sold-order-items.csv</code>
- Run data cleaning script
	- <code>python3 data_scrub.py</code>
-  Run dashboard app
	- <code>python3 app.py</code>
- Navigate to <code>http://<LOCAL_HOST>:8080/</code> to view the dashboard
