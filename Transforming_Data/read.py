import pandas as pd

def load_data():
    pass
    
    if __name__ == "__main__":
        hn_stories=pd.read_csv("hn_stories.csv")
        hn_stories.columns=["submission_time", "upvotes", "url", "headline"]
        print (hn_stories)
        load_data()
