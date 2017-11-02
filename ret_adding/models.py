# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random




# </standard imports>



author = 'Curtis Kephart (economicurtis@gmail.com)'

doc = """
Real Effort Task. Add as many ints as possible.  
"""

class Constants(BaseConstants):
    name_in_url = 'task_sum'
    players_per_group = None
    task_timer = 120 #see Subsession, before_session_starts setting. 
    num_rounds = 100 # must be more than the max one person can do in task_timer seconds

    INTS_T1 = [ 
    [   90  ,   95  ]   ,
    [   14  ,   19  ]   ,
    [   35  ,   50  ]   ,
    [   30  ,   29  ]   ,
    [   34  ,   31  ]   ,
    [   78  ,   82  ]   ,
    [   60  ,   27  ]   ,
    [   38  ,   70  ]   ,
    [   85  ,   19  ]   ,
    [   89  ,   26  ]   ,
    [   19  ,   18  ]   ,
    [   64  ,   83  ]   ,
    [   32  ,   99  ]   ,
    [   14  ,   17  ]   ,
    [   51  ,   60  ]   ,
    [   71  ,   49  ]   ,
    [   20  ,   87  ]   ,
    [   44  ,   75  ]   ,
    [   74  ,   88  ]   ,
    [   75  ,   70  ]   ,
    [   56  ,   24  ]   ,
    [   43  ,   60  ]   ,
    [   80  ,   84  ]   ,
    [   72  ,   14  ]   ,
    [   82  ,   67  ]   ,
    [   61  ,   23  ]   ,
    [   55  ,   11  ]   ,
    [   75  ,   35  ]   ,
    [   25  ,   25  ]   ,
    [   80  ,   74  ]   ,
    [   29  ,   22  ]   ,
    [   17  ,   32  ]   ,
    [   55  ,   12  ]   ,
    [   14  ,   77  ]   ,
    [   21  ,   90  ]   ,
    [   37  ,   24  ]   ,
    [   83  ,   90  ]   ,
    [   96  ,   69  ]   ,
    [   89  ,   69  ]   ,
    [   43  ,   86  ]   ,
    [   84  ,   29  ]   ,
    [   59  ,   33  ]   ,
    [   86  ,   34  ]   ,
    [   18  ,   20  ]   ,
    [   29  ,   92  ]   ,
    [   64  ,   82  ]   ,
    [   34  ,   65  ]   ,
    [   14  ,   65  ]   ,
    [   15  ,   23  ]   ,
    [   85  ,   44  ]   ,
    [   53  ,   86  ]   ,
    [   80  ,   93  ]   ,
    [   68  ,   51  ]   ,
    [   96  ,   32  ]   ,
    [   58  ,   72  ]   ,
    [   85  ,   92  ]   ,
    [   44  ,   49  ]   ,
    [   72  ,   53  ]   ,
    [   18  ,   21  ]   ,
    [   86  ,   85  ]   ,
    [   82  ,   47  ]   ,
    [   25  ,   91  ]   ,
    [   25  ,   17  ]   ,
    [   15  ,   76  ]   ,
    [   36  ,   59  ]   ,
    [   70  ,   77  ]   ,
    [   24  ,   40  ]   ,
    [   13  ,   91  ]   ,
    [   42  ,   20  ]   ,
    [   85  ,   64  ]   ,
    [   58  ,   93  ]   ,
    [   63  ,   41  ]   ,
    [   65  ,   61  ]   ,
    [   16  ,   12  ]   ,
    [   54  ,   45  ]   ,
    [   95  ,   91  ]   ,
    [   61  ,   92  ]   ,
    [   11  ,   15  ]   ,
    [   44  ,   22  ]   ,
    [   87  ,   37  ]   ,
    [   88  ,   32  ]   ,
    [   52  ,   41  ]   ,
    [   50  ,   77  ]   ,
    [   32  ,   13  ]   ,
    [   35  ,   60  ]   ,
    [   58  ,   88  ]   ,
    [   94  ,   31  ]   ,
    [   56  ,   48  ]   ,
    [   68  ,   80  ]   ,
    [   43  ,   86  ]   ,
    [   65  ,   86  ]   ,
    [   46  ,   62  ]   ,
    [   97  ,   34  ]   ,
    [   52  ,   96  ]   ,
    [   95  ,   13  ]   ,
    [   27  ,   54  ]   ,
    [   28  ,   82  ]   ,
    [   47  ,   98  ]   ,
    [   40  ,   59  ]   ,
    [   91  ,   74  ]   ,
    [   81  ,   34  ]   ,
    [   66  ,   57  ]   ,
    [   42  ,   18  ]   ,
    [   58  ,   85  ]   ,
    [   68  ,   82  ]   ,
    [   38  ,   43  ]   ,
    [   20  ,   91  ]   ,
    [   57  ,   26  ]   ,
    [   96  ,   14  ]   ,
    [   73  ,   73  ]   ,
    [   66  ,   24  ]   ,
    [   97  ,   74  ]   ,
    [   25  ,   59  ]   ,
    [   81  ,   97  ]   ,
    [   87  ,   97  ]   ,
    [   29  ,   80  ]   ,
    [   67  ,   18  ]   ,
    [   82  ,   60  ]   ,
    [   63  ,   65  ]   ,
    [   56  ,   30  ]   ,
    [   36  ,   42  ]   ,
    [   37  ,   80  ]   ,
    [   66  ,   86  ]   ,
    [   14  ,   52  ]   ,
    [   52  ,   77  ]   ,
    [   68  ,   39  ]   ,
    [   87  ,   91  ]   ,
    [   87  ,   36  ]   ,
    [   52  ,   74  ]   ,
    [   50  ,   44  ]   ,
    [   61  ,   64  ]   ,
    [   65  ,   58  ]   ,
    [   11  ,   34  ]   ,
    [   99  ,   91  ]   ,
    [   39  ,   18  ]   ,
    [   82  ,   22  ]   ,
    [   46  ,   40  ]   ,
    [   89  ,   26  ]   ,
    [   68  ,   65  ]   ,
    [   60  ,   73  ]   ,
    [   99  ,   82  ]   ,
    [   82  ,   89  ]   ,
    [   34  ,   38  ]   ,
    [   12  ,   30  ]   ,
    [   52  ,   99  ]   ,
    [   89  ,   61  ]   ,
    [   52  ,   89  ]   ,
    [   76  ,   54  ]   ,
    [   48  ,   32  ]   ,
    [   56  ,   29  ]   ,
    [   85  ,   39  ]   ,
    [   43  ,   39  ]   ,
    [   35  ,   43  ]   ,
    [   97  ,   31  ]   ,
    [   94  ,   26  ]   ,
    [   53  ,   77  ]   ,
    [   30  ,   63  ]   ,
    [   22  ,   88  ]   ,
    [   36  ,   28  ]   ,
    [   37  ,   49  ]   ,
    [   35  ,   64  ]   ,
    [   65  ,   40  ]   ,
    [   27  ,   70  ]   ,
    [   55  ,   84  ]   ,
    [   26  ,   63  ]   ,
    [   28  ,   34  ]   ,
    [   37  ,   59  ]   ,
    [   99  ,   49  ]   ,
    [   18  ,   84  ]   ,
    [   21  ,   35  ]   ,
    [   95  ,   56  ]   ,
    [   12  ,   37  ]   ,
    [   39  ,   28  ]   ,
    [   81  ,   60  ]   ,
    [   65  ,   46  ]   ,
    [   17  ,   44  ]   ,
    [   30  ,   79  ]   ,
    [   49  ,   15  ]   ,
    [   35  ,   84  ]   ,
    [   56  ,   33  ]   ,
    [   95  ,   32  ]   ,
    [   15  ,   57  ]   ,
    [   99  ,   12  ]   ,
    [   30  ,   39  ]   ,
    [   23  ,   90  ]   ,
    [   72  ,   14  ]   ,
    [   59  ,   30  ]   ,
    [   40  ,   87  ]   ,
    [   31  ,   21  ]   ,
    [   65  ,   49  ]   ,
    [   69  ,   27  ]   ,
    [   76  ,   41  ]   ,
    [   94  ,   85  ]   ,
    [   44  ,   36  ]   ,
    [   19  ,   30  ]   ,
    [   11  ,   14  ]   ,
    [   84  ,   39  ]   ,
    [   50  ,   70  ]   ,
    [   41  ,   59  ]   ,
    [   35  ,   35  ]   ]

