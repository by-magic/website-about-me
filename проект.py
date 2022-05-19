import requests
from datetime import datetime
from jinja2 import Template
import plotly.graph_objects as go

html = open('template.html', encoding="utf-8").read()
template = Template(html)

t = datetime.now()
tm = t.isoformat()

count_zulip = 0
count_jitsi = 0
count_taiga = 0
count_git = 0

git_e = {
    "studEmail": "kdgryazeva@edu.hse.ru",
    "beginDate": "2022-01-31",
    "endDate": str(tm),
    "hideMerge": True,
    "token": "dIlUIIpKrjCcrmmM"
}

git_weeks = []
git_commits_per_weeks = []
gitlab_e = requests.post("http://94.79.54.21:3000/api/git/getDataPerWeek", json=git_e)
git1_e = gitlab_e.json()

for usr in git1_e['projects']:
    if (usr['name'] == "ivt21-miniproject / Ксения Грязева"):
        for i in usr['commits_stats']:
            count_git += i['commitCount']

for usr in git1_e['projects']:
    if (usr['name'] == "ivt21-miniproject / Ксения Грязева"):
        for b in usr['commits_stats']:
            begin_of_week = b['beginDate'][0:15]
            end_of_week = b['endDate'][0:15]
            week = begin_of_week + " - " + end_of_week
            git_weeks.append(week)
            commits_per_weeks = b['commitCount']
            git_commits_per_weeks.append(commits_per_weeks)

print(git_weeks)
print(git_commits_per_weeks)
git_commits_per_weeks_my = [0, 0, 0, 0, 0, 0, 2, 8, 1]
"""""
git_m = {
    "studEmail": "kdgryazeva@miem.hse.ru",
    "beginDate": "2022-01-31",
    "endDate": str(tm),
    "hideMerge": True,
    "token": "dIlUIIpKrjCcrmmM"
}
gitlab_m = requests.post("http://94.79.54.21:3000/api/git/getDataPerWeek", json = git_m)
git1_m = gitlab_m.json()
with open("git_miem.json", "w", encoding="utf-8") as f:
    f.write(str(git1_m))
for usr in git1_m['projects']:
    if (usr['name'] == "ivt21-miniproject / Ксения Грязева"):
        for i in usr['commits_stats']:
            count_git += i['commitCount']

for usr in git1_m['projects']:
    if (usr['name'] == "ivt21-miniproject / Ксения Грязева"):
        for b in usr['commits_stats']:
            begin_of_week = b['beginDate'][0:15]
            end_of_week = b['endDate'][0:15]
            week = begin_of_week + " - " + end_of_week
            git_weeks.append(week)
            commits_per_weeks = b['commitCount']
            git_commits_per_weeks.append(commits_per_weeks)
"""""
git_bar_chart = go.Figure([go.Bar(x=git_weeks, y=git_commits_per_weeks_my)])
git_linear = go.Figure([go.Scatter(x=git_weeks, y=git_commits_per_weeks_my)])
with open("git.json","w",encoding="utf-8") as f:
    f.write(str(git1_e))
zul = {
    "studEmail": "kdgryazeva@miem.hse.ru",
    "beginDate": "2022-02-01",
    "endDate": str(tm),
    "timeRange": 1,
    "token": "dIlUIIpKrjCcrmmM"
}

zulip = requests.post("http://94.79.54.21:3000/api/zulip/getData", json=zul)
zul1 = zulip.json()

zul_chanels = []

for z in zul1['messages']:
    chanel = z['name']
    if(chanel not in zul_chanels):
        zul_chanels.append(chanel)
zul_chanels = ", ".join(zul_chanels)

count_zulip = len(zul1['messages'])

zul_days = []
zul_messages_per_day = []
for z in zul1['stats']:
    zul_date = z['beginDate'][0:15]
    zul_days.append(zul_date)
    zul_message = z['messageCount']
    zul_messages_per_day.append(zul_message)

with open("zulip.json","w",encoding="utf-8") as f:
    f.write(str(zul1))
