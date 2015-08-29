__author__ = 'khatcher'



from flask import redirect, \
    url_for, \
    render_template, \
    Blueprint, \
    request

from flask.views import MethodView

from models import Location
from forms import LocationForm

blight = Blueprint('blight', __name__,
                    template_folder='templates')



@blight.route('/')
def ares_root():
    return render_template('blight/root.html')


@blight.route('/create', methods=('GET', 'POST'))
def create_location():
    form = LocationForm()
    if request.method == 'POST':
        point = [form.latitude.data,form.longitude.data]
        render_template('blight/create.html', form=form)
        newlocation = Location(url=form.url.data, point=point, title=form.title.data, address=form.address.data).save()
    return render_template('blight/create.html', form=form)



class ListView(MethodView):

    def get(self):
        locations = Location.objects.all()
        return render_template('blight/list.html', locations=locations)


class DetailView(MethodView):

    def get_context(self, slug=None):
        form_cls = model_form(Post, exclude=('created_at', 'comments'))

        if slug:
            post = Post.objects.get_or_404(slug=slug)
            if request.method == 'POST':
                form = form_cls(request.form, inital=post._data)
            else:
                form = form_cls(obj=post)
        else:
            post = Post()
            form = form_cls(request.form)

        context = {
            "post": post,
            "form": form,
            "create": slug is None
        }
        return context

    def get(self, slug):
        location = Location.objects.get_or_404(slug=slug)
        return render_template('blight/detail.html', location=location)


    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)
            post.save()

            return redirect(url_for('admin.index'))
        return render_template('admin/detail.html', **context)




# Register the urls
blight.add_url_rule('/list', view_func=ListView.as_view('list'))
blight.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))