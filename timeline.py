class Timeline:
    def __init__(self, events) -> None:
        self.events = events
        self.sort_timeline()

    def sort_timeline(self):
        self.events.sort(key=lambda x: x[0])

    def add_event(self, year, events):
        lo, hi = 0, len(self.events)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.events[mid][0] == year:
                self.events[mid][1].extend(events)
                return
            elif year < self.events[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        self.events.insert(lo, (year, events))

    def get_timeline(self):
        return self.events
    
    def get_current_event(self, year):
        lo, hi = 0, len(self.events) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.events[mid][0] == year:
                return self.events[mid][1]
            elif self.events[mid][0] < year:
                lo = mid + 1
            else:
                hi = mid - 1

        return self.events[hi][1] if hi >= 0 else None
    
"""
Preliminary tests:

events = [(2005, ["job1", "job2"]), (2020, ["job3", "job4"]), (2040, ["job5", "job6"]), (2030, ["job7", "job8"])]
job_timeline = Timeline(events)
print(job_timeline.get_timeline())
print(2005, job_timeline.get_current_event(2005))
print(2020, job_timeline.get_current_event(2020))
print(2021, job_timeline.get_current_event(2021))
print(job_timeline.add_event(2030, ["job9"]))
print(2030, job_timeline.get_current_event(2030))
print(job_timeline.get_timeline())
print(2043, job_timeline.get_current_event(2043))
"""



