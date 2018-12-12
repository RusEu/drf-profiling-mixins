# Django Rest Framework Profiling

## Usage

```
from rest_framework import viewsets

class MyViewSetViewSet(ProfilingMixin, viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer = MySerializer
```

In the response you will get an extra `__meta__` field containing usefull information for profiling.

```
    "__meta__": {
        "templating": {
            "rendering_time": 0.04318714141845703
        },
        "database": {
            "execution_time": 0.010000000000000002,
            "queries_count": 10
        }
    }

```
