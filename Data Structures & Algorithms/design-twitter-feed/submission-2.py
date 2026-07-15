class Twitter:

    def __init__(self):
        # key: userid, value: (time, tweet)
        self.tweet = defaultdict(list)
        # key: userid, value: following
        self.users = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time, tweetId))
        if len(self.tweet[userId]) > 10:
            self.tweet[userId].pop(0)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.users[userId].add(userId)
        for followee in self.users[userId]:
            for time, tweet in self.tweet[followee]:
                heapq.heappush(minHeap, (time, tweet))
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        maxHeap = []
        while minHeap:
            time, tweet = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, (-time, tweet))
        ret_val = []
        while maxHeap:
            _, tweet = heapq.heappop(maxHeap)
            ret_val.append(tweet)
        return ret_val
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
