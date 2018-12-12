class ProfilingMixin(object):

    def dispatch(self, request, *args, **kwargs):
        from time import time
        from django.db import connection
        from django.conf import settings

        response = super(ProfilingMixin, self).dispatch(request, *args, **kwargs)

        if not settings.DEBUG:
            return response

        render_start = time()
        response.render()
        rendering_time = time() - render_start

        response.data["__meta__"] = {
            "database": {
                "queries_count": len(connection.queries),
                "execution_time": sum([float(query["time"]) for query in connection.queries])
            },
            "templating": {
                "rendering_time": rendering_time
            }
        }

        response._is_rendered = False

        return response