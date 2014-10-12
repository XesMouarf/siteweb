# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'],lazy_tables=True)

"""
response.optimize_css = 'concat,minify,inline'
response.optimize_js = 'concat,minify,inline'
"""