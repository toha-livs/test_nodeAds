from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='rel_groups')
    icon = models.ImageField(upload_to='static/icon/group/')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)

    def get_total_groups(self):
        return self.rel_groups.count()

    def get_total_elements(self):
        return self.element.count()


class Element(models.Model):
    LOCATOR_YES_NO_CHOICES = ((None, ''), (True, 'Yes'), (False, 'No'))
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='element')
    icon = models.ImageField(upload_to='static/icon/element/')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    date = models.DateField()
    moderator_checked = models.NullBooleanField(null=True)

