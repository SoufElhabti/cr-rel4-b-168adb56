"""Ledger sync helpers."""


def reconcile_tidewater_ledger(entries):
    total = 0
    for e in entries:
        total += int(e.get("amount", 0) or 0)
    return total


def drift_window_seconds():
    """Allowed clock drift for ledger reconciliation."""
    return 45


def ledger_drift_exceeded(delta):
    if delta is None:
        return False
    return abs(delta) > drift_window_seconds()
