# Developer Dashboard

A portfolio-ready developer analytics dashboard built with **Python + Streamlit + Plotly**.

## Features

- Developer overview with engineering KPIs
- Repository/project portfolio
- Project progress and health tracking
- Commit, code review and deployment analytics
- Programming language distribution
- Recent developer activity feed
- Repository quality/coverage indicators
- Searchable projects
- Settings workspace
- Responsive dark developer-focused UI
- Demo data included — no API key required

## Run

### Windows PowerShell

```powershell
cd "Developer Dashboard"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

Open: http://localhost:8501

## Project Structure

```text
Developer Dashboard/
├── app.py
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── data.py
    ├── ui.py
    └── charts.py
```

## Production Upgrade Ideas

- Connect GitHub REST/GraphQL API
- Add OAuth login
- Store data in PostgreSQL
- Add Docker deployment
- Add team/workspace support
- Add real CI/CD metrics
- Add GitHub Actions integration
- Add export to CSV/PDF
- Add role-based access control
