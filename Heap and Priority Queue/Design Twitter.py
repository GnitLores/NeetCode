from typing import List
from collections import defaultdict
import heapq

# Solution using approach from Merge K Sorted Lists problem.
# Keep track of tweet time with a count. Decrement for use with minheap as maxheap.
# Store people being followed as a set of userIds in dictionary with key userId. Unfollowing would be slow with lists instead of sets.
# Store tweets with their time (count) as lists in dictionary with key userId. Tweets are automatically ordered.
# The complex part is getting news feed:
# This is essentially a Merge K Sorted Lists problem.
# We want 10 most recent tweets from the user tweets and all follower tweets.
# Solve with heap.
# Add most recent tweet from all lists to heap WITH USER ID AND TWEET INDEX IN THAT LIST.
# Pop most recent tweet and then push the next most recent tweet from the user to heap with that info.
# Do this 10 times.
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # contians lists of [count, tweetId]
        self.followMap = defaultdict(set) # contains sets of userIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId) # Users "follows" themselves.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # Index of most recent tweet by followees
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1]) # include user ID and index of next tweet from that user
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0: # If user has more tweets, push their next tweet on the heap
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)        # User 1 posts a new tweet (id = 5).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)           # User 1 follows user 2.
twitter.postTweet(2, 6)        # User 2 posts a new tweet (id = 6).
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)         # User 1 unfollows user 2.
print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.