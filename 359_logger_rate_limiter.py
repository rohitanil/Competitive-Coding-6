"""
TC -> O(1)
SC -> O(M) where M is the average length of the key
Logic:
Use a hash map to store the message, timestamp as k,v pair.
When a new message, timesstamp arrives, check in hash map and see if its present or not. If not present, add to
hashmap and return true.
If present in hashmap, check if hashmap[msg]+10<= timestamp. If yes, update the hashmap and return true else it means the
mew message arrived within the predefined frame and return False
"""
class Logger:
    def __init__(self):
        self.logging_dict = {}
        self.delta = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logging_dict:
            self.logging_dict[message] = timestamp
            return True
        else:
            if self.logging_dict[message] + self.delta <= timestamp:
                self.logging_dict[message] = timestamp
                return True
            else:
                return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)