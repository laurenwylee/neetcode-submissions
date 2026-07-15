class Twitter:

    def __init__(self):
        self.user_tweet = defaultdict(deque)
        self.user_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].append(((self.time, tweetId)))
        if len(self.user_tweet[userId]) > 10:
            self.user_tweet[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.user_following[userId] | {userId}
        tweets = []
        heap = []
        for followee in following:
            if followee in self.user_tweet:
                idx = len(self.user_tweet[followee]) - 1
                time, tweetId = self.user_tweet[followee][idx]
                heapq.heappush(heap, (-time, tweetId, followee, idx))
        while heap and len(tweets) < 10:
            (time, tweetId, followeeId, idx )= heapq.heappop(heap)
            tweets.append(tweetId)
            if idx - 1 >= 0:
                new_time, new_tweetId = self.user_tweet[followeeId][idx - 1]
                heapq.heappush(heap, (-new_time, new_tweetId, followeeId, idx - 1))
        return tweets


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
        
