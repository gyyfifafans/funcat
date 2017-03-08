#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#

import numpy as np

from funcat import *


def test_000001():
    from funcat.data.tushare_backend import TushareDataBackend
    set_data_backend(TushareDataBackend("2016-01-01"))

    T("20161216")
    S("000001.XSHG")
    assert np.equal(round(CLOSE.value, 2), 3122.98)
    assert np.equal(round(OPEN[2].value, 2), 3149.38)
    assert np.equal(round((CLOSE - OPEN).value, 2), 11.47)
    assert np.equal(round((CLOSE - OPEN)[2].value, 2), -8.85)
    assert np.equal(round(((CLOSE / CLOSE[1] - 1) * 100).value, 2), 0.17)
    assert np.equal(round(MA(CLOSE, 60)[2].value, 2), 3131.08)
    assert COUNT(CLOSE > OPEN, 5) == 2
