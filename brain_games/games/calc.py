# -*- coding:utf-8 -*-

"""Calculating game."""

from brain_games.games import drive


def game(user_name):
    """Provide a little game logic."""
    drive.cycle(user_name, 'calc')