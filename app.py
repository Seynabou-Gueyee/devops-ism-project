from flask import Flask, render_template_string

app = Flask(__name__)

# Design professionnel avec appel à l'action
html_site = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { display: flex; flex-direction: column; min-height: 100vh; }
        .hero { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1550547660-d9450f859349?w=1200'); background-size: cover; color: white; padding: 100px 0; text-align: center; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">🍔 BURGER KINGDOM</a>
        </div>
    </nav>

    <header class="hero">
        <div class="container">
            <h1>Le meilleur burger de Dakar</h1>
            <p class="lead">Livraison rapide, goût authentique.</p>
            <a href="#menu" class="btn btn-danger btn-lg mt-3">Voir la carte</a>
        </div>
    </header>

    <main class="container my-5" id="menu">
        <h2 class="text-center mb-5">Nos Incontournables</h2>
        <div class="row">
            <div class="col-md-4">
                <div class="card h-100 shadow border-0">
                    <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600" class="card-img-top">
                    <div class="card-body text-center">
                        <h5>Royal Cheese</h5>
                        <p class="text-muted">Boeuf, cheddar fondant, sauce secrète.</p>
                        <h4 class="text-danger">8.50 €</h4>
                        <button class="btn btn-outline-danger w-100">Commander</button>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card h-100 shadow border-0">
                    <img src="https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=600" class="card-img-top">
                    <div class="card-body text-center">
                        <h5>Chicken Spicy</h5>
                        <p class="text-muted">Poulet croustillant, piment, salade.</p>
                        <h4 class="text-danger">9.00 €</h4>
                        <button class="btn btn-outline-danger w-100">Commander</button>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card h-100 shadow border-0">
                    <img src="https://images.unsplash.com/photo-1550547660-d9450f859349?w=600" class="card-img-top">
                    <div class="card-body text-center">
                        <h5>Veggie Deluxe</h5>
                        <p class="text-muted">Steak végétal, avocat, oignons confits.</p>
                        <h4 class="text-danger">7.50 €</h4>
                        <button class="btn btn-outline-danger w-100">Commander</button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-dark text-white text-center py-4 mt-auto">
        <p>&copy; 2026 Burger Kingdom | Commandez au 77 123 45 67</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_site)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
