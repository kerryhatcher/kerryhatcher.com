__author__ = 'kwhatcher'
from flask import Blueprint
from flask import render_template
from flask import request

from forms import NewPostForm
from models import Post

blog = Blueprint('blog', __name__,
                    template_folder='templates')


@blog.route('/')
def blog_home():
    posts = Post.objects.all_fields()
    return render_template('blogbase.html', posts=posts)


@blog.route('/<id>')
def post_by_id(id):
    for post in Post.objects(url=id):
        return render_template('blogpost.html', post=post)



@blog.route('/create', methods=('GET', 'POST'))
def create_post():
    form = NewPostForm()
    if request.method == 'POST':
        render_template('blogcreate.html', form=form)
        newpost = Post(url=form.URI.data, Content=form.Content.data, Title=form.Title.data).save()
    return render_template('blogcreate.html', form=form)