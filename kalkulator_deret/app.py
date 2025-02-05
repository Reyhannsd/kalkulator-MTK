from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk menghitung deret aritmatika
def deret_aritmatika(a, b, n):
    suku_n = a + (n - 1) * b
    jumlah_n = (n / 2) * (2 * a + (n - 1) * b)
    return suku_n, jumlah_n

# Fungsi untuk menghitung deret geometri
def deret_geometri(a, r, n):
    suku_n = a * (r ** (n - 1))
    if r != 1:
        jumlah_n = a * (1 - r ** n) / (1 - r)
    else:
        jumlah_n = a * n
    return suku_n, jumlah_n

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        deret_type = request.form["deret_type"]
        a = float(request.form["a"])
        n = int(request.form["n"])

        if deret_type == "aritmatika":
            b = float(request.form["b"])
            suku_n, jumlah_n = deret_aritmatika(a, b, n)
            return render_template("index.html", suku_n=suku_n, jumlah_n=jumlah_n, deret_type=deret_type)
        
        elif deret_type == "geometri":
            r = float(request.form["r"])
            suku_n, jumlah_n = deret_geometri(a, r, n)
            return render_template("index.html", suku_n=suku_n, jumlah_n=jumlah_n, deret_type=deret_type)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
