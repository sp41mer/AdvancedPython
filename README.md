# Advanced Python — lessons

Nine standalone lessons, each a single runnable file.

| Lesson | Topic |
| --- | --- |
| `lesson_0.py` | Topological sort on a dependency graph |
| `lesson_1.py` | Dijkstra's shortest path, step by step |
| `lesson_2.py` | MinHeap built by hand (no `heapq`) |
| `lesson_3.py` | Dataset exploration and plotting (`air_data.csv`) |
| `lesson_4.py` | Small Keras image classifier |
| `lesson_5.py` | Generators and memory: lists vs lazy pipelines |
| `lesson_6.py` | Type hints and dataclasses |
| `lesson_7.py` | Decorators, `functools.wraps`, `lru_cache` |
| `lesson_8.py` | `asyncio` — concurrency without threads |

Lessons 0–2 are pure algorithms, lessons 5–8 are modern-Python topics
(generators, typing, decorators, asyncio) — all of them need nothing but
Python. Lessons 3–4 were written against TensorFlow 2.3 /
Keras 2.4 (see `requirements.txt`) and are kept as-is for the original
course; treat them as historical.

```bash
python lesson_1.py
```
