import streamlit as st
from src.data import load_data
from src.ui import inject_css, metric_card, section_title, status_badge
from src.charts import activity_chart, language_chart, contribution_chart

st.set_page_config(page_title="Developer Dashboard", page_icon="⌘", layout="wide", initial_sidebar_state="expanded")
inject_css()

data = load_data()

with st.sidebar:
    st.markdown("# ⌘ DevDash")
    st.caption("Developer Analytics Workspace")
    st.divider()
    page = st.radio("Navigation", ["Overview", "Projects", "Activity", "Analytics", "Settings"], label_visibility="collapsed")
    st.divider()
    st.markdown("### Workspace")
    st.success("● All systems operational")
    st.caption("Demo workspace • v1.0.0")

st.markdown(f"<div class='eyebrow'>DEVELOPER WORKSPACE</div>", unsafe_allow_html=True)
st.title(f"Good morning, {data['profile']['name']} 👋")
st.markdown("Track your engineering activity, projects, technologies, and delivery progress from one workspace.")

if page == "Overview":
    section_title("Engineering Overview", "Your current development snapshot")
    cols = st.columns(4)
    metrics = [
        ("Repositories", str(data["stats"]["repositories"]), "+3 this month"),
        ("Commits", f"{data['stats']['commits']:,}", "+18.4% vs last month"),
        ("Pull Requests", str(data["stats"]["prs"]), "+7 this month"),
        ("Issues Closed", str(data["stats"]["issues_closed"]), "91% resolution rate"),
    ]
    for col, (label, value, delta) in zip(cols, metrics):
        with col: metric_card(label, value, delta)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    left, right = st.columns([1.65, 1])
    with left:
        section_title("Coding Activity", "Last 12 weeks")
        st.plotly_chart(activity_chart(data), use_container_width=True, config={"displayModeBar": False})
    with right:
        section_title("Languages", "Code distribution")
        st.plotly_chart(language_chart(data), use_container_width=True, config={"displayModeBar": False})

    section_title("Active Projects", "Projects currently receiving development effort")
    for p in data["projects"][:4]:
        c1, c2, c3, c4 = st.columns([2.1, 1, 1, .7])
        with c1:
            st.markdown(f"**{p['name']}**")
            st.caption(p["description"])
        with c2: st.markdown(status_badge(p["status"]), unsafe_allow_html=True)
        with c3: st.progress(p["progress"]/100, text=f"{p['progress']}% complete")
        with c4: st.caption(p["updated"])

elif page == "Projects":
    section_title("Project Portfolio", "Monitor delivery across your repositories")
    search = st.text_input("Search projects", placeholder="Search by project, language, or status...")
    filtered = [p for p in data["projects"] if not search or search.lower() in str(p).lower()]
    for p in filtered:
        with st.container(border=True):
            a,b,c = st.columns([2.2,1,1])
            with a:
                st.markdown(f"### {p['name']}")
                st.write(p["description"])
                st.caption(" • ".join(p["stack"]))
            with b:
                st.markdown(status_badge(p["status"]), unsafe_allow_html=True)
                st.metric("Progress", f"{p['progress']}%")
            with c:
                st.metric("Stars", p["stars"])
                st.metric("Open issues", p["issues"])
            st.progress(p["progress"]/100)
            st.caption(f"Last updated {p['updated']} • {p['commits']} commits • {p['contributors']} contributors")

elif page == "Activity":
    section_title("Developer Activity", "Recent engineering events")
    st.plotly_chart(contribution_chart(data), use_container_width=True, config={"displayModeBar": False})
    st.markdown("### Recent Events")
    for e in data["events"]:
        c1,c2,c3 = st.columns([.15, 2.4, 1])
        with c1: st.markdown("🟢" if e["type"]=="commit" else "🟣" if e["type"]=="pull_request" else "🟠")
        with c2:
            st.markdown(f"**{e['title']}**")
            st.caption(f"{e['repo']} • {e['detail']}")
        with c3: st.caption(e["time"])

elif page == "Analytics":
    section_title("Engineering Analytics", "Delivery and quality indicators")
    a,b,c,d = st.columns(4)
    a.metric("Deployment frequency", "4.8 / week", "+12%")
    b.metric("Lead time", "7.4 hrs", "-18%")
    c.metric("Code review time", "3.1 hrs", "-9%")
    d.metric("Build success", "97.8%", "+1.4%")
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.plotly_chart(activity_chart(data, detailed=True), use_container_width=True, config={"displayModeBar": False})
    section_title("Repository Health", "Operational view")
    for r in data["health"]:
        c1,c2,c3,c4 = st.columns([2,1,1,1])
        c1.markdown(f"**{r['repo']}**")
        c2.metric("Coverage", r["coverage"])
        c3.metric("Open issues", r["issues"])
        c4.markdown(status_badge(r["health"]), unsafe_allow_html=True)

else:
    section_title("Workspace Settings", "Customize your dashboard")
    st.toggle("Show private repositories", value=True)
    st.toggle("Enable activity notifications", value=True)
    st.selectbox("Default dashboard", ["Overview", "Projects", "Activity", "Analytics"])
    st.selectbox("Theme", ["Dark", "System"])
    st.text_input("GitHub username", value=data["profile"]["username"])
    st.button("Save settings", type="primary")
    st.info("This demo stores settings locally in the session. Connect a GitHub API or database to persist production settings.")
