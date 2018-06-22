# This coin change problem will have three implementations which I have found on the internet. 
# Diffrenet way to handle the same problem gives the ability to the programmer to think in many direction

class CoinChange:
    def __init__(self, coin):
        self.coin = coin
    # Coin change solution using recursion
    def change_recursion(self, amount, currentCoin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        else:
            result = 0
            for i in range(currentCoin, len(self.coin)):
                result += self.change_recursion(amount - self.coin[i], i)
        return result

    # Coin change using Dynamic programming
    def change_dynamic(self, amount):
        comibination = [0] * (amount+1)
        comibination[0] = 1
        for coin in self.coin:
            for i in range(1,amount+1):
                if i >= coin:
                    comibination[i] += comibination[i-coin]
        return comibination[amount]
    
    # Coin chamnge using Dynamic programming but this time the coins will be linear i.e. 1,2,3,4
    def change_dynamic_linear(self,amount):
        result = [[0] * (amount+1) for _ in range(len(self.coin)+1)]
        result[0][0] = 1
        for row in self.coin:
            for col in range(amount + 1):
                if row > col:
                    result[row][col] = result[row-1][col]
                else:
                    result[row][col] = result[row-1][col] + result[row][col - row]
        return result[len(self.coin)][amount]


coin = [1,2]
amount = 4
change = CoinChange(coin)
# All the results will be same which checks the validity of the implementation
print(change.change_recursion(amount, 0))
print(change.change_dynamic(amount))
print(change.change_dynamic_linear(amount))

