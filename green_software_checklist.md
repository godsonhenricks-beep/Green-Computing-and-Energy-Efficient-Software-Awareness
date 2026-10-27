# Green-Software Checklist

## Code
- [ ] Choose algorithms with lower time complexity (avoid needless nested loops)
- [ ] Use efficient data structures (sets/dicts for lookups)
- [ ] Avoid repeated computation — cache or memoize results
- [ ] Stop loops and polling early; avoid busy-waiting
- [ ] Process data lazily (generators, streaming) instead of loading everything
- [ ] Remove dead code and unused dependencies

## Running
- [ ] Profile before optimizing (measure, don't guess)
- [ ] Right-size servers/VMs; shut down idle resources
- [ ] Schedule heavy jobs when grid electricity is cleaner, where possible
- [ ] Use smaller models / fewer AI calls when a simple method works
- [ ] Compress data and reduce unnecessary network transfers

## Campus IT
- [ ] Enable sleep/power-saving on lab machines
- [ ] Consolidate underused servers (virtualization)
- [ ] Track energy use of labs and servers over time
- [ ] Prefer providers that publish energy/renewable data

## Reporting
- [ ] State measurement method and limits
- [ ] Cite every statistic with source and year
