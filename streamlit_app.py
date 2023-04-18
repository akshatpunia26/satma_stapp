import streamlit as st
st.set_page_config(page_title="Indian Geospatial Analysis",layout="wide")
from streamlit_option_menu import option_menu
from apps import home, heatmap, intmap, splitmap, basemaps, marketcluster, upload  # import your app modules here


# https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": intmap.app, "title": "Interactive Map", "icon": "globe"},
    {"func": splitmap.app, "title": "Split Map", "icon": "window-split"},
    {"func": marketcluster.app, "title": "Market Cluster", "icon": "pin-map"},
    {"func": basemaps.app, "title": "Base Maps", "icon": "atlas"},
    {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """test """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
