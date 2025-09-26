

    
class MyStack:
    
    def __init__(self):
        self.stack = deque()
        self.helper_stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        while self.stack:
            self.helper_stack.append(self.stack.popleft())
        self.helper_stack, self.stack = self.stack, self.helper_stack

    def pop(self) -> None:
        return self.stack.popleft() 

    def top(self) -> int:
        if not self.empty():
            return self.stack[0]
        return None

    def empty(self) -> bool:
        return not self.stack
    
class MyQueue:

    def __init__(self):
        self.queue = deque()
        self.helper_queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        while self.queue:
            self.helper_queue.append(self.queue.popleft())
        self.helper_queue, self.queue = self.queue, self.helper_queue

    def pop(self) -> int:
        return self.queue.popleft()

    def empty(self) -> bool:
        return not self.queue
    
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        
        return(-1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index = {}
        longest = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_to_index and char_to_index[char] >= left:
                left = char_to_index[char] + 1 
            char_to_index[char] = right
            longest = max(longest, right - left + 1)
        return(longest)
    def countSubarrays(self, nums: list[int], k: int) -> int:
        final_list = []

        def recursive_func(nums, current_combo, start_idx, k, final_list):
        # Check current combination
            if current_combo and sum(current_combo)*len(current_combo) < k:
                final_list.append(current_combo.copy())
            
            # Try adding each remaining element
            for i in range(start_idx, len(nums)):
                current_combo.append(nums[i])
                recursive_func(nums, current_combo, i + 1, k, final_list)
                current_combo.pop()  # Backtrack
            
            return final_list
        recursive_func(nums, [], 0, k, final_list)
        # Remove duplicates by converting subarrays to tuples and back to lists
        final_list = list(dict.fromkeys(tuple(subarray) for subarray in final_list))
        final_list = [list(t) for t in final_list]  # Convert tuples back
        final_count = len(final_list)
        return final_count 
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)
        else:
            res.append(".") 
        # map: remainder -> index in result
        seen = {}

        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(res)

