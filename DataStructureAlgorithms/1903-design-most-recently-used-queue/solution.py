from collections import deque

class MRUQueue:
    def __init__(self, n: int):
        # We're going to break up the numbers into buckets of size `sqrt(n)`.
        # Ceil because even if the bucket won't be full, we need the bucket
        # to store whatever numbers are there, e.g.
        # n = 8. We need 3 buckets: [1,2,3]  [4,5,6]  [7,8]
        # sqrt(8) is 2.82.. but we need 3 buckets.
        self.sqrt = ceil(math.sqrt(n))
        self.buckets = []

        nums = list(range(1, n + 1))
        # Break up the numbers into chunks of size sqrt(n).
        chunks = [nums[i: i + self.sqrt] for i in range(0, len(nums), self.sqrt)]

        for chunk in chunks:
            self.buckets.append(deque(chunk))

    def fetch(self, k: int) -> int:
        # Question says k is 1-indexed, but our buckets are 0-indexed.
        k -= 1
        bucket_idx = k // self.sqrt
        num_idx = k % self.sqrt  # Index in the bucket.
        bucket = self.buckets[bucket_idx]
        target_num = bucket[num_idx]

        # Remove the target number by re-creating the bucket without it.
        new_bucket = deque()
        for i, num in enumerate(bucket):
            if i != num_idx:
                new_bucket.append(num)
        self.buckets[bucket_idx] = new_bucket

        # Append the target num to the tail.
        self.buckets[-1].append(target_num)

        # For this bucket and each subsequent, move down 1 element
        # to fill the gap of the moved target number.
        for b in range(bucket_idx, len(self.buckets) - 1):
            left_bucket = self.buckets[b]
            right_bucket = self.buckets[b + 1]

            left_bucket.append(right_bucket.popleft())
        return target_num
