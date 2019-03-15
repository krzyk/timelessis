"""TableShape views module."""
import pytest

from http import HTTPStatus

from flask import (
    Blueprint, redirect, abort, render_template, request, url_for
)

from timeless import views
from timeless.db import DB
from timeless.restaurants import models
from timeless.restaurants.table_shapes import forms
from timeless.templates.views import order_by, filter_by
from timeless.uploads import IMAGES


BP = Blueprint("table_shape", __name__, url_prefix="/table_shapes")


@pytest.mark.skip(reason="Waiting for TableShape Filtering Implementation")
class List(views.ListView):
    """ List the TableShape """
    model = models.TableShape
    template_name = "restaurants/table_shapes/list.html",


"""List.register(BP, "/")"""


@BP.route("/")
def list():
    """List all table shapes
    @todo #316:30min Improve filtering of table shapes from the UI.
     Now to filter tables from the UI, GET params should look like this:
     filter_by=description=mytable&filter_by=id=1
     It is ambiguous to make such request from a HTML from. So either
     alter the way filter fields are parsed or write some JS logic.
    """
    order_fields = request.args.getlist("order_by")
    filter_fields = request.args.getlist("filter_by")
    query = models.TableShape.query
    if order_fields:
        query = order_by(query, order_fields)
    if filter_fields:
        query = filter_by(query, filter_fields)
    return render_template(
        "restaurants/table_shapes/list.html",
        table_shapes=query.all())


class Create(views.CreateView):
    """
    Create view for TableShapes
    """
    form_class = forms.TableShapeForm
    template_name = "restaurants/table_shapes/create_edit.html"
    success_view_name = "table_shape.list"


class Edit(views.UpdateView):
    model = models.TableShape
    form_class = forms.TableShapeForm
    template_name = "restaurants/table_shapes/create_edit.html"
    success_view_name = "table_shape.list"


class Delete(views.DeleteView):
    """
    @todo #312:30min Refactor all deleting views to use `views.DeleteView`
     and the method they were registered to bluprints. See `.register` method
     in `GenericView`, use it. Also uncomment all tests related to these views.
    """
    model = models.TableShape
    success_view_name = "table_shape.list"


Create.register(BP, "/create")
Edit.register(BP, "/edit/<int:id>")
Delete.register(BP, "/delete/<int:id>")
