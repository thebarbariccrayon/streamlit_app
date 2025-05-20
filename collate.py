from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import streamlit as st

st.set_page_config(page_title="HPC Research Node Performance Dashboard", page_icon="🗃")

@st.cache_data

def fetch_data(samples):
    data = pd.read_json('http://127.0.0.1:5000/data',
                        precise_float=True
                        ) #, dtype={'auth_time': float})
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')
    pd.set_option('display.float_format' ,lambda x: '{:,.3f}' % x)
    #data = data.astype({'auth_time':'float64'}).dtypes
    return pd.DataFrame(data)

@st.cache_data
def fetch_host_data(samples):
    data = pd.read_json('http://127.0.0.1:5000/data',
                    precise_float=True
                    )
    return pd.DataFrame(data)

st.sidebar.subheader("Drill down options")
st.sidebar.markdown("Under construction")
st.header("HPC Research Analysis Aggregated Data")
st.markdown(
    """
    This is a prototype of the HPC Research Node Performance Dashboard.
    The data collected here is for the overall performance analysis of targeted public
    facing login nodes that have been integrated with the HPC Research Identitfy Management
    System.
"""
)
tab_labels = ["Data"] + fetch_data(samples=10)['host'].unique().tolist()
tabs = st.tabs(tab_labels)
with tabs[0]:
    data = fetch_data(samples=10)
    st.markdown("### Averages")
    mean_data = pd.DataFrame(
        {
            "login response" : [data['login_reponse'].mean()],
            "auth": [data['auth'].mean()],
            "command execution" : [data['command_exe'].mean()],
            "total time" : [data['total'].mean()],
        }
    )
    st.dataframe(mean_data, use_container_width=True, hide_index=True)
    st.markdown("### Standard Deviation")
    std_data = pd.DataFrame(
        {
            "login response" : [data['login_reponse'].std()],
            "auth": [data['auth'].std()],
            "command execution" : [data['command_exe'].std()],
            "total time" : [data['total'].std()],
        }
    )
    st.dataframe(std_data, use_container_width=True, hide_index=True)
    st.markdown("### Data Table")
    st.dataframe(data, use_container_width=True)
    chart_data = pd.DataFrame(
        {
            "login response" : data['login_reponse'],
            "auth": data['auth'],
            "command execution" : data['command_exe'],
            "total time" : data['total'],
        }
    )
    st.markdown("### Overall Performance")
    st.line_chart(chart_data, use_container_width=True)

with tabs[1]:
    st.markdown("### Performance sorted by command")
    source_data = data[data['host'].isin([tab_labels[1]])]
    command_label = fetch_data(samples=10)['command'].unique().tolist()
    command_tabs = st.tabs(command_label)

    with command_tabs[0]:
        command_data = source_data[source_data['command'].isin([command_label[0]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data,use_container_width=True)

    with command_tabs[1]:
        command_data = source_data[source_data['command'].isin([command_label[1]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[2]:
        command_data = source_data[source_data['command'].isin([command_label[2]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[3]:
        command_data = source_data[source_data['command'].isin([command_label[3]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[4]:
        command_data = source_data[source_data['command'].isin([command_label[4]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[5]:
        command_data = source_data[source_data['command'].isin([command_label[5]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

with tabs[2]:
    st.markdown("### Performance sorted by command")
    source_data = data[data['host'].isin([tab_labels[2]])]
    command_label = fetch_data(samples=10)['command'].unique().tolist()
    command_tabs = st.tabs(command_label)
    with command_tabs[0]:
        command_data = source_data[source_data['command'].isin([command_label[0]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[1]:
        command_data = source_data[source_data['command'].isin([command_label[1]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[2]:
        command_data = source_data[source_data['command'].isin([command_label[2]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[3]:
        command_data = source_data[source_data['command'].isin([command_label[3]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[4]:
        command_data = source_data[source_data['command'].isin([command_label[4]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[5]:
        command_data = source_data[source_data['command'].isin([command_label[5]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

with tabs[3]:
    st.markdown("### Performance sorted by command")
    source_data = data[data['host'].isin([tab_labels[3]])]
    command_label = fetch_data(samples=10)['command'].unique().tolist()
    command_tabs = st.tabs(command_label)
    with command_tabs[0]:
        command_data = source_data[source_data['command'].isin([command_label[0]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)


    with command_tabs[1]:
        command_data = source_data[source_data['command'].isin([command_label[1]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)


    with command_tabs[2]:
        command_data = source_data[source_data['command'].isin([command_label[2]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[3]:
        command_data = source_data[source_data['command'].isin([command_label[3]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[4]:
        command_data = source_data[source_data['command'].isin([command_label[4]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[5]:
        command_data = source_data[source_data['command'].isin([command_label[5]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

with tabs[4]:
    st.markdown("### Performance sorted by command")
    source_data = data[data['host'].isin([tab_labels[4]])]
    command_label = fetch_data(samples=10)['command'].unique().tolist()
    command_tabs = st.tabs(command_label)
    with command_tabs[0]:
        command_data = source_data[source_data['command'].isin([command_label[0]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[1]:
        command_data = source_data[source_data['command'].isin([command_label[1]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[2]:
        command_data = source_data[source_data['command'].isin([command_label[2]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[3]:
        command_data = source_data[source_data['command'].isin([command_label[3]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[4]:
        command_data = source_data[source_data['command'].isin([command_label[4]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)

    with command_tabs[5]:
        command_data = source_data[source_data['command'].isin([command_label[5]])]
        st.markdown("### Averages")
        mean_data = pd.DataFrame(
            {
                "login response" : [command_data['login_reponse'].mean()],
                "auth": [command_data['auth'].mean()],
                "command execution" : [command_data['command_exe'].mean()],
                "total time" : [command_data['total'].mean()],
            }
        )
        st.dataframe(mean_data, use_container_width=True, hide_index=True)
        chart_data = pd.DataFrame(
            {
                "login response" : command_data['login_reponse'],
                "auth": command_data['auth'],
                "command execution" : command_data['command_exe'],
                "total time" : command_data['total'],
            }
        )
        st.line_chart(chart_data, use_container_width=True)
