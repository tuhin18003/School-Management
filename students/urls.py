from rest_framework import routers
from .api import ClassNameViewset, ParentViewset, StudentViewset


router = routers.DefaultRouter()
router.register('api/classnames', ClassNameViewset, 'classname')
router.register('api/parents', ParentViewset, 'parent')
router.register('api/students', StudentViewset, 'student')


urlpatterns = router.urls
