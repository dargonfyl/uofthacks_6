from flask import Flask, render_template, request, redirect, url_for
from .imagetoword import *
from .getwikipediaarticle import *
from .keysentences import *
app = Flask(__name__)


@app.route('/')
def root():
    """
    Creates the starting page

    :return: the template of index
    :rtype:  template
    """
    dummy = "Hello!"

    return render_template('index.html', dummy=dummy)


@app.route('/', methods=["POST", "GET"])
def process_url():
    """
    Takes the url in the text field

    :return: the summary page for the text field
    :rtype:  redirect
    """
    return redirect(url_for("summary", info=get_word(request.form["url"])), code=302)


@app.route("/summary/<info>")
def summary(info):
    """
    Creates the page for the summary of info

    :param info: the name of the image
    :type info:  str
    :return:     the template of the summary
    :rtype:      template
    """
    bullets = None
    image = None
    try:
        wiki_page = WikiPage(info)
        bullets = key_sentences(wiki_page.get_summary_full())
        make_bullet_points(bullets)
        image = wiki_page.get_img_url()
    except WikiPageException as e:
        print(e)

    return render_template("summary.html", name=info, bullets=bullets, image=image)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
