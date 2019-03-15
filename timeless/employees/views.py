"""Employees views module.
@todo #357:30min Continue implementing ListView to enable filtering
 for every column. For this, probably there will be a need to create a new
 generic view that all other List views will extend. This generic view should
 use GenericFilter implemented in #317.
"""
from flask import Blueprint

from timeless.access_control.views import SecuredView
from timeless.employees.forms import EmployeeForm
from timeless import views
from timeless.employees.models import Employee

BP = Blueprint("employee", __name__, url_prefix="/employees")


class Create(views.CreateView, SecuredView):
    """Create employee"""
    template_name = "employees/create_edit.html"
    form_class = EmployeeForm
    model = Employee
    success_view_name = "employee.list"
    resource = "employee"

    def get(self, **kwargs):
        context = self.get_context(action="create")
        return self.render_to_response(context)


# class Edit(views.UpdateView):
#     """Update employee"""
#     template_name = "employees/create_edit.html"
#     form_class = EmployeeForm
#     model = Employee


class Delete(views.DeleteView, SecuredView):
    """Delete employee"""
    model = Employee
    success_view_name = "employee.list"
    resource = "employee"


class List(views.ListView, SecuredView):
    """List all employees"""
    model = Employee
    success_view_name = "employee.list"
    resource = "employee"
    """
    @todo #348:15min Delete template_name from List after #312 will be pulled
     to the master branch. "template_name" is using now due to current
     implementation of views.DeleteView.
    """
    template_name = "employees/list.html"


List.register(BP, "/")
Create.register(BP, "/create")
# Edit.register(bp, "/edit/<int:id>")
Delete.register(BP, "/<int:id>/delete")
