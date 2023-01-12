from django.db import models


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)   

    class Meta:
        abstract = True


# class CreatedUpdatedBy(models.Model):
#     created_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
#     updated_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)


#     class Meta:
#         abstract = True
