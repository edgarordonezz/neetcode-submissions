import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        tweets.extend(self.tweets[userId])
        for followee in self.following[userId]:
            tweets.extend(self.tweets[followee])
        res = heapq.nlargest(10, tweets)
        feed = []
        for time, tweetId in res:
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)