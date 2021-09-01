from django.shortcuts import render
import plotly.express as px
import datetime as dt


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
    df = px.data.gapminder().query("year==2007")
    fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                         hover_name="country", size="pop",
                         projection="natural earth",title="Welt Karte")
    graph=fig.to_html()
    return render(request,'Ins/Zielgruppe.html',context={'fig':graph})