class Subsession(BaseSubsession):

    def before_session_starts(self):

        players = self.get_players()
        if 'task_timer' in self.session.config:
            task_timer = self.session.config['task_timer']
        else:
            task_timer = Constants.task_timer

        for p in self.get_players():
            p.task_timer = task_timer
            p.int1 = Constants.INTS_T1[self.round_number - 1][0]
            p.int2 = Constants.INTS_T1[self.round_number - 1][1]
            p.solution = p.int1 + p.int2

class Group(BaseGroup):
	pass

class Player(BasePlayer):

    def score_round(self):
        # update player payoffs
        if (self.solution == self.user_total):
            self.is_correct = True
            self.payoff_score = 1
        else: 
            self.is_correct = False
            self.payoff_score = c(0)      



    task_timer = models.PositiveIntegerField(
        doc="""The length of the real effort task timer."""
    )

    int1 = models.PositiveIntegerField(
        doc="this round's first int")

    int2 = models.PositiveIntegerField(
        doc="this round's second int")

    solution = models.PositiveIntegerField(
        doc="this round's correct summation")

    user_total = models.PositiveIntegerField(
        min = 1,
        max = 9999,
        doc="user's summation",
        widget=widgets.TextInput(attrs={'autocomplete':'off'}))

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    payoff_score = models.FloatField(
            doc = '''score in this task'''
        )
