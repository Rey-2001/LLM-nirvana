import pytest
from unittest.mock import Mock
from forms import Jinja2Forms, Form
from schemas import Schema
from fields import Field, Choice, Boolean, String
from forms import *

class TestForm:
    def test_render_fields_without_values(self):
        schema = Mock(fields={"field1": Field(), "field2": Field()})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert form.render_fields() == "<html>...</html>"

    def test_render_fields_with_values(self):
        schema = Mock(fields={"field1": Field(), "field2": Field()})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema, values={"field1": "value1", "field2": "value2"})

        assert form.render_fields() == "<html>...</html>"
        
    def test_render_field(self):
        field = Field(title="Field", allow_null=False)
        schema = Mock(fields={"field1": field})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert form.render_field(field_name="field1", field=field) == "<input type='text' name='field1' required/>"
        
    def test_template_for_field(self):
        boolean_field = Boolean()
        choice_field = Choice(choices=[("1", "One"), ("2", "Two")])
        string_field = String(format="text")
        other_field = Field()
        schema = Mock(fields={"boolean_field": boolean_field, "choice_field": choice_field, "string_field": string_field, "other_field": other_field})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert form.template_for_field(boolean_field) == "forms/checkbox.html"
        assert form.template_for_field(choice_field) == "forms/select.html"
        assert form.template_for_field(string_field) == "forms/textarea.html"
        assert form.template_for_field(other_field) == "forms/input.html"
        
    def test_input_type_for_field(self):
        boolean_field = Boolean()
        string_field = String(format="email")
        other_field = Field()
        schema = Mock(fields={"boolean_field": boolean_field, "string_field": string_field, "other_field": other_field})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert form.input_type_for_field(boolean_field) == "checkbox"
        assert form.input_type_for_field(string_field) == "email"
        assert form.input_type_for_field(other_field) == "text"
        
    def test_str(self):
        schema = Mock(fields={"field1": Field(), "field2": Field()})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert str(form) == "<html>...</html>"
        
    def test_html(self):
        schema = Mock(fields={"field1": Field(), "field2": Field()})
        jinja2_forms = Jinja2Forms(directory="templates")
        form = Form(env=jinja2_forms.env, schema=schema)
        
        assert form.__html__() == "<html>...</html>"


class TestJinja2Forms:
    def test_load_template_env_with_directory(self):
        jinja2_forms = Jinja2Forms(directory="templates")
        env = jinja2_forms.load_template_env(directory="templates")

        assert isinstance(env, jinja2.Environment)

    def test_load_template_env_with_package(self):
        jinja2_forms = Jinja2Forms(package="forms")
        env = jinja2_forms.load_template_env(package="forms")

        assert isinstance(env, jinja2.Environment)

    def test_form_method(self):
        schema = Mock(spec=Schema)
        jinja2_forms = Jinja2Forms(directory="templates")
        form = jinja2_forms.Form(schema=schema)
        
        assert isinstance(form, Form)