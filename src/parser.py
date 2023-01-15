# -*- coding: utf-8 -*-
from StockHistory import StockHistory
import json
import os

STOCK_FOLDER = "stock_market_data"


def parseDataset(dataset: str) -> list[StockHistory]:
    dataset_path = os.path.join(STOCK_FOLDER, dataset, "json")
    dataset_stocks = os.listdir(dataset_path)

    stocks = []

    for stock_name in dataset_stocks:
        stock_path = os.path.join(dataset_path, stock_name)
        with open(stock_path) as json_file:
            try:
                stock = StockHistory(
                    json.load(json_file)
                )  # Create a dictionary from the json
                stocks.append(stock)  # Create a stock history object from the json

                print(f"Loaded: {stock.get_name()}")
            except Exception as e:
                print(e)

    return stocks


def parseDatasets(datasets: list[str]) -> list[StockHistory]:
    stocks = []
    for dataset in datasets:
        stocks.extend(parseDataset(dataset))

    return stocks
