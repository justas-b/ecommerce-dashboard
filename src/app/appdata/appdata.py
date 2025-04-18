import sys

sys.path.append("./")
from src.data_utils.transformer import DataTransformer
from src.data_utils.extractor import DataExtractor


transformer = DataTransformer()
transformer.apply_transformations()
extractor = DataExtractor(transformer.df)

START, END = extractor.date_range()
NUM_OF_DAYS = extractor.number_of_days()
TOT_REVENUE = extractor.total_revenue()
TOT_ORDERS = extractor.total_orders()
TOT_ITEMS = extractor.total_items()
DAILY_REVENUE = round(TOT_REVENUE / NUM_OF_DAYS, 2)
DAILY_ORDERS = round(TOT_ORDERS / NUM_OF_DAYS, 2)

TOP_ORDERS_DATE, TOP_ORDERS_DATE_CT = extractor.best_datetime_performance("orders", "date")
TOP_REVENUE_DATE, TOP_REVENUE_DATE_CT = extractor.best_datetime_performance("revenue", "date")

TOP_ORDERS_DAY, TOP_ORDERS_DAY_CT = extractor.best_datetime_performance("orders", "weekday")
TOP_REVENUE_DAY, TOP_REVENUE_DAY_CT = extractor.best_datetime_performance("revenue", "weekday")

TOP_ORDERS_MONTH, TOP_ORDERS_DAY_MONTH = extractor.best_datetime_performance("orders", "month")
TOP_REVENUE_MONTH, TOP_REVENUE_MONTH_CT = extractor.best_datetime_performance("revenue", "month")

TOP_ORDERS_COUNTRY, TOP_ORDERS_COUNTRY_CT = extractor.country_grouping("orders").agg(["idxmax", "max"])
TOP_REVENUE_COUNTRY, TOP_REVENUE_COUNTRY_CT = extractor.country_grouping("revenue").agg(["idxmax", "max"])