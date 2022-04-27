"""Routes logic."""
from flask import flash, redirect, render_template, request, url_for

from app.main import app, db, hashids
from app.models import Url


@app.route('/', methods=('GET', 'POST'))
def index():  # noqa: WPS210
    """Render index page.

    Returns:
        str.
    """
    if request.method == 'POST':
        url = request.form['url']

        if db.session.query(Url).filter(Url.original_url == url).scalar():

            url_data = db.session.query(Url).filter(
                Url.original_url == url,
            ).one()
            short_url = request.host_url + hashids.encode(url_data.id)
            return render_template('index.html', short_url=short_url)

        if url:
            url_data = Url(original_url=url)

            db.session.add(url_data)
            db.session.commit()

            url_id = url_data.id
            hashid = hashids.encode(url_id)
            short_url = request.host_url + hashid

            return render_template('index.html', short_url=short_url)

        flash('The URL is required!')
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/<url_id>')
def url_redirect(url_id):
    """Redirect to url.

    Args:
        url_id: shorten url id.

    Returns:
        Response.
    """
    original_id = hashids.decode(url_id)

    if original_id:
        original_id = original_id[0]
        url_data = db.session.query(Url).filter(
            Url.id == original_id,
            ).one()

        original_url = url_data.original_url
        url_data.clicks_counter = Url.clicks_counter + 1

        db.session.commit()
        db.session.close()
        return redirect(original_url)
    flash('Invalid URL')
    return redirect(url_for('index'))


@app.route('/stats')
def stats():
    """Render statictic page.

    Returns:
        str.
    """
    db_urls = db.session.query(Url).all()
    db.session.close()

    urls = []
    for url in db_urls:
        url_dict = {
            'id': url.id,
            'created': url.created,
            'original_url': url.original_url,
            'clicks': url.clicks_counter,
        }
        url_dict['short_url'] = request.host_url + hashids.encode(url.id)
        urls.append(url_dict)

    return render_template('stats.html', urls=urls)


@app.route('/about')
def about():
    """Render about page.

    Returns:
        str.
    """
    return render_template('about.html')
