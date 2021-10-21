import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        '''
        GREEDY
        
        num_coins = 0
        change_left = amount
        
        coins.sort()
        
        print(coins)
            
        for i in range(len(coins) - 1, -1 , -1):
            
            num_coins += change_left // coins[i]
            
            change_left = change_left % coins[i]
        
        return num_coins if change_left == 0 else -1
        '''
        
        # answers with max num of coins
        least_coins = [sys.maxsize] * (amount + 1)
        
        # 0th position = 0 coins to sum to 0
        least_coins[0] = 0
        
        # for each level of change up to amount
        for i in range(amount+1):
            
            # for each type of type
            for coin in coins:
                
                # if amount leftover - coin == 0 or more less leftover, we have possible answer
                if i - coin >= 0:
                    
                    # update ith position matching change needed to either current least number of coins or new number of coins
                    # 1 + least_coins[i - coin]
                    # 1 meaning accept current coin, i - coin meaning look in 'cache' or precalculated
                    least_coins[i] = min(least_coins[i], 1 + least_coins[i - coin])
                
        # last position meaning num of coins needed at amount
        # if unchanged meaning from first initialization, -1
        return least_coins[-1] if least_coins[-1] != sys.maxsize else -1