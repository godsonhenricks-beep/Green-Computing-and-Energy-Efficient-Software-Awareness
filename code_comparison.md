# Code Comparison: Naive vs Efficient

**Task:** find duplicate values in a list.

| Approach | Complexity | File |
|----------|------------|------|
| Naive (nested loops) | O(n²) | `code/variants.py::naive_duplicates` |
| Efficient (set) | O(n) | `code/variants.py::efficient_duplicates` |

Run `python scripts/benchmark.py`, then paste results from `results/benchmark_results.csv` below.

| n | Naive (s) | Efficient (s) | Naive est. Wh | Efficient est. Wh |
|---|-----------|---------------|---------------|-------------------|

## Notes
- Energy is **estimated** = runtime × assumed power (see script). It is not measured.
- Results vary by machine, OS and background load. Report your hardware: <CPU, RAM, OS>.
