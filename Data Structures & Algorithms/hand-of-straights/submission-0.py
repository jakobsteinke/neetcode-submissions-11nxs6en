class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)
        while heap:
            card = heapq.heappop(heap)
            if counter[card] == 0:
                continue
            counter[card] -= 1
            if counter[card] > 0:
                heapq.heappush(heap, card)
            groupCounter = 1
            cur = card
            while groupCounter < groupSize:
                if counter[cur + 1] == 0:
                    return False
                groupCounter += 1
                counter[cur + 1] -= 1
                cur += 1
        return True
            
        
            



        