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
REVENUE_PER_ORDER = round(TOT_REVENUE / TOT_ORDERS, 2)
DAILY_ORDERS = round(TOT_ORDERS / NUM_OF_DAYS, 2)