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
            if followee in self.tweet:
                idx = len(self.tweet[followee]) - 1
                time, tweet = self.tweet[followee][idx]
                # this is a max heap
                heapq.heappush(minHeap, (-time, tweet, followee, idx))
        res = []
        while minHeap and len(res) < 10:
            time, tweet,followee, idx = heapq.heappop(minHeap)
            res.append(tweet)
            if idx - 1 >= 0:
                time, tweet = self.tweet[followee][idx-1]
                heapq.heappush(minHeap, (-time, tweet, followee, idx - 1))
        return res

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
