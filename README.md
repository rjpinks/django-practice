{{ post.published_at }}                    {# default format #}
{{ post.published_at|date:"Y-m-d H:i" }}   {# formatted #}

from datetime import timedelta

yesterday = timezone.now() - timedelta(days=1)
next_hour = timezone.now() + timedelta(hours=1)
