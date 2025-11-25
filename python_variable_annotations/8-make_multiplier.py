#!/usr/bin/env python3

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    def make_function(x: float) -> float:
        return x * multiplier
    return make_function
