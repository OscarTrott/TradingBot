# -*- coding: utf-8 -*-
from StockHistory import StockHistory


def parseDataset(dataset: str) -> list[StockHistory]:
    return []


def parseDatasets(datasets: list[str]) -> list[StockHistory]:
    stocks = []
    for dataset in datasets:
        stocks.extend(parseDataset(dataset))

    return stocks
