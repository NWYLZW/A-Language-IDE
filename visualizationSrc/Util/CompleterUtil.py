#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CompleterUtil.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 7:25
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''

"""Code completion logic in the text editor."""
import io
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt

from .frozenDir import tempPath

class Completer(object):
    """Comleter class to use in the query text editor."""

    def __init__(self):
        """Initialize Completer class with the functions."""
        with io.open(
                tempPath()+r'\visualizationSrc\Data\completer_data\functions.txt', 'r', encoding='utf-8') as f:
            titlecase_funcs = [f.rstrip() for f in f.readlines()]
            uppercase_funcs = [f.upper() for f in titlecase_funcs]
            lowercase_funcs = [f.lower() for f in titlecase_funcs]

        all_keywords_and_funcs = [
            lowercase_funcs,
            uppercase_funcs,
            titlecase_funcs,
        ]

        self.standard_items = [
            keyword for sublist in all_keywords_and_funcs for keyword in sublist
        ]

        self.completer = QCompleter(self.standard_items)

        self.completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        self.completer.setCaseSensitivity(Qt.CaseSensitive)
        self.completer.setWrapAround(False)
        return
    def update_completer_string_list(self, items):
        """Update completer string list to include additional strings.
        The list of additional strings include geodatabase items.
        """
        cur_items = []
        titlecase_items = [i.title() for i in items]
        uppercase_items = [i.upper() for i in items]
        lowercase_items = [i.lower() for i in items]

        cur_items.extend(self.standard_items)
        cur_items.extend(titlecase_items + uppercase_items + lowercase_items)
        self.completer.model().setStringList(cur_items)
        return