class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
                    break  # Stop checking once a match is found
        return count
        
