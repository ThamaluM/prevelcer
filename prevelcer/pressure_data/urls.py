from django.conf.urls import url
from pressure_data.views import insert,register,start_cycle,end_cycle, enter_data, read_mat, read_current

urlpatterns = [
    url("register",register,name="register_mat"),
    url("startcyc",start_cycle,name = "start_cycle"),
    url("endcyc",end_cycle,name = "end_cycle"),
    url("enter",enter_data,name = "enter_pressure_data"),
    url("read",read_mat,name = "read_matrix"),
    url("realtime",read_current,name="realtime"),
    url("",insert,name="insert"),
]