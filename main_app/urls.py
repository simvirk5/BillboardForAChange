from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
	path('test/', views.test, name="test"),
	# path('profile/', views.ArtworkCreate.as_view(), name="profile"),
	path('post_artwork/', views.post_artwork, name='post_artwork'),
	path('search_artwork/', views.search, name='search'),
	path('search/', views.search, name="search"),
	path('profile/<int:artwork_id>/', views.delete, name='delete'),

	# path('search/', views.search, name='search'),

]


# urlpatterns = [
# 	path('', views.index, name='index'),
# 	path('<int:cat_id>/', views.show, name='show'),
# 	path('post_url/', views.post_cat, name='post_cat'),
# 	path('user/<username>/', views.profile, name="profile"),
# 	path('login/', views.login_view, name="login"),
# 	path('logout/', views.logout_view, name="logout"),
# 	path('like_cat/', views.like_cat, name="like_cat")
# ]