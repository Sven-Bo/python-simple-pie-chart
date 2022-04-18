import pandas as pd
import plotly.express as px


# Read data from excel
df = pd.read_excel("data.xlsx")
values = df["Results"]
names = df["Category"]

fig = px.pie(df, values=values, names=names, title="Survey Results")

fig.update_traces(textposition="inside", textinfo="percent+label")

fig.update_layout(
    title_font_size=42,
)

# Export Piechart to HTML
fig.write_html("Piechart.html")
