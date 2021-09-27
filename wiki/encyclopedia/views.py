from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from datetime import date
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewWikiPageForm(forms.Form):
    title = forms.CharField(label="New Page Title")
    body = forms.CharField(label="Page Content", widget=forms.Textarea())


def index(request):
    """
    Handle the default request path
    :param request:
    :return:
    """
    context = {
        "title": "Encyclopedia",
        "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)


def page(request, title):
    """
    Handle a request for a specific page in the wiki
    :param request:
    :param name: name of the page to be displayed
    :return:
    """

    # Instantiate Markdown object
    markdowner: Markdown = Markdown()
    # Convert the markdown text to html
    body = util.get_entry(title)
    if body is None:
        bold_text = f"There is no Wiki entry for: {title}"
        error_title = "Error"
        body = "."
        url = reverse("wiki:error") + f"?title={error_title}&bold_text={bold_text}&body={body}"
        return HttpResponseRedirect(url)
    else:
        context = {
            "is_error": False,
            "title": title,
            "bold_text": title,
            "body": markdowner.convert(str(body))
        }
    return render(request, "encyclopedia/page.html", context)


def add(request):
    """
    Handle the user requesting to add a new page
    - It appears here that a session is appropriate. I will use it to compare the before and after directory listing
    :param request:
    :return:
    """
    context = {
        "title": "New Encyclopedia Page",
        "form": NewWikiPageForm()
    }

    if request.method == "POST":
        new_page_form: NewWikiPageForm = NewWikiPageForm(request.POST)
        if new_page_form.is_valid():
            title = new_page_form.cleaned_data["title"]
            body = new_page_form.cleaned_data["body"]
            if util.save_entry(title, body):
                return HttpResponseRedirect(reverse("wiki:page", args=(title,)))
            else:
                bold_text = f"Wiki page: {title} already exists."
                error_title = "Error"
                body = f"Try again with a new name, or edit the existing page."
                url = reverse("wiki:error") + f"?title={error_title}&bold_text={bold_text}&body={body}"
                return HttpResponseRedirect(url)

        else:  # Handle failed validation
            bold_text = f"Attempt to create Wiki page failed validation.",
            error_title = "Error"
            body = "."
            url = reverse("wiki:error") + f"?title={error_title}&bold_text={bold_text}&body={body}"
            return HttpResponseRedirect(url)

    return render(request, "encyclopedia/add.html", context)


def error(request):
    """
    Handle a request for a specific page in the wiki
    :param title:
    :param request:
    :param name: name of the page to be displayed
    :return:
    """
    context = {
        "title": request.GET.get('title'),
        "bold_text": request.GET.get('bold_text'),
        "body": request.GET.get('body'),
        "is_error": True
    }
    return render(request, "encyclopedia/page.html", context)


def edit(request):
    """
    Handle the user requesting to add a new page
    - It appears here that a session is appropriate. I will use it to compare the before and after directory listing
    :param request:
    :return:
    """
    context = {
        "title": f"Editing: { request.GET.get('title') }",
        "bold_text": request.GET.get('title'),
        "body": request.GET.get('title'),
    }

    return render(request, "encyclopedia/edit.html", context)
