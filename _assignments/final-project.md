---
title: Final Project
date: 2018-03-16 0:00:00 -04:00
description: |
  From now until the end of the semester you will be working with a team
  of students on a group software project. The project will culminate during the Final
  Event period for this class,  with an EXPO style demo / poster session.
announce: 2018-03-16 13:30:00 -04:00
due: 2018-05-08 12:00:00 -05:00
proposal_survey_url: https://about:blank
spreadsheet_url: https://about:blank
parts:
- name: Team Registration Survey
  due: 2018-03-29 13:30:00 -04:00
  tag: team-registration-survey
- name: Project Proposal
  due: 2018-03-29 13:30:00 -04:00
  tag: project-proposal
- name: AR Preparation Document
  due: 2018-04-03 13:30:00 -04:00
  tag: architectural-review
- name: AR Reflection Document
  due: 2018-04-10 13:30:00 -04:00
  tag: architectural-review
- name: Project Presentation
  due: 2018-04-24 13:30:00 -04:00
  tag: project-presentation
- name: Project Website MVP
  due: 2018-04-24 13:30:00 -04:00
  tag: project-website-mvp
- name: Project Website, feedback addressed
  due: 2018-05-01 13:30:00 -04:00
  tag: project-website-final
- name: Final Deliverables
  due: 2018-05-08 12:00:00 -04:00
  tag: demo-session-poster
type: index
team_registration_survey_part: 0
proposal_part: 1
arch_review_part: 2
presentation_part: 4
website_part: 5
website_revision: 6
expo_part: 7
final_deliverables_part: 7
---

{% include toc %}

## Overview

From now until the end of the semester you will be working with a team of
students on a group software project. The project will culminate during the
Final Event period for this class, with an EXPO style demo / video / poster session.

## Project Topic

### Requirements

* As this class is called "Software Design", your project should have a substantial software design component (interfacing with mechanical or electrical systems is considered on a case by case basis, but the software should be the major component).
* Most of the your final project should be written in Python. It is okay if some amount is written in another language, but the bulk of the project should be implemented in Python. Part of the reason for this requirement is to facilitate peer design reviews.

### Suggestions for Project Topics

* Because the theme of this course is "computation as applied to interesting problems in science, engineering, and beyond" you may want to use this project as an opportunity to explore how computation can be applied to a discipline / problem you care deeply about. Choosing an interdisciplinary project may also allow your software design project to overlap with work you are doing in other courses (we are fine with this, but we would have to check with the other instructors to make sure this is okay). If you choose to be interdisciplinary, perhaps we can recruit an appropriate faculty angel adviser for your project.
* If you want to have some experience doing a project "for" a client, talk to faculty and staff on campus. Talk to parents and relatives with real jobs. Perhaps, they have a need that your team can help with.
* Make a positive difference in the world. See broken things and try to fix them.
* A good project is one that meets your learning goals. For instance, if it is really important to you to learn how to create a program with a GUI, you should make sure that your project topic aligns with this learning goal.
* A good project is one that has a realistic and well-defined minimum deliverable as well as many opportunities for going beyond the minimum deliverable (depending on the pace and enthusiasm of the team).

## Teaming

### Requirements

* You are required to work on a team of 2-4 students. Instructors will help facilitate teaming (and approve final teams)

### Team Formation Advice

* Try to **work with people because you share a common interest** rather than simply working with your friends (we will offer guidance during the final project kick-off).
* **Work with people that want to devote similar amounts of time to the project.** For instance, if you want to devote your life to making the best most awesomest SoftDes project ever, you should probably work with other people who share that desire!
* **Work with people that envision a similar style of work on the project.** For instance, if you really want to pair-program the entire project, but your teammates prefer to divvy up the work and work independently, that is probably not a good situation.

Refer back to the answers you provided during the reflection and teaming surveys and share your thoughts with potential teammates.

## Project Activities / Deliverables

### Team Registration Survey
_Due {{ page.parts[page.team_registration_survey_part].due | date: site.part_due_date_format }}_

