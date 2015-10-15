# -*- coding: utf-8 -*-

import pandas as pd
import subprocess
import pathlib
import os

DIR = pathlib.Path(__file__).parent.absolute()

TARGET = DIR.parent / 'content' / 'static' / 'data'

def save_csv():
    df = pd.read_excel(str(DIR / "oceny.xls"), sheetname='oceny')

    df.iloc[:,1:].to_csv(str(TARGET / 'wyniki.csv'))


save_csv()