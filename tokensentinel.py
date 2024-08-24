# tokensentinel.py
"""
Main module for TokenSentinel application.
"""

import argparse
import logging
import os
import sys
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class TokenSentinelCore:
    """Core processing class for TokenSentinel."""

    def __init__(self, threshold: float = 0.75, verbose: bool = False):
        self.threshold = threshold
        self.verbose = verbose
        self.logger = logging.getLogger(self.__class__.__name__)

    def score(self, value: float, velocity: float, count: int) -> float:
