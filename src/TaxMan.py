class TaxMan:
    def __init__(self, items, tax) -> None:
        self.items = items
        self.tax = float(tax[:-1]) / 100
        self.__total = 0

    def calc_total(self):
        self.__total = round(sum(list(map(lambda i: i["price"], self.items))) * (1 + self.tax), 2)

    def get_total(self):
        return self.__total
