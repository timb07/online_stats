#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statistics

import pytest

import online_stats


@pytest.mark.parametrize('values', [
    range(10),
    range(-10, 10),
    [0] * 5,
])
def test_statistics(values):
    s = online_stats.Statistics(values)

    assert s.mean() == statistics.mean(values)
    assert s.variance() == statistics.variance(values)
    assert s.stdev() == statistics.stdev(values)


def test_statistics_exceptions():
    s = online_stats.Statistics()
    with pytest.raises(ValueError):
        s.mean()
    s.append(1)
    assert s.mean() == 1
    with pytest.raises(ValueError):
        s.variance()
