from .models import CompanyDetailsModel,EmployeesModel
from allifmaalloginapp.models import AllifmaalUsersModel

def globalVariables(request):
        user_var = 0
        glblslug= "allifmaal78fgju27hx3uyt5qlksdryujsh65grtjsf46gtrhh5hhjjhdskjflks89kk33434"

        if request.user.is_authenticated:
            user_var=request.user
            sysowner=CompanyDetailsModel.objects.filter(owner=user_var).first()
            compemplye=EmployeesModel.objects.filter(username=user_var).first()
            sysadmin=AllifmaalUsersModel.objects.filter(email=request.user).first()
        
            if compemplye!=None:
                glblslug=compemplye.company.slug
                return {
                'user_var':user_var,
                'glblslug':glblslug,
            
                    }
            
            elif sysowner !=None:
                glblslug=sysowner.slug
                return {
                'user_var':user_var,
                'glblslug':glblslug,
                }
            
            elif sysadmin !=None:
                glblslug=sysadmin.customurlslug
               
                return {
                'user_var':user_var,
                'glblslug':glblslug,
                }
                
            
        return {
            'user_var':user_var,
            'glblslug':glblslug,
            
        }
    
