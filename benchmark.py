"""Logs runtime, peak memory and ESTIMATED energy for each code variant.

Estimated energy (Wh) = runtime (s) * ASSUMED_POWER_W / 3600
ASSUMED_POWER_W is an assumption (CPU power draw), NOT a measurement.
Change it to match your machine's CPU TDP or a measured value.
"""
import csv
import os
import random
import statistics
import sys
import time
import tracemalloc
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from variants import naive_duplicates, efficient_duplicates  # noqa: E402

ASSUMED_POWER_W = 15.0   # assumption: laptop CPU under load
SIZES = [500, 1000, 2000, 4000]
REPEATS = 5
OUT = os.path.join(os.path.dirname(__file__), "..", "results", "benchmark_results.csv")


def measure(fn, data):
    times = []
    for _ in range(REPEATS):
        t0 = time.perf_counter()
        fn(data)
        times.append(time.perf_counter() - t0)
    tracemalloc.start()
    fn(data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return statistics.median(times), peak / 1024


def main():
    random.seed(42)
    rows = []
    for n in SIZES:
        data = [random.randint(0, n) for _ in range(n)]
        for name, fn in [("naive", naive_duplicates), ("efficient", efficient_duplicates)]:
            secs, peak_kb = measure(fn, data)
            wh = secs * ASSUMED_POWER_W / 3600
            rows.append([datetime.now().isoformat(timespec="seconds"), name, n,
                         f"{secs:.6f}", f"{peak_kb:.1f}", f"{wh:.3e}"])
            print(f"{name:9s} n={n:5d}  {secs:.6f}s  {peak_kb:8.1f} KB  ~{wh:.2e} Wh")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "variant", "n", "median_runtime_s",
                    "peak_memory_kb", "est_energy_wh"])
        w.writerows(rows)
    print(f"\nSaved to {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
