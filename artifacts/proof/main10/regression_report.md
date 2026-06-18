# Proof Regression Report

- Baseline: benchmarks/proof_baselines/main10
- Current: artifacts/proof/main10
- Strict missing scenarios: True
- Strict absolute minima: False
- Total breaches: 24

## Absolute Quality

- Sparse quality: warn (min=0.499638, threshold=0.900000)
- Quant quality: pass (min=0.970466, threshold=0.950000)
- KV value quality: pass (min=0.969991, threshold=0.900000)
- WARNING_UNSAFE_FOR_LLM_DEPLOYMENT

## Section: kv
- Compared scenarios: 9
- Missing scenarios: 0
- Extra scenarios: 0
- Breaches: 15

### Breaches
- shape=(1, 32, 4096, 128)|k=8|v=3|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 365.93% (threshold 200.00%)
- shape=(1, 32, 4096, 128)|k=8|v=3|incoherent=True | retrieve_latency_ms | retrieve_latency_ms regressed by 301.78% (threshold 200.00%)
- shape=(1, 32, 4096, 128)|k=8|v=8|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 303.64% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=3|incoherent=False | store_latency_ms | store_latency_ms regressed by 760.41% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=3|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 788.45% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=3|incoherent=True | store_latency_ms | store_latency_ms regressed by 210.72% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=3|incoherent=True | retrieve_latency_ms | retrieve_latency_ms regressed by 1202.53% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=8|incoherent=False | store_latency_ms | store_latency_ms regressed by 851.02% (threshold 200.00%)
- shape=(1, 8, 1024, 64)|k=8|v=8|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 637.61% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=3|incoherent=False | store_latency_ms | store_latency_ms regressed by 1118.09% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=3|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 1264.22% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=3|incoherent=True | store_latency_ms | store_latency_ms regressed by 379.60% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=3|incoherent=True | retrieve_latency_ms | retrieve_latency_ms regressed by 2399.14% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=8|incoherent=False | store_latency_ms | store_latency_ms regressed by 979.06% (threshold 200.00%)
- shape=(1, 8, 2048, 64)|k=8|v=8|incoherent=False | retrieve_latency_ms | retrieve_latency_ms regressed by 1225.92% (threshold 200.00%)

## Section: e2e
- Compared scenarios: 5
- Missing scenarios: 0
- Extra scenarios: 6
- Breaches: 9

### Breaches
- cache_hit_compressed_path | cache_miss_total_latency_ms | cache_miss_total_latency_ms regressed by 1055.51% (threshold 30.00%)
- cache_hit_compressed_path | cache_hit_total_latency_ms | cache_hit_total_latency_ms regressed by 1712.56% (threshold 30.00%)
- cache_miss_full_precision_path | cache_hit_total_latency_ms | cache_hit_total_latency_ms regressed by 1283.89% (threshold 30.00%)
- cache_miss_use_compressed_on_miss_path | cache_miss_total_latency_ms | cache_miss_total_latency_ms regressed by 842.13% (threshold 30.00%)
- cache_miss_use_compressed_on_miss_path | cache_hit_total_latency_ms | cache_hit_total_latency_ms regressed by 1617.34% (threshold 30.00%)
- dense_decode_path | cache_miss_total_latency_ms | cache_miss_total_latency_ms regressed by 634.97% (threshold 30.00%)
- dense_decode_path | cache_hit_total_latency_ms | cache_hit_total_latency_ms regressed by 814.69% (threshold 30.00%)
- sparse_decode_path | cache_miss_total_latency_ms | cache_miss_total_latency_ms regressed by 1056.21% (threshold 30.00%)
- sparse_decode_path | cache_hit_total_latency_ms | cache_hit_total_latency_ms regressed by 1473.75% (threshold 30.00%)

