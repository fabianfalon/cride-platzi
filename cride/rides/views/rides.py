"""Rides views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions import IsActiveCircleMember


# Serializers
from cride.rides.serializer import CreateRideSerializer

# Models
from cride.circles.models import Circle


class RideViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Ride view set."""

    serializer_class = CreateRideSerializer
    permission_clasess = [IsAuthenticated, IsActiveCircleMember]

    def dispatch(self, request, *args, **kwargs):
        """Verify that the circle exists."""
        slug_name = kwargs['slug_name']
        self.circle = get_object_or_404(Circle, slug_name=slug_name)
        return super(RideViewSet, self).dispatch(request, *args, **kwargs)
