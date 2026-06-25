from fastapi import FastAPI 
from topic import TopicBasics
from database import add_topic, get_all_topics, update_topic, delete_topic, get_this_topic
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message" : "Hello World"}

@app.get("/topics")
def fetch_topics():
    return get_all_topics()

@app.post("/add-topic")
def new_topic(name):
    new = TopicBasics(name)
    add_topic(new)    

@app.delete("/delete-topic")
def rem_topic(id : int):
    delete_topic(id)

@app.post("/review")
def review_topic(id : int, quality : int):
    info = get_this_topic(id)
    this_object = TopicBasics(info[0]['name'])
    this_object.id = info[0]['id']
    this_object.rep_count = info[0]['rep_count']
    this_object.EF =info[0]['ef']
    this_object.interval = info[0]['interval']
    this_object.next_review_date = info[0]['next_review_date']
    this_object.review(quality)
    update_topic(this_object)
    


    

