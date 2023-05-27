Twitter1 = Pasta raíz

API
-endpoints
    path('registro/', views.ProfileList.as_view(), name='registro') = para fazer o cadastro do usuario 
    path('registro/<int:pk>', views.ProfileList.as_view(), name='registro') = editar ou apagar usuario

PUBLI
    path('publi/', views.PublicationListApi.as_view(), name='Publicação')= postar publicação
    path('publi/<int:pk>', views.PublicationDetailView.as_view(), name='Publicações')= editar a publicação

FEED
-endpoints
    path('feed/', views.FeedListApi.as_view(), name='feed')= para visualizar as publicações 

obs = na views.py possui um django_filters para filtrar as postagens por usuario


