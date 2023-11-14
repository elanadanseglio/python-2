class Invoice:
    def __init__(self, string) -> None:
        self.array_stuff = string.split(",")
        self.__invoice_id = self.array_stuff[0]
        self.__user_id = self.array_stuff[1]
        self.__amount = self.array_stuff[2]
        self.__paid = self.array_stuff[3]

    def __repr__(self):
        return f"Invoice(invoice_id={self.__invoice_id}, user_id={self.__user_id}, amount={self.__amount}, paid={self.__paid})"
