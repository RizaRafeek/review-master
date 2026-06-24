import os
from supabase import Client, create_client
from dotenv import load_dotenv
from topic import TopicBasics

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_topic(topic):
    data = {
        "name" : topic.name,
        "rep_count" : topic.rep_count,
        "ef" : topic.EF,
        "interval": topic.interval,
        "next_review_date" : str(topic.next_review_date)
    }
    result = supabase.table("topics").insert(data).execute()
    topic.id = result.data[0]['id']

def get_all_topics():
    result = supabase.table("topics").select("*").execute()
    return result.data

def update_topic(topic):
    change = {
        "rep_count" : topic.rep_count,
        "ef" : topic.EF,
        "interval": topic.interval,
        "next_review_date" : str(topic.next_review_date)
    }
    supabase.table("topics").update(change).eq("id", topic.id).execute()

def delete_topic(id):
    supabase.table("topics").delete().eq("id", id).execute()

def get_this_topic(id):
    result = supabase.table("topics").select("*").eq("id", id).execute()
    return result.data

if __name__ =="__main__":
    print(supabase)
    test_topic = TopicBasics("test1")
    add_topic(test_topic)
    print(test_topic.id)
    test_topic.review(5)
    update_topic(test_topic)
    delete_topic(test_topic.id)
    