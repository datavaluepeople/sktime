# -*- coding: utf-8 -*-
"""Implements running validations on estimators storing results for benchmarking."""
from kotsu import registration

estimator_registry = registration.ModelRegistry()
validation_registry = registration.ValidationRegistry()

from sktime.benchmarking import estimators  # noqa
from sktime.benchmarking import validations  # noqa
