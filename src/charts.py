import plotly.graph_objects as go
from plotly.subplots import make_subplots

def activity_chart(data, detailed=False):
    df=data["activity"]
    if detailed:
        fig=make_subplots(specs=[[{"secondary_y":True}]])
        fig.add_trace(go.Scatter(x=df.date,y=df.commits,mode="lines",name="Commits",fill="tozeroy"),secondary_y=False)
        fig.add_trace(go.Scatter(x=df.date,y=df.reviews,mode="lines",name="Reviews"),secondary_y=False)
        fig.add_trace(go.Bar(x=df.date,y=df.deploys,name="Deploys",opacity=.45),secondary_y=True)
    else:
        fig=go.Figure()
        fig.add_trace(go.Bar(x=df.date,y=df.commits,name="Commits"))
        fig.add_trace(go.Scatter(x=df.date,y=df.reviews,name="Reviews",mode="lines"))
    fig.update_layout(template="plotly_dark",height=330,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",legend=dict(orientation="h",y=1.1),hovermode="x unified")
    return fig

def language_chart(data):
    labels=list(data["languages"].keys()); values=list(data["languages"].values())
    fig=go.Figure(go.Pie(labels=labels,values=values,hole=.62))
    fig.update_layout(template="plotly_dark",height=330,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor="rgba(0,0,0,0)",showlegend=True,legend=dict(orientation="h",y=-.05))
    return fig

def contribution_chart(data):
    df=data["activity"].copy()
    df["week"]=df["date"].dt.to_period("W").astype(str)
    weekly=df.groupby("week",as_index=False)["commits"].sum()
    fig=go.Figure(go.Bar(x=weekly.week,y=weekly.commits,name="Weekly commits"))
    fig.update_layout(template="plotly_dark",height=300,margin=dict(l=0,r=0,t=10,b=0),paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")
    return fig
