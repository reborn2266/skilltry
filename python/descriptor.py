#!/usr/bin/env python

class MailEvent(object):
   def fire(self, instance, cls):
      print "handling mail event from " + str(cls.__name__) + " " + str(instance.name)

class LogEvent(object):
   def fire(self, instance, cls):
      print "handling log event from " + str(cls.__name__) + " " + str(instance.name)

# using inheritance
class BaseWorker(object):
   def __init__(self, name):
      self.name = name
      self.event_factory = {"mail":MailEvent(), "log":LogEvent()}

   def event(self, evt):
      if evt in self.event_factory:
         self.event_factory[evt].fire(self, type(self))

class Worker(BaseWorker):
   pass

worker = Worker("SIMPLE")
worker.event("mail")
worker.event("log")

##### delegation approach #####
# naive way
class EventProxyA(object):
   def __init__(self):
      self.event_factory = {"mail":MailEvent(), "log":LogEvent()}

   def handle_event(self, evt, instance, cls):
      if evt in self.event_factory:
         self.event_factory[evt].fire(instance, cls)

class BaseWorkerA(object):
   def __init__(self, name):
      self.name = name
      self.event_proxy = EventProxyA()

   def event(self, evt):
      self.event_proxy.handle_event(evt, self, type(self))

class WorkerA(BaseWorkerA):
   pass

worker = WorkerA("SIMPLE_A")
worker.event("mail")
worker.event("log")

# dafe's approach
class EventProxyB(object):
   def __init__(self):
      self.event_factory = {"mail":MailEvent(), "log":LogEvent()}

   def __get__(self, instance, cls):
      def handle(evt):
         if evt in self.event_factory:
            # access caller's info without passing any parameter
            self.event_factory[evt].fire(instance, cls)
      return handle;

class BaseWorkerB(object):
	event = EventProxyB()
	def __init__(self, name):
		self.name = name

class WorkerB(BaseWorkerB):
   pass

worker = WorkerB("SIMPLE_B")
worker.event("mail")
Worker.__dict__['event'].__get__(worker, Worker)("mail")
