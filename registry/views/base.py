def get_profile(request):
     return request.user.profile

def get_organization(request):
     return request.user.profile.organization

