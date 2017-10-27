from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings
import time
import random


class start(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has ret_timer seconds to complete as many pages as possible
        self.participant.vars['expiry_timestamp'] = time.time() + self.player.task_timer 

    def vars_for_template(self):

        return {
            'debug': settings.DEBUG,  
        }


class task(Page):


    form_model = models.Player
    form_fields = ['user_text']
    # timeout_seconds = self.player.ret_timer # time? no, only works on specific pages

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3

    def vars_for_template(self):


        # current number of correctly done tasks
        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None: 
                total_payoff += p.payoff_score

        # set up messgaes in transcription task
        if self.round_number == 1: #on very first task
            correct_last_round = "<br>"
        else: #all subsequent tasks
            if self.player.in_previous_rounds()[-1].is_correct:
                correct_last_round = "Your last answer was <font color='green'>correct</font>"
            else: 
                correct_last_round = "Your last answer was <font color='red'>incorrect</font>"
        
        return {
            'total_payoff': round(total_payoff),
            'round_count':(self.round_number - 1),
            'debug': settings.DEBUG,
            'correct_last_round': correct_last_round,        
        }



    def before_next_page(self):
        self.player.score_round()


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    def after_all_players_arrive(self):
        pass

class Results(Page):

    
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None: 
                total_payoff += p.payoff_score

        self.participant.vars['task_1_score'] = total_payoff

        # only keep obs if YourEntry player_sum, is not None. 
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            if (prev_player.user_text != None):
                row = {
                    'round_number': prev_player.round_number,
                    'correct_text': prev_player.correct_text,
                    'user_text': prev_player.user_text,
                    'is_correct':prev_player.is_correct,
                    'payoff': round(prev_player.payoff_score),
                }
                table_rows.append(row)

        self.participant.vars['t1_results'] = table_rows

        return {
        'table_rows': table_rows,
        'total_payoff':round(total_payoff),
        }

    # def before_next_page(self):
    #     self.participant.vars['start_time'] = None


page_sequence = [
        start, 
        task, 
        ResultsWaitPage,
        Results
        ]






        