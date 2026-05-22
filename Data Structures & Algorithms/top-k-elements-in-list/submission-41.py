class Solution:
    # O(nlogn) : not optimal
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) # val : freq

        for num in nums:
            freq[num] += 1
        
        res = list(freq.items())
        res.sort(key=lambda x: x[1], reverse=True)

        return [res[i][0] for i in range(k)]
