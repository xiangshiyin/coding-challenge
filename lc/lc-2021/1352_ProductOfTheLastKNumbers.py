class ProductOfNumbers:

    def __init__(self):
        self.preprod = [1]

    def add(self, num: int) -> None:
        if num==0:
            self.preprod = [1]
        else:
            self.preprod.append(self.preprod[-1] * num)
        # print(self.preprod)

    def getProduct(self, k: int) -> int:
        if k < len(self.preprod):
            return int(self.preprod[-1] / self.preprod[-(k+1)])
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
