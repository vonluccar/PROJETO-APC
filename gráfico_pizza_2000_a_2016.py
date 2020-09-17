import plotly.graph_objects as go

ano_entre_2000_a_2016 = int(input('Digite o ano da olimpíada entre 2000 a 2016: '))

if ano_entre_2000_a_2016 == 2000:
    labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
    values = [12, 14, 97, 5, 34, 13, 18, 59, 58, 28, 56, 7, 88, 29, 4, 38]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()

else:
    if ano_entre_2000_a_2016 == 2004:
        labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
        values = [10, 12, 101, 6, 32, 16, 37, 63, 50, 30, 49, 7, 90, 23, 6, 33]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.show()

    else:
        if ano_entre_2000_a_2016 == 2008:
            labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
            values = [17, 20, 11, 1, 27, 43, 25, 100, 46, 51, 41, 16, 60, 30, 6]

            fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
            fig.show()

        else:
            if ano_entre_2000_a_2016 == 2012:
                labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
                values = [17, 18, 104, 6, 28, 35, 38, 91, 35, 65, 44, 13, 68, 15, 4]

                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                fig.show()

            else: 
                if ano_entre_2000_a_2016 == 2016:
                    labels = ['Brasil','Canada','USA','Áfica do Sul','Itália','Grécia','Japão','China','Austrália','Inglaterra','Alemanha','Quênia','Rússia','Cuba','Argentina','França']
                    values = [19, 22, 121, 10, 28, 11, 41, 70, 29, 41, 42, 13, 56, 11, 4, 42]

                    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                    fig.show()
                else:
                    print('Não há o ano recomendado')