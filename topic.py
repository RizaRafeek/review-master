import datetime
class TopicBasics:
    def __init__(self, name):
        self.name = name
        self.rep_count = 0
        self.EF = 2.5
        self.interval = 0
        self.next_review_date = datetime.date.today() + datetime.timedelta(1)
        self.id = None
  
    def review(self, quality):
        if self.rep_count == 0:
            self.interval = 1
        elif self.rep_count == 1:
            self.interval = 6
        elif self.rep_count >= 2:
            self.interval = self.interval * self.EF
            self.interval = int(self.interval)
        self.rep_count += 1
        self.EF = self.EF + (0.1 - (5 - quality)*(0.08 + (5 - quality)* 0.02))
        if int(quality) < 3:
            self.rep_count = 0
            self.interval = 1
        self.next_review_date = datetime.date.today() +datetime.timedelta(self.interval)
    
    def is_due_today(self):
        if self.next_review_date <= datetime.date.today():
            return True
        else:
            return False

if __name__ == "__main__":
    Topic = TopicBasics("Machine Learning")
    Topic.review(5)
    print(Topic.interval)
    print(Topic.next_review_date)
    print(Topic.is_due_today())
    Topic.review(5)
    print(Topic.interval)
    print(Topic.next_review_date) 
    print(Topic.is_due_today())
    Topic.review(5)
    print(Topic.interval)
    print(Topic.next_review_date)
    print(Topic.is_due_today())
    Topic.review(1)
    print(Topic.interval)
    print(Topic.next_review_date)
    print(Topic.is_due_today())
    Topic2 = TopicBasics("Deep Learning")
    Topic2.next_review_date = datetime.date.today()
    print(Topic2.is_due_today())
    
    
    
