class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if len(meetings) < n:
            return 0
        meetings.sort()
        # end time, room number, num of meetings
        used = []
        # rm number and num of meetings
        available = [(i, 0) for i in range(n)]
        for a, b in meetings:
            while used and used[0][0] < a:
                end_time, rm, num_meeting = heapq.heappop(used)
                heapq.heappush(available, (rm, num_meeting))
            if available:
                rm, num_meeting = heapq.heappop(available)
                heapq.heappush(used, (b, rm, num_meeting + 1))
            else:
                end_time, rm, num_meeting = heapq.heappop(used)
                heapq.heappush(used, (b-a + end_time, rm, num_meeting + 1))
                
        most_meeting = 0
        best_room = -1
        while used:
            _, rm, num_meeting = heapq.heappop(used)
            if num_meeting == most_meeting:
                if rm < best_room:
                    best_room = rm
            elif num_meeting > most_meeting:
                best_room = rm
                most_meeting = num_meeting
        while available:
            rm, num_meeting = heapq.heappop(available)
            if num_meeting == most_meeting:
                if rm < best_room:
                    best_room = rm
            elif num_meeting > most_meeting:
                best_room = rm
                most_meeting = num_meeting
        return best_room

        
        #     # print(heap)
        #     if heap and heap[0][0] < a:
        #         end, rm, num_meeting = heapq.heappop(heap)
        #         heapq.heappush(heap, (rm, b, num_meeting + 1))
        #     else:
        #         if len(heap) == n:
        #             # need to wait for the next avail room
        #             end, rm, num_meeting = heapq.heappop(heap)
        #             heapq.heappush(heap, (rm, b - a + end, num_meeting + 1))
        #         else:
                    
        #             heapq.heappush(heap,( len(heap), b, 1))
        # most_meeting = 0
        # best_room = -1
        # # print(heap)
        # while heap:
        #     end, rm, num_meeting = heapq.heappop(heap)
        #     if num_meeting == most_meeting:
        #         if rm < best_room:
        #             best_room = rm
        #     elif num_meeting > most_meeting:
        #         best_room = rm
        #         most_meeting = num_meeting
        # return best_room



