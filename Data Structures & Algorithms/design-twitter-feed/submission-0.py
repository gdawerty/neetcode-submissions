class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = list(self.following[userId]) + [userId]
        heap = []
        res = []

        for f_id in followees:
            if self.posts[f_id]:
                idx = len(self.posts[f_id]) - 1
                time, tweet_id = self.posts[f_id][idx]
                heapq.heappush(heap, (time, tweet_id, f_id, idx))

        while heap and len(res) < 10:
            _, tid, fid, idx = heapq.heappop(heap)
            res.append(tid)

            if idx > 0:
                prev_time, prev_tid = self.posts[fid][idx - 1]
                heapq.heappush(heap, (prev_time, prev_tid, fid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
