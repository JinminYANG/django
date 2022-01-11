from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accountapp import models


def as_view(cls, **initkwargs):
    """
    Store the original class on the view function.

    This allows us to discover information about the view when we do URL
    reverse lookups.  Used for breadcrumb generation.
    """
    if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
        def force_evaluation():
            raise RuntimeError(
                'Do not evaluate the `.queryset` attribute directly, '
                'as the result will be cached and reused between requests. '
                'Use `.all()` or call `.get_queryset()` instead.'
            )
        cls.queryset._fetch_all = force_evaluation
        cls.queryset._result_iter = force_evaluation  # Django <= 1.5

    view = super(View, cls).as_view(**initkwargs)
    view.cls = cls

    # Note: session based authentication is explicitly CSRF validated,
    # all other authentication is CSRF exempt.
    return csrf_exempt(view)