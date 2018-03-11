class Call(object):
    def __init__(self, unique_id, name, phone_number, call_time, reason):
        self.unique_id = unique_id
        self.name = name
        self.phone_number = phone_number
        self.call_time = call_time
        self.reason = reason
    def display(self):
        print 'Id: ' + self.unique_id + ' | Name: ' + self.name + ' | Phone Number: ' + self.phone_number + ' | Time: ' + self.call_time + ' | Reason: ' + self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, newCall):
        self.calls.append(newCall)
        self.queue_size += 1
        return self
#Bubble Sort:
    def sort(self):
        for i in range(0, self.queue_size):
            for j in range(0, self.queue_size-i-1):
                if self.calls[j].call_time > self.calls[j+1].call_time:
                    self.calls[j], self.calls[j+1] = self.calls[j+1], self.calls[j]
        return self
    # deletes the first item in queue:
    # def remove(self):
    #     if self.queue_size > 0:
    #         del self.calls[0]
    #         self.queue_size -= 1
    #     return self
    def remove(self, byNumber):
        for i in range (0, self.queue_size):
            if self.calls[i].phone_number == byNumber:
                self.calls.pop(i)
                self.queue_size -= 1
        return self
    def info(self):
        for queuedCall in self.calls:
            queuedCall.display()
        print 'Queue Size: ' + str(self.queue_size)
        return self

call1 = Call('1', 'Pete', '555-5555', '1200', 'Assignment')
call2 = Call('2', 'Todd', '666-5555', '1300', 'Instructing')
call3 = Call('3', 'Minh', '777-5555', '1400', 'Programing')
# call1.display()
# call2.display()
# call3.display()

call_center1 = CallCenter()

# call_center1.add(call1).info()
call_center1.add(call1).add(call2).remove(call2).info()
call_center1.add(call3).add(call1).add(call2).sort().info()
# call_center1.remove('555-5555').info()