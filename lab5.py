from Queue import Queue
from Stack import Stack

class ConvertToBinaryWithQueue():
    def __init__(self, value):
        self.value = value
        self.queue = Queue()
    
    def ToBinary(self):
        highest_power_of_two = 1

        while highest_power_of_two * 2 < self.value:
             highest_power_of_two *= 2

        while highest_power_of_two >= 1:
            if self.value // highest_power_of_two == 0:
                self.queue.enqueue("0")
            else:
                self.queue.enqueue("1")
            
            self.value %= highest_power_of_two

            highest_power_of_two /= 2

        binary = ""

        while not self.queue.IsEmpty():
            binary += self.queue.dequeue()

        return binary

class ConvertToBinaryWithStack():
    def __init__(self, value):
        self.value = value
        self.stack = Stack()
    
    def ToBinary(self):
        while self.value >= 1:
            if self.value % 2 == 0:
                self.stack.push("0")
            else:
                self.stack.push("1")
            self.value //= 2

        binary = ""

        while not len(self.stack) == 0:
            binary += self.stack.pop()

        return binary


toConvert = ConvertToBinaryWithQueue(255)
print( toConvert.ToBinary() )
toConvert = ConvertToBinaryWithStack(255)
print( toConvert.ToBinary() )
