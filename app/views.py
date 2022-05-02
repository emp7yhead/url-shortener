"""Routes logic."""
from app import db
from app.models import Url
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from hashids import Hashids

url_shortener = Blueprint(
    'url_shortener',
    __name__,
    template_folder='templates',
)

hashids = Hashids(min_length=4, salt=current_app.secret_key)


@url_shortener.route('/', methods=('GET', 'POST'))
def index():  # noqa: WPS210
    """Render index page.

    Returns:
        str.
    """
    if request.method == 'POST':
        url = request.form['url']

        if Url.query.filter(Url.original_url == url).scalar():

            url_data = Url.query.filter(
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
        return redirect(url_for('url_shortener.index'))

    return render_template('index.html', page=1)


@url_shortener.route('/<url_id>')
def url_redirect(url_id: int):
    """Redirect to url.

    Args:
        url_id: shorten url id.

    Returns:
        Response.
    """
    original_id = hashids.decode(url_id)

    if original_id:
        original_id = original_id[0]
        url_data = Url.query.filter(
            Url.id == original_id,
        ).one()

        original_url = url_data.original_url
        url_data.clicks_counter = Url.clicks_counter + 1

        db.session.commit()
        db.session.close()
        return redirect(original_url)
    flash('Invalid URL')
    return redirect(url_for('url_shortener.index'))


@url_shortener.route('/stats/page/<int:page>', methods=['GET'])
def stats(page: int = 1):
    """Render statictic page with pagination.

    Args:
        page: first page.

    Returns:
        str.
    """
    per_page = 5
    urls = Url.query.order_by(Url.id).paginate(page, per_page, error_out=False)
    db.session.close()

    short_urls = {}
    for url in urls.items:

        short_url = request.host_url + hashids.encode(url.id)
        short_urls[url.id] = short_url

    return render_template('stats.html', url=urls, short_urls=short_urls)


@url_shortener.route('/about')
def about():
    """Render about page.

    Returns:
        str.
    """
    return render_template('about.html')
