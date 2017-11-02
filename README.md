# otree_rets

oTree project with a number of Real Effort Task (RET) example apps Edit



## ret_typing

`ret_typing` is an oTree app that asks players to correctly type as many character strings as possible in a certain number of seconds. (set in `settings.py` >> `ret_timer`). 

![oTree Typing Real Effort Task (RET)](/_static/misc/typing_ret.gif)


[[Insert gif about here]]

- The sequence of character strings is set in `models.py`. This sequence is currently fixed, i.e. not randomly generated on the fly. 
- The length of the RET is set in `settings.py` (see config field `ret_timer`). If you want this to vary by period or subject or anything, see `models.py` >> `Subsession` for a good place to add additional logic. 
- The timer is handled by `views.py` >> `get_timeout_seconds`
- Converting the string to an image is handled by a js script in `templates/ret_typing/task.html` >> `Text to png Image`. The string will actually appear in page source and via the Inspect element, but takes a little work to find it. 
- Results page has a complete log of RET attempts and accounting of one's score. You may want to tone that down, and reduce the amount of information given to subjects.
- Note in instructions, "Once you have entered your summation, click the <b>Next</b> button or press the <b>Enter</b> key." I found that some subjects ignored the second part of that sentence. Be aware that one's score can be significantly less if subjects are not aware of the just-click-enter-to-get-the-next-ret feature. 



## ret_adding

`ret_adding` is an oTree app that asks players to correctly add as many integers (set in `models.py` >> `Constants`) of as possible in a certain number of seconds (set in `settings.py` >> `ret_timer`).

![oTree Adding Real Effort Task (RET)](/_static/misc/adding_ret.gif)

