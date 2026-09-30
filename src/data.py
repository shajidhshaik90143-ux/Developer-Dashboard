import pandas as pd
import random

def load_data():
    random.seed(42)
    activity = []
    for i in range(84):
        activity.append({
            "date": pd.Timestamp.today().normalize() - pd.Timedelta(days=83-i),
            "commits": random.randint(0, 14),
            "reviews": random.randint(0, 8),
            "deploys": random.choice([0,0,0,1,1])
        })
    return {
        "profile": {"name":"Alex Morgan","username":"alexmorgan-dev"},
        "stats": {"repositories":27,"commits":1248,"prs":186,"issues_closed":342},
        "activity": pd.DataFrame(activity),
        "languages": {"Python":34,"TypeScript":24,"JavaScript":18,"Kotlin":10,"SQL":8,"CSS":6},
        "projects": [
            {"name":"DevOps Control Center","description":"Infrastructure monitoring and deployment orchestration platform.","status":"Active","progress":82,"stars":128,"issues":4,"stack":["Python","FastAPI","PostgreSQL","Docker"],"updated":"2 hours ago","commits":312,"contributors":5},
            {"name":"AI Code Review Assistant","description":"LLM-powered pull request analysis with security and quality checks.","status":"Active","progress":68,"stars":94,"issues":7,"stack":["Python","FastAPI","OpenAI","Redis"],"updated":"Yesterday","commits":241,"contributors":4},
            {"name":"Mobile Finance Tracker","description":"Cross-platform personal finance application with analytics.","status":"Review","progress":91,"stars":76,"issues":2,"stack":["Kotlin","Firebase","Compose"],"updated":"2 days ago","commits":187,"contributors":3},
            {"name":"Campus Services API","description":"Unified API for student services, attendance and notifications.","status":"Active","progress":56,"stars":51,"issues":11,"stack":["Node.js","PostgreSQL","Redis"],"updated":"3 days ago","commits":154,"contributors":6},
            {"name":"Portfolio Website","description":"Modern developer portfolio with case studies and contact workflows.","status":"Complete","progress":100,"stars":38,"issues":0,"stack":["React","TypeScript","CSS"],"updated":"1 week ago","commits":93,"contributors":2},
        ],
        "events": [
            {"type":"commit","title":"Refactor authentication middleware","repo":"DevOps Control Center","detail":"8 files changed • +214 −97","time":"12 min ago"},
            {"type":"pull_request","title":"Add deployment health checks","repo":"DevOps Control Center","detail":"PR #184 • awaiting review","time":"48 min ago"},
            {"type":"issue","title":"Optimize database query for dashboard","repo":"Campus Services API","detail":"Issue #72 • high priority","time":"2 hrs ago"},
            {"type":"commit","title":"Improve mobile analytics cards","repo":"Mobile Finance Tracker","detail":"5 files changed • +88 −21","time":"5 hrs ago"},
            {"type":"pull_request","title":"Add secure prompt templates","repo":"AI Code Review Assistant","detail":"PR #63 • merged","time":"Yesterday"},
        ],
        "health": [
            {"repo":"DevOps Control Center","coverage":"94%","issues":4,"health":"Healthy"},
            {"repo":"AI Code Review Assistant","coverage":"89%","issues":7,"health":"Healthy"},
            {"repo":"Campus Services API","coverage":"76%","issues":11,"health":"Attention"},
            {"repo":"Mobile Finance Tracker","coverage":"92%","issues":2,"health":"Healthy"},
        ]
    }
