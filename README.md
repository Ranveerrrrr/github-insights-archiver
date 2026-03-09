# GitHub Insights Archiver


![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-GitHub%20API-181717?logo=github&logoColor=white&style=for-the-badge)

## Overview

GItHub Insights Archiver is a tool that archives GitHub repository traffic analytics and generates a local dashboard for long-term tracking.
By default, GitHub only retains 14 days of traffic data in the repository insights page. After this period, views, clones, and referrer analytics are permanently lost.
This project automates the collection and archiving of that data so developers can maintain long-term insights about their projects.

## Problem
GitHub repository insights only retain traffic data for 14 days. After that:
- Repository views are no longer available
- Repository clone data is removed
- Referrer site analytics disappear
- Popular content insights are lost

Developers therefore lose historical traffic data that could be useful for growth analysis, marketing, and project evaluation.

## Solution
GItHub Insights Archiver periodically fetches traffic data using the GitHub API and stores it locally.
The collected data can then be visualized in a local analytics dashboard, allowing long-term repository traffic analysis beyond GitHub's native 14-day limit.
## Features
- Interactive repository traffic graphs
- Views and clone tracking
- Referring site analytics
- Popular content analytics
- Multi-repository dashboard
- Local historical data storage
- GitHub-style dark user interface
- Automated data archiving

## Architecture
```
GitHub API
    |
    v
 tracker.py ---> collects traffic data
    |
    v
 traffic.json ---> stored analytics
    |
    v
 Dashboard/index.html ---> shows the data
```
## Project Structure
```
Github-Insight-Archiver/
|-- tracker.py       # Fetches GitHub traffic data
|-- traffic.json      # Stored traffic history
|-- config.json      # GitHub API token
|-- Dashboard/index.html    # Generated analytics dashboard
```

## Installation
```bash
git clone https://github.com/Ranveerrrrr/Github-Insights-Archiver.git
cd Github-Insights-Archiver
pip install -r requirements.txt
```

## Configuration
Create a GitHub Personal Access Token with the following permissions:
`repo`
`read:org`
Add the token to config.json:
```json
{
  "token": "YOUR_GITHUB_TOKEN"
}
```

## Usage
Collect repository traffic data:
```bash
python tracker.py
```
Open the dashboard:
`Dashboard/index.html`

## Dashboard Preview
<img width="1218" height="995" alt="image" src="https://github.com/user-attachments/assets/fbcbe453-e880-410b-bae7-0cf84925197c" />
<img width="1228" height="994" alt="image" src="https://github.com/user-attachments/assets/4b9e4767-eed9-4561-bee3-17b4beffb2d3" />


## Development Status
This project is currently under active development. Planned improvements include:
- Repository search and filtering
- Traffic spike detection
- GitHub-style heatmap visualization
- Cloud deployment support
- OAuth authentication
- API integration for external analytics tools

## Developer
Ranveer(Bugatsec)<br>
Website: https://bugatsec.dev<br>
GitHub: https://github.com/Ranveerrrrrr<br>

## License
MIT License