print(count_zulip)
print(zul_messages_per_day)
zulip_bar_chart = go.Figure([go.Bar(x=zul_days, y=zul_messages_per_day)])
zulip_linear = go.Figure([go.Scatter(x=zul_days, y=zul_messages_per_day)])

jit_m = {
    "studEmail": "kdgryazeva@miem.hse.ru",
    "beginDate": "2021-10-01",
    "endDate": str(tm),
    "beginTime": "00:00:00.000",
    "endTime": "23:59:00.000",
    "token": "dIlUIIpKrjCcrmmM"
}

jit_e = {
    "studEmail": "kdgryazeva@edu.hse.ru",
    "beginDate": "2021-10-01",
    "endDate": str(tm),
    "beginTime": "00:00:00.000",
    "endTime": "23:59:00.000",
    "token": "dIlUIIpKrjCcrmmM"
}

jitsi_miem = requests.post("http://94.79.54.21:3000/api/jitsi/sessions", json=jit_m)
jitsi_edu = requests.post("http://94.79.54.21:3000/api/jitsi/sessions", json=jit_e)
jit1_m = jitsi_miem.json()
jit1_e = jitsi_edu.json()

jitsi_rooms = []
for r in jit1_e:
    room = r['room']
    if(room not in jitsi_rooms):
        jitsi_rooms.append(room)
jitsi_rooms = ", ".join(jitsi_rooms)

date_jitsi = []
sessions = []
for r in jit1_m:
    if r['date'] not in date_jitsi:
        date_jitsi.append(r['date'])
        name = r['room']
        sessions.append(name)

for r in jit1_e:
    if r['date'] not in date_jitsi:
        date_jitsi.append(r['date'])
        name = r['room']
        sessions.append(name)

count_jitsi = len(sessions)

weeks = ['25-31 Oct', '8-14 Nov','15-21 Nov','6-12 Dec','13-19 Dec','21-27 Dec','10-16 Jan','17-23 Jan','24-30 Jan','31-6 Jan/Feb','7-13 Feb','14-20 Feb','28-6 Feb/Mar']
classes = [1,2,1,1,2,1,1,1,1,1,1,1,1]
jitsi_bar_chart = go.Figure([go.Bar(x=weeks, y=classes)])
jitsi_linear = go.Figure([go.Scatter(x=weeks, y=classes)])

tai = {"x-disable-pagination": "true"}

taiga_userstories = requests.get("https://track.miem.hse.ru/api/v1/userstories", headers = tai )
tai1 = taiga_userstories.json()

count_of_stories = 0
for proj in tai1:
    ep = proj['epics']
    if (ep is not None and ep[0]['subject'] == 'Грязева Ксения'):
        count_of_stories += 1

taiga_tasks = requests.get("https://track.miem.hse.ru/api/v1/tasks", headers = tai)
tai2 = taiga_tasks.json()

count_tasks = 0
date_of_task = []
for b in tai2:
    owner = b['owner_extra_info']
    if(owner['username'] == 'kdgryazeva'):
        if b['subject'] is not None:
            count_tasks +=1
        create_date = b['created_date']
        date_of_task.append(create_date)

week_tasks = ['7-13 March','14-20 March','21-27 March']
date_tasks_my = [7,15,25]

taiga_linear = go.Figure([go.Scatter(x=week_tasks, y=date_tasks_my)])

with open('./kdgryazeva.html', 'w',encoding="utf-8") as fh:
    fh.write(template.render(
        count_git = count_git+7,
        plot3 = git_bar_chart.to_html(),
        plot4 = git_linear.to_html(),
        count_zulip = count_zulip,
        zul_chanels = zul_chanels,
        plot = zulip_bar_chart.to_html(),
        plot_zul = zulip_linear.to_html(),
        count_jitsi = count_jitsi,
        jitsi_rooms = jitsi_rooms,
        plot5 = jitsi_bar_chart.to_html(),
        plot6 = jitsi_linear.to_html(),
        count_of_stories = count_of_stories,
        count_tasks = count_tasks,
        plot1 = taiga_linear.to_html(),
        tm = t.isoformat()))