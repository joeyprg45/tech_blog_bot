import requests
import json

# 検索タグの設定
search_tags = ["Python", "機械学習", "MachineLearning", "DeepLearning", "競技プログラミング", "R"]

# DiscordのサーバーのWebhook URL
webhook_url = "https://discord.com/api/webhooks/1284082781865115728/Uco5ccj4IZuF4bTkYjroTsuJf6sY_1gY_qhPAmB03KLdlCegRSp3fmwLxG2gAWL7aZuX"

api_url = "https://zenn-api.netlify.app/trendTech.json"
res = requests.get(api_url)
trends = json.loads(res.text)

link_urls = []
tags = []
for i in range(len(trends)):
    link_url = trends[i]["node"]["linkUrl"]
    link_urls.append(link_url)
    tags_temp = []
    for j in range(len(trends[i]["node"]["tags"])):
        tag = trends[i]["node"]["tags"][j]["name"]
        tags_temp.append(tag)
    tags.append(tags_temp)

send_urls = []
for i in range(len(trends)):
    for search_tag in search_tags:
        if search_tag in tags[i]:
            send_urls.append(trends[i]["node"]["linkUrl"])
            break
        else:
            continue

for send_url in send_urls:
    content = {
        "username":"Qiita2Discord",
        "content":f"{send_url}"
    }
    requests.post(webhook_url, content)
