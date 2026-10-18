import pandas as pd

def generate_html_dashboard():
    print("Generating Interactive HTML Dashboard...")
    df = pd.read_csv("imdb_top_250_movies.csv")
    
    # Calculate stats
    total_movies = len(df)
    max_rating = df['IMDb Rating'].max()
    avg_rating = round(df['IMDb Rating'].mean(), 2)
    
    # Convert dataframe to HTML table
    table_html = df.to_html(classes='table table-striped table-hover', index=False)
    
    # HTML template with modern styling
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IMDb Top 250 Movies Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #f8f9fa; font-family: Arial, sans-serif; }}
            .header {{ background: #1f1f1f; color: white; padding: 25px; text-align: center; }}
            .card {{ box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px; }}
            .container {{ margin-top: 30px; margin-bottom: 50px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🎬 IMDb Top 250 Movies Dashboard</h1>
            <p>Mini Project Analysis & Visual Report</p>
        </div>
        
        <div class="container">
            <!-- KPI Cards -->
            <div class="row text-center mb-4">
                <div class="col-md-4">
                    <div class="card p-3 bg-primary text-white">
                        <h3>{total_movies}</h3>
                        <p class="mb-0">Total Movies Scraped</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3 bg-success text-white">
                        <h3>{max_rating}</h3>
                        <p class="mb-0">Highest IMDb Rating</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3 bg-warning text-dark">
                        <h3>{avg_rating}</h3>
                        <p class="mb-0">Average Rating</p>
                    </div>
                </div>
            </div>
            
            <!-- Data Table Section -->
            <div class="card p-4">
                <h3 class="mb-3">📋 Complete Movies Dataset</h3>
                <div class="table-responsive" style="max-height: 500px; overflow-y: scroll;">
                    {table_html}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save as HTML file
    with open("imdb_dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Success! HTML Dashboard generated as 'imdb_dashboard.html'.")

if __name__ == "__main__":
    generate_html_dashboard()