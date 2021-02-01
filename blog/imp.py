import json
import pandas as pd
import matplotlib.pyplot as plt
import requests


def plot(request)
    resss=requests.get('https://api.mentimeter.com/questions/48d75c359ce4/result', headers=headers).json()
    data = json.loads(resss)
    dates = [i['label'] for i in data["data"]]
    values = [i['score'] for i in data['data']]

    df = pd.DataFrame({'dates':dates, 'values':values})

    print(df.sort_values(by='dates'))

    plt.bar(dates, values)
    return render(request,'pavananna/home.html',plt.bar(dates, values))