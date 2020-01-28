# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:40:42 2019

@author: louis
"""

import pandas as pd
plays = pd.read_excel('original_play_by_play.xlsx')
games = pd.read_excel('Starting Lineups.xlsx')
roster = [
          'Charlie Brown', 
          'Lamarr Kimble', 
          'Jared Bynum', 
          'Chris Clover', 
          'Taylor Funk', 
          'Lorenzo Edwards', 
          'Pierfrancesco Oliva', 
          'Anthony Longpre', 
          'Troy Holston', 
          'Markell Lodge', 
          'Toliver Freeman',
          'Mike Muggeo']
# The following loads the starting lineups for each game into a tuple.
starting_lineup = {}
for full_game in range(1, 34):
    starting_lineup[full_game] = tuple(starting_lineup.get(full_game, 
                                 list(games.loc[full_game - 1, ['Starter 1', 
                                                                'Starter 2', 
                                                                'Starter 3', 
                                                                'Starter 4', 
                                                                'Starter 5']])))
game_number = 1
lineup = []
for line in range(len(plays.index)):
    # The following sets lineup at the beginning  of each game equal to
    # the starting lineup from the Excel file.
    if plays.loc[line, 'Reset Lineup'] == 1:
        game_number = plays.loc[line, 'Game No']
        lineup = list(starting_lineup[game_number])
    # The following subs players into and out of the lineup.
    if str(plays.loc[line, 'SJU Play']).rstrip() == 'SUB IN':
        player_in = str(plays.loc[line, 'SJU Player'])
        if player_in not in lineup:
            lineup.append(player_in)
    if str(plays.loc[line, 'SJU Play']).rstrip() == 'SUB OUT':
        player_out = str(plays.loc[line, 'SJU Player'])
        if player_out in lineup:
            lineup.remove(player_out)
    for active_player in lineup:
        plays.loc[line, active_player] = 1
plays.to_excel('modified_play_by_play.xlsx')
