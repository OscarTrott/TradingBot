# -*- coding: utf-8 -*-
# File to encode a stocks trading history


class StockHistory:
    def __init__(self, data: dict):

        assert len(data["chart"]["result"]) == 1

        # Meta information
        meta = data["chart"]["result"][0]["meta"]
        self.name = meta["symbol"]

        if len(data["chart"]["result"][0]["indicators"]["quote"][0]) == 0:
            raise Exception(f"No data for symbol {self.name}")

        # Price history, just market close
        self.priceHistory = data["chart"]["result"][0]["indicators"]["quote"][0][
            "close"
        ]

    def get_name(self) -> str:
        return self.name
