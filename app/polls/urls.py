from django.urls import path
from . import views
from .views import fbv as views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # r'^(?P<question_id>\d+)/$'
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]
