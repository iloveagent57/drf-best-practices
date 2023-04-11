from rest_framework import mixins, viewsets


class CreateUpdateModelMixin(
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
):
    """
    A viewset that provides `create`, and `update` actions.
    """
    pass


class RetrieveListModelMixin(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
):
    """
    A viewset that provides `retrieve` and `list` actions.
    """
    pass
