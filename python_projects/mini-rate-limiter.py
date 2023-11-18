import collections
from datetime import datetime

"""

Rate limiter
Build a rate limiter for an API that allows each user to access the API at most 5 times every 2 seconds.

Let's focus on getting something working using in-memory data structures.

It's okay to write code that's inefficient to start.

An example usage might look like:

Requirements:
User should only be able to access API at most 5 times every 2 seconds or (150 request a min)
- Caution with the rate limiter
- Treat the API as kind of black box

- How do we keep track of the number of requests we've made every two seconds
- We could keep track of the previous requests we've made in a list
- The list would contain the previous time-stamps that we've made a request
- When the incoming request comes in, we can simply query our in-memory datastructure, and see if we have
- 5 requests within 2 seconds
- Whats the best unit to store these log entries in

- Heap (which can sort things really efficiently)

"""


class RateLimiter:
    def __init__(self):
        # Instead of just storing each log line with timestamp,
        self.log = collections.defaultdict(list)
        self.timespan = 2000

    # Returns a boolean if we haven't exceeded 5 API requests within the 2 seconds
    def can_access(self, req):
        # We, we can simply loop through all the logs, and given a 2 second start, end time, we can return
        # True if there are less than 5 log lines else False break out of the loop
        now_time = datetime.now().timestamp()
        previous_time = datetime.now().timestamp() - self.timespan  # 2 seconds ago
        user = req['user']

        count = 0
        for time_stamp in self.log[user]:
            if previous_time <= time_stamp <= now_time:
                count += 1

            # Short circuits
            if count >= 5:
                return False

        return True

    def add_log_line(self, req):
        # We want to persist a new log line in self.log that represents when the API was called
        access_api_time = datetime.now().timestamp()
        user = req['user']
        self.log[user].append(access_api_time)

# Example API endpoint function
# def get_items(req):
#   if not rate_limiter.can_access(req.user):
#     return (429, None)
#   return (200, ["foo", "bar"])


def main():
    def get_items(req, rate_limiter):
        # print(req)
        if not rate_limiter.can_access(req):
            return False
        rate_limiter.add_log_line(req)
        return True
        #         return (429, None)
        # return (200, ["foo", "bar"])

    req = {}
    req['user'] = 'jack'
    rate_limiter = RateLimiter()
    assert (get_items(req, rate_limiter) == True)
    assert (get_items(req, rate_limiter) == True)
    assert (get_items(req, rate_limiter) == True)
    assert (get_items(req, rate_limiter) == True)
    assert (get_items(req, rate_limiter) == True)
    assert (get_items(req, rate_limiter) == False)  # Exceeded 5 at this point, so we should expect a false
    req = {}
    req['user'] = 'bob'
    assert (get_items(req, rate_limiter) == True)


if __name__ == '__main__':
    main()
