import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown="""
Naglowki

# H1
## H2
### H3

Znaczniki tekstu:

Kursywa: *tekst kursywa* lub _tekst kursywa_  
Pogrubienie: **Teekst pogrubiony** lub __tekst pogrubiony__  
Pogrubienie i kursywa: **pogrubienie i _kursywa_**  
Przekreslenie: ~~przekreslony tekst~~  

Listy:  
Lista uporzadkowana:  
1. Python  
2. Sql  
3. Java  

Lista unordered:  
* Python  
* Java  
* Sql

Linkowanie:  
[Google.com](http://www.google.com)

Kod:  
Uzyj `print('Hello')`

Blok kodu:  
```
import numpy as np
x = np.random.randn(100)
print(x)
```

Tabele:  

|UserID   |Rating  |Age|
|---------|--------|---|
|001      |4.5     |24 |

Cytowanie:  

> Python jest w pyte

Linie horyzontalne:  

---
"""

app.layout = html.Div([

    dcc.Markdown(markdown)

])

if __name__ == '__main__':
    app.run_server(debug=True)
