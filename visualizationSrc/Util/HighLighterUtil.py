#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   HighLighterUtil.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 6:50
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import io
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import (QTextCharFormat, QColor, QFont, QSyntaxHighlighter)

from visualizationSrc.Util.frozenDir import tempPath

class HighLighter(QSyntaxHighlighter):
    """Highlighter class to provide text coloring in the query panel."""
    def __init__(self, parent=None):
        """Initialize Highlighter with basic highlight options."""
        super(HighLighter, self).__init__(parent)

        self.setHighlightRulesKeywords()
        self.setHighlightRulesNumeric()
        self.setHighlightRulesComments()
        self.setHighlightRulesTODO()
        self.setHighlightRulesSTR()
        self.setHighlightRulesFunction()

        self.multi_line_comment_format = QTextCharFormat()
        self.multi_line_comment_format.setForeground(Qt.darkGreen)
        self.comment_start_expression = QRegExp('/\*')
        self.comment_end_expression = QRegExp('\*/')
        return
    def setHighlightRulesKeywords(self):
        """关键词代码高亮"""
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keyword_format.setFontWeight(QFont.Bold)
        with io.open(
                tempPath()[0]+r'\visualizationSrc\Data\completer_data\keywords.txt', 'r', encoding='utf-8') as f:
            self.plain_keywords = [k.rstrip() for k in f.readlines()]
        keyword_patterns = [
            '\\b{0}\\b'.format(plain_keyword)
            for plain_keyword in self.plain_keywords
        ]

        self.highlight_rules = []
        for pattern in keyword_patterns:
            regexp = QRegExp(pattern)
            regexp.setCaseSensitivity(Qt.CaseInsensitive)
            self.highlight_rules.append((regexp, keyword_format))
    def setHighlightRulesNumeric(self):
        """数字代码高亮"""
        numeric_format = QTextCharFormat()
        numeric_format.setForeground(Qt.blue)
        regex = QRegExp(r'\s[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?')
        self.highlight_rules.append((regex, numeric_format))
    def setHighlightRulesComments(self):
        """注释代码高亮"""
        single_line_comment_format = QTextCharFormat()
        single_line_comment_format.setForeground(Qt.darkGreen)
        self.highlight_rules.append((QRegExp('//.*'),
                                     single_line_comment_format))
        return
    def setHighlightRulesTODO(self):
        """TODO代码高亮"""
        single_line_comment_format = QTextCharFormat()
        single_line_comment_format.setForeground(QColor(0, 121, 196))
        self.highlight_rules.append((QRegExp('// TODO.*'),
                                     single_line_comment_format))
        return
    def setHighlightRulesFunction(self):
        """函数代码高亮"""
        function_format = QTextCharFormat()
        function_format.setFontItalic(True)
        function_format.setForeground(QColor(237, 162, 0))
        self.highlight_rules.append((QRegExp('\\b[A-Za-z0-9_]+:'),
                                     function_format))
    def setHighlightRulesSTR(self):
        quote_format = QTextCharFormat()
        quote_format.setForeground(QColor(0, 127, 132))
        self.highlight_rules.append((QRegExp('\".*\"'), quote_format))
        self.highlight_rules.append((QRegExp('\'.*\''), quote_format))
        return
    def highlightBlock(self, text):  # noqa: N802
        """Reimplementation of the built-in method."""
        for pattern, format_ in self.highlight_rules:
            expression = QRegExp(pattern)
            idx = expression.indexIn(text)
            while idx >= 0:
                length = expression.matchedLength()
                self.setFormat(idx, length, format_)
                idx = expression.indexIn(text, idx + length)

        self.setCurrentBlockState(0)

        start_idx = 0
        if self.previousBlockState() != 1:
            start_idx = self.comment_start_expression.indexIn(text)

        while start_idx >= 0:
            end_index = self.comment_end_expression.indexIn(text, start_idx)

            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_idx
            else:
                matched_length = self.comment_end_expression.matchedLength()
                comment_length = end_index - start_idx + matched_length

            self.setFormat(start_idx, comment_length,
                           self.multi_line_comment_format)
            start_idx = self.comment_start_expression.indexIn(
                text, start_idx + comment_length)
        return