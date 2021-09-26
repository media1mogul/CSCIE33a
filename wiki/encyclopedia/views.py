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

def index(request):
    context = {
        "entries": util.list_entries()
    }
    return render(request, "encyclopedia/index.html", context)


def page(request, name):
    """
    :param request:
    :param name: name of the page to be displayed
    :return:
    """

    # Instantiate Markdown object
    markdowner: Markdown = Markdown()
    # Convert the markdown text to html
    wiki_page_html = util.get_entry(name)
    if wiki_page_html is None:
        not_found_md = f"There is not wiki entry for: **{ name }** "
        context = {
        "name": name,
        "wiki_page_text": markdowner.convert(not_found_md)
        }
    else:
        context = {
        "name": name,
        "wiki_page_text": markdowner.convert(str(wiki_page_html))
        }

    return render(request, "encyclopedia/page.html", context)
