import json

repos = json.load(open("traffic.json"))

repos_json = json.dumps(repos)

html = """
<!DOCTYPE html>
<html>

<head>

<title>GitHub Repo Analytics</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>

*{
box-sizing:border-box;
}

body{
margin:0;
background:#0d1117;
color:#c9d1d9;
font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial;
display:flex;
height:100vh;
}

.sidebar{
width:260px;
background:#161b22;
border-right:1px solid #30363d;
display:flex;
flex-direction:column;
}

.logo{
display:flex;
align-items:center;
gap:10px;
padding:16px;
font-weight:600;
border-bottom:1px solid #30363d;
}

.repo-list{
overflow-y:auto;
flex:1;
}

.repo-item{
padding:12px 16px;
cursor:pointer;
border-bottom:1px solid #30363d;
font-size:14px;
}

.repo-item:hover{
background:#21262d;
}

.main{
flex:1;
padding:40px;
overflow-y:auto;
}

.repo-title{
font-size:28px;
font-weight:600;
margin-bottom:6px;
}

.repo-desc{
color:#8b949e;
margin-bottom:16px;
max-width:900px;
}

.repo-meta{
color:#8b949e;
margin-bottom:16px;
}

.repo-link{
margin-bottom:20px;
display:block;
color:#c9d1d9;
text-decoration:none;
}

.repo-link:hover{
text-decoration:underline;
}

.stats{
display:flex;
gap:20px;
margin-bottom:30px;
}

.stat-box{
background:#161b22;
border:1px solid #30363d;
border-radius:6px;
padding:16px;
width:160px;
}

.stat-title{
font-size:12px;
color:#8b949e;
margin-bottom:4px;
}

.stat-value{
font-size:22px;
font-weight:600;
}

canvas{
max-width:900px;
}

</style>

</head>

<body>

<div class="sidebar">

<div class="logo">

<svg height="20" viewBox="0 0 16 16" fill="white">
<path d="M8 0C3.58 0 0 3.58 0 8a8 8 0 005.47 7.59c.4.07.55-.17.55-.38
0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94
-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52
-.01-.53.63-.01 1.08.58 1.23.82
.72 1.21 1.87.87 2.33.66
.07-.52.28-.87.51-1.07
-1.78-.2-3.64-.89-3.64-3.95
0-.87.31-1.59.82-2.15
-.08-.2-.36-1.02.08-2.12
0 0 .67-.21 2.2.82
A7.7 7.7 0 018 4.69
c.68 0 1.36.09 2 .26
1.53-1.04 2.2-.82 2.2-.82
.44 1.1.16 1.92.08 2.12
.51.56.82 1.27.82 2.15
0 3.07-1.87 3.75-3.65 3.95
.29.25.54.73.54 1.48
0 1.07-.01 1.93-.01 2.2
0 .21.15.46.55.38
A8 8 0 0016 8
c0-4.42-3.58-8-8-8z"/>
</svg>

Repositories

</div>

<div id="repoList" class="repo-list"></div>

</div>

<div class="main">

<div id="repoInfo"></div>

<div class="stats">

<div class="stat-box">
<div class="stat-title">Total Views</div>
<div id="totalViews" class="stat-value">0</div>
</div>

<div class="stat-box">
<div class="stat-title">Total Clones</div>
<div id="totalClones" class="stat-value">0</div>
</div>

</div>

<canvas id="chart" height="120"></canvas>

</div>
<script>

const repos = REPO_DATA;

const repoList = document.getElementById("repoList");
const repoInfo = document.getElementById("repoInfo");

let chart = null;

repos.forEach((repo,index)=>{

const item = document.createElement("div");
item.className = "repo-item";
item.innerText = repo.name;

item.onclick = () => loadRepo(index);

repoList.appendChild(item);

});

function loadRepo(index){

const repo = repos[index];

repoInfo.innerHTML = `
<div class="repo-title">${repo.name}</div>
<div class="repo-desc">${repo.description || "No description"}</div>
<div class="repo-meta">⭐ ${repo.stars} | 🍴 ${repo.forks}</div>
<a class="repo-link" href="${repo.url}" target="_blank">${repo.url}</a>
`;

const labels = repo.views.map(v => v.timestamp.substring(0,10));
const views = repo.views.map(v => v.count);
const clones = repo.clones.map(v => v.count);

const totalViews = views.reduce((a,b)=>a+b,0);
const totalClones = clones.reduce((a,b)=>a+b,0);

document.getElementById("totalViews").innerText = totalViews;
document.getElementById("totalClones").innerText = totalClones;

if(chart) chart.destroy();

chart = new Chart(document.getElementById("chart"),{

type:"line",

data:{
labels:labels,
datasets:[
{
label:"Views",
data:views,
borderColor:"#58a6ff",
tension:0.3
},
{
label:"Clones",
data:clones,
borderColor:"#3fb950",
tension:0.3
}
]
},

options:{
interaction:{mode:"index",intersect:false},
plugins:{tooltip:{enabled:true}},
scales:{y:{beginAtZero:true}}
}

});

}

loadRepo(0);

</script>

</body>
</html>
"""

html = html.replace("REPO_DATA", repos_json)

open("dashboard.html","w",encoding="utf8").write(html)

print("dashboard.html created")