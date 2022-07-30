import pickle
from fastapi import FastAPI
loaded_model = pickle.load(open("recommendation_model.sav", 'rb'))
app = FastAPI()

@app.get("/")
def getRecommendation():
    recommended = []
    article = "space"
    for i , doc in enumerate(loaded_model.recommend(text = article,n = 5)):
        print(i+1)
        recommended.append ( str(i+1)+"  "+" ".join(doc['text'].split()[:500]))
        
    return [{
        "recommended":recommended
    }]

