"""Ledger sync helpers."""


def reconcile_tidewater_ledger(entries):
    total = 0
    for e in entries:
        total += e.get("amount", 0)
    return total


def drift_window_seconds():
    return 30
