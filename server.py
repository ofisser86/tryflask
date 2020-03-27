import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    # return 'My blogpost!'
    return  render_template('blog.html',)


@app.route('/<slug>')
def works(slug):
    print(request.view_args)
    return render_template(f'{slug}', slug=slug)


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', newline='', mode='a') as csv_database:
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(csv_database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                   fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerow({'email': email, 'subject': subject, 'message': message})


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as database:
        file = database.write(f'\n {email}, {subject}, {message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        # print(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Some error occur"


# @app.route('/works')
# def works():
#     return render_template('works.html')

# @app.route('/work')
# def work():
#     return render_template('work.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/components')
# def components():
#     return render_template('components.html')


if __name__ == '__main__':
    # in olser version use debug=true for debug mode on
    app.run()
