# -*- coding: utf-8 -*-
import os
from parser import parseDatasets
from util import findElemInList


dataset_names = os.listdir("stock_market_data")


def run():
    print(
        f"Train with: \n 1. all data\n 2. {dataset_names[0]}\n 3. {dataset_names[1]}\n 4. {dataset_names[2]}\n 5. {dataset_names[3]}"
    )

    choice = input()

    datasets = []

    match int(choice):
        case 1:
            datasets = dataset_names
        case 2:
            datasets.append(findElemInList(dataset_names[0]))
        case 3:
            datasets.append(findElemInList(dataset_names[1]))
        case 4:
            datasets.append(findElemInList(dataset_names[2]))
        case 5:
            datasets.append(findElemInList(dataset_names[3]))
        case _:
            raise Exception("Requested a non-existent dataset, somehow...")

    stocks = parseDatasets(datasets)


if __name__ == "__main__":
    run()
