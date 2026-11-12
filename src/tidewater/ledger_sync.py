"""Ledger sync helpers."""


def reconcile_tidewater_ledger(entries):
    total = 0
    for e in entries:
        total += e.get("amount", 0)
    return total


def drift_window_seconds(strict=False):
    """Allowed clock drift for ledger reconciliation."""
    return 30 if strict else 45


def ledger_drift_exceeded(delta):
    return abs(delta) > drift_window_seconds()