Once you know who is on your team, you should create a GitHub repository for your final project.  Note: that there is no GitHub classroom assignment to accept and there is no base repository to fork (instead you will be [creating your repository from scratch](https://help.github.com/articles/create-a-repo/)).  Whoever creates the repository should add the other team members as collaborators.  You will be using this repository to turn in all of the project deliverables listed below.

Once your team's GitHub repository is set, you are ready to fill out the [team registration survey](https://docs.google.com/forms/d/e/1FAIpQLSdlqZgPCi8dIfyREs8MTb4cWpo3o3hmpFoGvhEmmxJhkwL27w/viewform).  We will need you to fill out this survey in order to know where to look for your other project deliverables, so please complete it as soon as you can.

### Project Proposal

_Due {{ page.parts[page.proposal_part].due | date: site.part_due_date_format }}_

**The project proposal is worth 10% of the project grade ([rubric]({% link _assignments/final-project/project-proposal-rubric.md %})).**

Create a document on your team's final project repo that answers the following questions. More detailed answers give us an ability to give you better feedback to start the project (or revise your proposal).

1. **The Big Idea:** What is the main idea of your project? What topics will you explore and what will you generate? What is your **minimum viable product**? What is a **stretch goal**?
2. **Learning Goals:** What are your individual learning goals for this project?
3. **Implementation Plan:** This will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don't have any idea how you will implement your project, provide a rough plan for how you will determine this information.
4. **Project schedule:** You have 6 weeks (roughly) to finish the project. Sketch out a rough schedule for completing the project. Depending on your project, you may be able to do this in great specificity or you may only be able to give a broad outline. Additionally, longer projects come with increased uncertainty, and this schedule will likely need to be refined along the way.
5. **Collaboration plan:** How do you plan to collaborate with your teammates on this project? Will you split tasks up, complete them independently, and then integrate? Will you pair program the entire thing? Make sure to articulate your plan for successfully working together as a team. This might also include information about any software development methodologies you plan to use (e.g. [agile development](http://en.wikipedia.org/wiki/Agile_software_development)). Make sure to make clear why you are choosing this particular organizational structure.
6. **Risks:** What do you view as the biggest risks to the success of this project?
7. **Additional Course Content:** What are some topics that we might cover in class that you think would be especially helpful for your project?

The teaching team will either approve your page, or provide suggestions and request revisions.

### Architectural Review

_Date: {{ page.parts[page.arch_review_part].due | date: '%A, %B %-d' }}_

**The Architectural review is worth 15% of the project grade ([rubric]({% link _assignments/final-project/architectural-review.md %})).**

Each team will complete one (or more) architectural reviews, which will entail teams presenting plans for their project to other teams, NINJAs, and instructors.
This review is intended to very interactive, and will focus on soliciting useful/actionable feedback rather than being a one-way brain dump.
In addition to the in-person component of this activity, there will be a
framing/agenda setting document due before the review and a
reflection/synthesis document due after.

See the [Architectural Review]({% link _assignments/final-project/architectural-review.md %}) page for full details about the assignment.

### Project Presentation

{% assign part = page.parts[page.presentation_part] %}
_Date: {{ part.due | date: '%A, %B %-d' }}_

**The Project Presentation is worth 10% of the project grade** **(see [project presentation rubric]({% link _assignments/final-project/project-presentation-rubric.md %}))**

On {{ page.parts[page.presentation_part].due | date: '%A, %B %-d' }}, your team will present the progress with the project to the studio.
This is intended to be a formal / polished presentation. The focus of this activity will be around successful and professional communication.
There will be limited time for feedback in class, but you can communicate your feedback using the online form.

### Project Website

{% assign part = page.parts[page.website_part] %}
_Due: {{ part.due | date: '%-I:%M %p %A, %B %-d' }}._

_Final revision, that incorporates instructor feedback, due {{ page.parts[page.website_revision].due | date: '%-I:%M %p %A, %B %-d' }}._

**The final website is worth 15% of the project grade**

Your project website is the lasting record of what you have accomplished over
the course of this project, and hopefully a valuable contribution to your
professional portfolio. You should draw upon all the deliverables and
activities above to create the final site, combining, reformatting, and adding
to them to effectively tell the story of your project.

The project website can serve many audiences, including:

* Current and future SoftDes students and faculty
* Potential users of your software and those with a domain-specific interest in your topic
* Future employers
* Final event audience, broader Olin community, family

There are many successful formats for a project website, but you should
consider including:

* **Big Idea/Goal/What is this?/** **Why did we do this?**
Quick and easily understandable explanation of what your project is all about.
Consider including a narrative or example use case, e.g. via screenshots,
video, or story boarding.

* **User instructions/README**
Information to help users download, install, and get started running your
software ([README rubric]({% link _assignments/final-project/readme-rubric.md %}))

* **Implementation information**
Code doesn't tell a story by itself. Use more effective methods such as
flowcharts and architectural, class, or sequence diagrams to explain how your
code works. You could consider including or linking to snippets of code to
highlight a particularly crucial segment.

* **Results**
Though the details will be different for each project, show off what your
software can do! Screenshots and video are likely helpful. Include graphs or
other data if appropriate.

* **Project evolution/narrative**
Tell an illustrative story about the process of creating your software,
showing how it improved over time. This may draw upon what you learned from
the two peer technical reviews and from the code review. Consider the use of
screenshots or other tools to demonstrate how your project evolved.

* **Attribution**
Give proper credit for external resources used.

**_Note_**: These content prompts exist to inspire your thinking, and you should use whatever organization and sections make sense for your project and the story you're telling. Simply answering the given prompts sequentially is not the strongest way to communicate your work to an external audience. Think about what you've accomplished and frame it nicely - finish strong!

Your final project website may be implemented using whatever platform you
like. You can continue to use [GitHub pages](https://pages.github.com/),
possibly along with [Jekyll](http://jekyllrb.com/docs/github-pages/), or you
can switch to an easier option like [Google Sites](https://sites.google.com/).
If you'd like to make a GitHub site with multiple pages using Markdown,
former SoftDes NINJAs Patrick and Franton have written a [helpful
guide](http://phuston.github.io/patrickandfrantonarethebestninjas/howto).

Whatever implementation option you choose, you **must** include a link to your
project website from your GitHub repository. Remember that this is part of
your professional portfolio as you select a platform -- choose something that
will still be around in the future!

**Submission mechanics**: Your project's GitHub repo page should link to your web site. This means either the README, or the Website that is optionally displayed in the upper right corner of your GitHub repo page, should contain this link.

### Demo Session Poster and Video

{% assign part = page.parts[page.expo_part] %}
_Printed before {{ part.due | date: '%-H:%M %p' }} on {{ part.due | date: '%A, %B %-d' }}_

**The poster and video are worth 10% of the project grade.**

Each team will create a poster to accompany the final demonstration session.
Your poster will contain similar information to your website, but reformatted
and selectively edited for a different context:

* **Poster** - large form factor, tool to support your demo (content need not stand alone without explanation)
* **Website** - one-way communication, allows for more complete/in-depth coverage

Posters are generally 24 x 36 inches.
You may use a larger size if you want.
You can print your poster in the Olin computer lab.

Your poster should have the same sections as your website (but leave out installation instructions). It serves two purposes:
* We will put these on the wall during the final event, to display our work to each other and to visitors
* It is practice for a research poster, which is a standard format for presenting work at an academic conference, or in the halls of an academic institution. You may have seem posters during Olin EXPOs, or on some of the AC halls at other times. [Thinking and explaining clearly and laying out your work in this format is not bad practice for industry presentations too.]

Examples and guides:
* <https://guides.nyu.edu/posters>
* <https://ugs.utexas.edu/our/poster/samples>
* <https://nau.edu/undergraduate-research/poster-presentation-tips/>
* <http://justinlmatthews.com/posterhelp/posterguide/>

**demo video**

Your website will have a video of your team demoing your project and giving a 1-minute or less pitch about it. Include the project's goal, what the software does, how to use it, why your team made it, and what you would do if you had more time.

The teaching team will offer suggestions and give feedback on draft videos related to production quality and content.


**Submission mechanics**: (1) Your project README or project web site must link to your poster file and video. (2) Your poster must also be printed in time for the {{ part.due | date: '%b %-d' }} final event.

### Code submission

{% assign part = page.parts[page.expo_part] %}
_Due: {{ part.due | date: '%A, %B %-d' }}_

**Project code is worth 40% of the project grade (see code rubric on the [course policy page]({% link pages/policies.md %}))**

Project code must be submitted via GitHub by {{ part.due | date: '%B %-d' }}. You must include a
README describing how to run your code, including any required dependencies
(e.g. libraries to install) and any input files ([README rubric]({% link _assignments/final-project/readme-rubric.md %})).

Proper documentation is important to your final submission, and one way to
ensure you have adequate docstrings is to generate documentation from them.
You can do this using [pydoc](https://docs.python.org/3/library/pydoc.html):

`$ pydoc path/to/my_project.py`

This will open a help file based on your docstrings (use q to quit). Make sure
the help file would be useful to someone using your code, and feel free to
attach it to your code submission as an appendix. If you want to generate
truly beautiful documentation, check out [Sphinx](http://sphinx-doc.org/) (the
tool used to generate the [Python documentation](https://docs.python.org/3/)).

Make sure that your code gives appropriate attribution to external resources
used, as per the [course policy page]({% link pages/policies.md %}). If you have any questions
about this, just ask.

**Submission mechanics**: Verify that the link in the [Final Project Team Survey]({{ page.spreadsheet_url }}) is correct. Check that you have git pushed your final changes to GitHub.

### Final Demo / Presentation Session

{% assign part = page.parts[page.expo_part] %}
_Date: {% if part.due %}{{ part.due | date: '%A, %b %-d, %-H:%M %p' }}–{{ part.due | date: '%-H:%M %p' }}{% else %}TBD{% endif %}_

During the Final Event, {% if site.sections > 1 %} all studios of {% endif %}
SoftDes will meet in {{ site.final_room_number }}
for an EXPO style poster/demo session of your final projects. This session is
for everyone to share what they've created, and will not be evaluated. We will
be inviting other members of the Olin community to check out your fantastic
work.
