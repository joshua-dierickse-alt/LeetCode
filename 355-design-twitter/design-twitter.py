from collections import defaultdict
import heapq

class User:
    def __init__(self):
        self.posts = []
        self.following = set()

class Twitter:
    def __init__(self):
        self.time = 0
        self.users = defaultdict(User)  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].posts.append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []

        def add_post(follower, i):
            if i >= 0:
                time, tweet = self.users[follower].posts[i]
                heapq.heappush(posts, (-time, tweet, follower, i - 1))

        add_post(userId, len(self.users[userId].posts) - 1)
        for follower in self.users[userId].following:
            add_post(follower, len(self.users[follower].posts) - 1)

        result = []

        for _ in range(10):
            if not posts:
                break

            _, tweet, follower, i = heapq.heappop(posts)
            add_post(follower, i)
            result.append(tweet)
            
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)