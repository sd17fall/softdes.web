---
title: Assignment 14
due: 2017-11-02 10:50:00 -04:00
spreadsheet_url: https://docs.google.com/spreadsheets/d/1HtPkvLfhCo9cfIQAKojzhBqLgJMWCkaqQx73rdoPrTU/edit?usp=sharing
---

## Create a GitHub Repo

Create a GitHub repo for your project.

Add your team members to the repo.

Place these files in the repo:

* A [`.gitignore` file]({% link pages/recipes.md %}#gitignore-ignoring-files). This file should contain at least the line `*.pyc`.
* A project proposal.

## Create a Trello Board

Create a [Trello board](https://trello.com). Add your team mates and the professor and NINJAs:

{% for person in site.data.team %}
* {{ person.first_name }}
{% endfor %}

In class on Thursday we will finish setting this up.

## Register your team

Add your team, a link to your repo, and a link to your Trello board, to the [final project spreadsheet]({{ page.spreadsheet_url }}).

## Project Proposal

Create a [Final Project]({% link _assignments/final-project.md %}#project-proposal) document.
