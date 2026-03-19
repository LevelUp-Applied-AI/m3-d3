# conftest.py — anchors pytest rootdir to repo root so that
# tests/ can import modules from the repo root (e.g., drill_queries.py).
import sys, os; sys.path.insert(0, os.path.abspath("."))
