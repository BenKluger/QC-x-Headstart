from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'November 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'November 15, 2022'
    }
]

grants_data = [
    {
        'name': 'STEM Scholarship',
        'organization': 'UNCF',
        'amount': 5000,
        'due_date': '2022-12-29',
        'description': 'One of the public schools with a few merit scholarships is the University of Vermont...',
    },
    {
        'name': 'Special Excellence Award',
        'organization': 'CIRI',
        'amount': 7590,
        'due_date': '2023-03-15',
        'description': 'One of the public schools with a few merit scholarships is the University of Vermont...',
    },
    {
        'name': 'Coca Cola Scholarship Program',
        'organization': 'Coca Cola',
        'amount': 12000,
        'due_date': '2022-11-05',
        'description': 'One of the public schools with a few merit scholarships is the University of Vermont...',
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/grants")
def grants():
    return render_template('grants_list.html', grants=grants_data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/upload")
def upload_grant():
    return render_template('upload_grant.html')


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
