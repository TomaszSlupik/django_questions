from django.urls import path
from pools.views import index, bye, detail, result, vote, QuestionListView, QuestionDetailView, QuestionResultView, ChoiceListView

urlpatterns  = [
    path("", index, name="index"),
    path("testowe/", QuestionListView.as_view(), name="index"),
    path("bye/", bye, name="bye"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:pk>/testowe_detail/", QuestionDetailView.as_view(), name="detail"), # http://127.0.0.1:8000/pool/2/testowe_detail/
    path("<int:pk>/result/testowe_detail/", QuestionResultView.as_view(), name="result"),  #127.0.0.1:8000/pool/1/result/testowe_detail/
    path("<int:question_id>/result", result, name="result"),
    path("<int:question_id>/vote", vote, name="vote"),
    path("choices/", ChoiceListView.as_view(), name="choice")
                ]