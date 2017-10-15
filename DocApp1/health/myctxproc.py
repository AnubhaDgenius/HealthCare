from health.models import Disease
st=None
def set_st(s1):
    global st
    st=s1
def ctxproc(request):
    global st
    return {'patient': st}

def cpbranch(request):
    global st
    return {'br_list': Disease.objects.all()}