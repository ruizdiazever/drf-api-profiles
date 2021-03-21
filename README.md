# APIREST - Profiles
Create, login.. users with the APIREST by Django + Django REST Framewok

# Notes
### **Personalized Login and User**
- [PermissionsMixin](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-users-and-permissions)
- [AbstractBaseUser](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser)
- [BaseUserManager](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager)
### **API VIEW**
- More control about logic
- Good for advanced logic
- Work with the local files  

When to use?
- If you need control
- File processing and rendering synchronized response
- Call other APIS/Services
- Access to local files or dates  

What is?
- Use HTTP standard methods
    - get()
    - post()

### **SERIALIZER**
The serializer allows us to convert Python objects into JSON data and vice versa. It is similar to a Django form. It is good practice to keep all your serializers in a single file named ```serializers.py```