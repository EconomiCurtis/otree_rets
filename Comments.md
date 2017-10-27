

The experiment is made up of a series of otree apps. The ret, the quiz, the vcm game, and stage game. 




## csr0 ret 
is the real effort task
- this creates a var passed into next stages with subjects ret scores. the variable is ret_score stored in self.participant.vars 
- if you see a ret score of "61" (an impossible ret score) that means the experimetn didn't pass that ret score correctly somewhere. 



## crs1 quiz 
is the quiz section

## csr2 vcm
is the vcm game. 
- it should take the ret score from csr0 and use it as one's own ret score. 
- it should take the other players' in one's group as the other scores
- if you see an own score of 61 and other score of [41,50,61] that means these variables were not passed between apps. 

### role assignment
this app also gets people's group exchange contributions (as percent), and ranks players by ge%, with the two highest ge% role A, and the two lowest role F. 
if there is a tie, the tie is broken, ties are broken by player id number ranks. (I didn't want a random number method so that we'd have a consistent and predictable way to break ties.)

## csr3 quiz

a short quiz like csr1 quiz

## csr3
is the stage game. 

again, if you see a ret score of 61 that means the correct ret score wasnt passed between apps. 

if roles were not assigned, P1 and P2 are role A and P3 and P4 are role F. 

Issues:
- The line "This part of the experiment is divided into 5 identical rounds of the same type of investment game as in Part 2. In each round, both Role A and Role F participants will receive the endowment they earned in Part 1. You will receive 60 points and your partner will receive 60 points." 
 This line may contradict the line preceding. What if you only earned 40 points in the RET? 
 Maybe it should that read "You will receive ___insert_own_RET_score__ and your partner will receive __insert_partner_ret___ points."? I removed the sentence for now.
- The line "A2means Role F will be asked to increase his or her contribution over and above what s/he contributed to the Investment Account in Part 2." should that read "Group exchange" and not Investment Account? It's called Common exchange in a quiz q in same treatment too. 