"""tables views module.
"""
from flask import Blueprint

from timeless import views
from timeless.restaurants import models
from timeless.restaurants.tables import forms


BP = Blueprint("table", __name__, url_prefix="/tables")


class TableListView(views.ListView):
    """ List the tables """
    model = models.Table
    template_name = "restaurants/tables/list.html"


class Create(views.CreateView):
    form_class = forms.TableForm
    success_view_name = "table.list_tables"
    template_name = "restaurants/tables/create_edit.html"


class Edit(views.UpdateView):
    """View for editing a table"""
    model = models.Table
    form_class = forms.TableForm
    template_name = "restaurants/tables/create_edit.html"
    success_view_name = "table.list_tables"


class Delete(views.DeleteView):
    """View for deleting a table"""
    model = models.Table
    success_view_name = "table.list_tables"


TableListView.register(BP, "/")
Create.register(BP, "/create")
Edit.register(BP, "/edit/<int:id>")
Delete.register(BP, "/delete/<int:id>")
