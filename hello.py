import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd

# Initialize the Dash app with Bootstrap theme for layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample account numbers list
account_numbers = ["Chris Krüger", "John Doe", "Alice Smith"]

# Sample data for the transactions table
data = {
    "Date": ["2023-09-01", "2023-09-02", "2023-09-03"],
    "Description": ["Transaction 1", "Transaction 2", "Transaction 3"],
    "Amount": [100, -50, 200]
}
df = pd.DataFrame(data)

# Layout
app.layout = dbc.Container([
    dbc.Row([
        # Left Card (1/3 screen) for selecting account, date, file type, etc.
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4("Download Statement", className="card-title text-center", style={"font-weight": "bold", "font-size": "24px", "color": "#000"}),

                    # Account Selection
                    dbc.Label("Select Account", className="mt-2", style={"font-size": "16px", "color": "#000"}),
                    dcc.Dropdown(
                        id="account-dropdown",
                        options=[{"label": acct, "value": acct} for acct in account_numbers],
                        value=account_numbers[0],
                        className="mb-3",
                        style={"font-size": "14px"}
                    ),

                    # Date Selection with min-width to avoid clipping
                    dbc.Label("Start Date", style={"font-size": "16px", "color": "#000"}),
                    dcc.DatePickerSingle(
                        id='start-date-picker',
                        placeholder='Start date',
                        className="mb-3",
                        style={
                            "width": "50%",
                            "min-width": "300px",  # Min width to ensure proper sizing
                            "font-size": "12px",
                            "padding": "10px",
                            "border-radius": "5px",
                            "border": "1px solid #ccc",
                            "box-sizing": "border-box"
                        }
                    ),
                    dbc.Label("End Date", style={"font-size": "16px", "color": "#000"}),
                    dcc.DatePickerSingle(
                        id='end-date-picker',
                        placeholder='End date',
                        className="mb-3",
                        style={
                            "width": "50%",
                            "min-width": "300px",  # Min width for end date to match
                            "font-size": "12px",
                            "padding": "10px",
                            "border-radius": "5px",
                            "border": "1px solid #ccc",
                            "box-sizing": "border-box"
                        }
                    ),

                    # File Type Selection
                    dbc.Label("File Type", style={"font-size": "16px", "color": "#000"}),
                    dbc.RadioItems(
                        id="file-type-radio",
                        options=[
                            {"label": "PDF", "value": "PDF"},
                            {"label": "Excel", "value": "Excel"}
                        ],
                        value="PDF",
                        inline=True,
                        className="mb-3",
                        style={"font-size": "14px"}
                    ),

                    # Download Button
                    dbc.Button("Download", id="download-btn", color="dark", className="w-100 mt-3",
                               style={"font-size": "16px", "padding": "10px", "box-shadow": "0 4px 6px rgba(0,0,0,0.1)", "border-radius": "5px"}),
                ])
            ], style={"width": "100%", "border-radius": "10px", "padding": "15px", "border": "1px solid #000", "min-width": "300px"}),
            width=4  # Left side takes 1/3rd of the screen
        ),

        # Right Card (2/3 screen) for displaying transactions table
        dbc.Col(
            dbc.Card([
                dbc.CardBody([
                    html.H4("Transactions", className="card-title text-center", style={"font-weight": "bold", "font-size": "24px", "color": "#000"}),

                    # Dash DataTable for Transactions with cleaner styling
                    dash_table.DataTable(
                        id='transaction-table',
                        columns=[{"name": i, "id": i} for i in df.columns],
                        data=df.to_dict('records'),
                        style_as_list_view=True,
                        style_header={
                            'backgroundColor': 'black',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'textAlign': 'left',
                            'padding': '10px',
                            'border': '1px solid #ddd',
                            'font_size': '14px',
                            'color': '#000',
                        },
                        style_table={'width': '100%', 'border': 'none'}
                    )
                ])
            ], style={"width": "100%", "border-radius": "10px", "padding": "15px", "border": "1px solid #000"}),
            width=8  # Right side takes 2/3rd of the screen
        ),
    ], className="mt-4")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
