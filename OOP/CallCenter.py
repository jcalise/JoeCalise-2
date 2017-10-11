from datetime import datetime

class Call(object):
    def __init__(self,uni_id,caller_name,caller_number,call_reason):
        self.uni_id = uni_id
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.call_reason = call_reason
        self.call_time = datetime.now()

    def display(self):
        print "Caller ID:", self.uni_id
        print "Call Time:", self.call_time
        print "Caller Name:", self.caller_name
        print "Caller Number:", self.caller_number
        print "Call Reason:", self.call_reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self

    def info(self):
        print "Queue Size:", self.queue
        for call in self.calls:
            print "Caller Name:", call.caller_name, ", Number:", call.caller_number
        return self

c1 = Call(123,"Joe", "555-555-5555", "Refund")
c2 = Call(125,"Greg", "555-555-5555", "Complaint")
c3 = Call(125,"Fred", "555-555-5555", "Question")

CallCenter = CallCenter()
CallCenter.add(c1).add(c2).info()
