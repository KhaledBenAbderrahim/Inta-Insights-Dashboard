from django.shortcuts import render
import plotly.express as px
import datetime as dt
import pandas as pd
import plotly.graph_objects as go




# Create your views here.


def dashboard(request):
    current_datetime = dt.datetime.now()
    string_date = current_datetime.strftime("%A,%B,%d,%Y")
    content={
        'date':string_date
    }
    return render(request,'Ins/dashboard.html',content)

def erreichte_Konten(request):
    df = px.data.tips()

    #Graph-1 -----------------------------------------------------------------------------------------------------
    fig = px.pie(df, values='tip', names='day', color='day',
                 color_discrete_map={'Thur': 'lightcyan',
                                     'Fri': 'cyan',
                                     'Sat': 'royalblue',
                                     'Sun': 'darkblue'})

    #Graph-1 ------------------------------------------------------------------------------------------------------
    data = dict(
        number=[39, 27.4, 20.6, 11, 2],
        stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
    fig_1 = px.funnel(data, x='number', y='stage')

    #Graph-2 ------------------------------------------------------------------------------------------------------
    df2 = px.data.tips()

    fig_2 = px.density_contour(df2, x="total_bill", y="tip")
    fig_2.update_traces(contours_coloring="fill", contours_showlabels=True)



    graph=fig.to_html(full_html=False)
    graph_2= fig_1.to_html(full_html=False)
    graph_3= fig_2.to_html(full_html=False)
    return render(request,'Ins/Erreichte_Konten.html', context={'plot_div': graph,
                                                                'plot_div2':graph_2,
                                                                'plot_div3':graph_3})

def content_Interaktionen(request):
    return render(request ,'Ins/Content-Interaktionen.html')

def zielGruppe(request):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
    df.head()

    df['text'] = df['name'] + '<br>Population ' + (df['pop'] / 1e6).astype(str) + ' million'
    limits = [(0, 2), (3, 10), (11, 20), (21, 50), (50, 3000)]
    colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]
    cities = []
    scale = 5000

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=df_sub['lon'],
            lat=df_sub['lat'],
            text=df_sub['text'],
            marker=dict(
                size=df_sub['pop'] / scale,
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            ),
            name='{0} - {1}'.format(lim[0], lim[1])))

    fig.update_layout(
        title_text='MAP EXAMPLE<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        )
    )
    graph=fig.to_html()
    return render(request,'Ins/Zielgruppe.html',context={'fig':graph})