from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
    database="FILL YOUR OWN",
    user="FILL YOUR OWN",
    password="FILL YOUR OWN",
    host="FILL YOUR OWN",
    port="FILL YOUR OWN",
)

# create a cursor
cur = conn.cursor()


@app.route("/")
def index():
    # Data
    data = {}

    # Connect to the database
    conn = psycopg2.connect(
        database="FILL YOUR OWN",
        user="FILL YOUR OWN",
        password="FILL YOUR OWN",
        host="FILL YOUR OWN",
        port="FILL YOUR OWN",
    )

    # create a cursor
    cur = conn.cursor()

    # Select all products from the table
    cur.execute(
        """
            SELECT c.cust_id, c.full_name, c.physical_address, m.title, s.salutation
            FROM customers c 
            JOIN movie_rented_by mrb ON (c.cust_id = mrb.cust_id)
            JOIN movies m ON (mrb.movie_id=m.movie_id)
            JOIN salutations s ON (c.salutation_id=s.salutation_id);
        """
    )

    # Fetch the data
    data["general"] = cur.fetchall()

    # Select all customers from the table
    cur.execute(
        """
            SELECT c.*, s.*
            FROM customers c
            JOIN salutations s ON (s.salutation_id=c.salutation_id);
        """
    )

    # Fetch the data
    data["customers"] = cur.fetchall()

    # Select all movies from the table
    cur.execute(
        """
            SELECT *
            FROM movies m;
        """
    )

    # Fetch the data
    data["movies"] = cur.fetchall()

    # Select all salutations from the table
    cur.execute(
        """
            SELECT *
            FROM salutations s
            ORDER BY salutation_id DESC;
        """
    )

    # Fetch the data
    data["salutations"] = cur.fetchall()

    # close the cursor and connection
    cur.close()
    conn.close()

    return render_template("index.html", data=data)


@app.route("/create_new_customer", methods=["POST"])
def createNewCustomer():
    conn = psycopg2.connect(
        database="FILL YOUR OWN",
        user="FILL YOUR OWN",
        password="FILL YOUR OWN",
        host="FILL YOUR OWN",
        port="FILL YOUR OWN",
    )

    cur = conn.cursor()

    # Get the data from the form
    full_name = f"{request.form['first_name']} {request.form['last_name']}"
    physical_address = request.form["physical_address"]
    salutation = request.form["salutation"]

    # Insert the data into the table
    cur.execute(
        f"""
            INSERT INTO customers (full_name, physical_address, salutation_id)
            VALUES
                ('{full_name}', '{physical_address}', {salutation})
        """
    )

    # commit the changes
    conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()

    return redirect(url_for("index"))


@app.route("/rent", methods=["POST"])
def rent():
    conn = psycopg2.connect(
        database="FILL YOUR OWN",
        user="FILL YOUR OWN",
        password="FILL YOUR OWN",
        host="FILL YOUR OWN",
        port="FILL YOUR OWN",
    )

    cur = conn.cursor()

    # Get the data from the form
    cust_id = request.form["cust_id"]
    movie_id = request.form["movie_id"]

    # Insert the data into the table
    cur.execute(
        f"""
            INSERT INTO movie_rented_by (cust_id, movie_id)
            VALUES
                ({cust_id},{movie_id})
        """
    )

    # commit the changes
    conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()

    return redirect(url_for("index"))


@app.route("/add_new_movie", methods=["POST"])
def add_new_movie():
    conn = psycopg2.connect(
        database="FILL YOUR OWN",
        user="FILL YOUR OWN",
        password="FILL YOUR OWN",
        host="FILL YOUR OWN",
        port="FILL YOUR OWN",
    )

    cur = conn.cursor()

    # Get the data from the form
    title = request.form["title"]

    # Update the data in the table
    cur.execute(
        f"""
            INSERT INTO movies (title)
            VALUES
                ('{title}');
        """
    )

    # commit the changes
    conn.commit()
    return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete():
    conn = psycopg2.connect(
        database="FILL YOUR OWN",
        user="FILL YOUR OWN",
        password="FILL YOUR OWN",
        host="FILL YOUR OWN",
        port="FILL YOUR OWN",
    )
    cur = conn.cursor()

    # Get the data from the form
    id = request.form["id"]

    # Delete the data from the table
    cur.execute("""DELETE FROM products WHERE id=%s""", (id,))

    # commit the changes
    conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
