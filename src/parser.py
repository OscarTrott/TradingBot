from StockHistory import StockHistory


def parseDataset(dataset: str) -> list[StockHistory]:
    pass


def parseDatasets(datasets: list[str]) -> list[StockHistory]:
    stocks = []
    for dataset in datasets:
        stocks.append(parseDataset(dataset))

    return stocks
