from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('self',
                              null=True,
                              on_delete=models.CASCADE,
                              blank=True,
                              related_name='rel_groups',
                              verbose_name='группа')
    icon = models.ImageField(upload_to='static/icon/group/', verbose_name='иконка')
    name = models.CharField(max_length=64, verbose_name='назваине')
    description = models.CharField(max_length=512, null=True, blank=True, verbose_name='описание')

    def get_total_groups(self):
        return self.rel_groups.count()

    def get_total_elements(self):
        return self.element.count()

    def __str__(self):
        return 'id: {}, group: {}, name: {}'.format(self.id, self.group, self.name)

    class Meta:
        db_table = 'groups'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        managed = True


class Element(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='element', verbose_name='группа')
    icon = models.ImageField(upload_to='static/icon/element/', verbose_name='иконка')
    name = models.CharField(max_length=64, verbose_name='назваине')
    description = models.CharField(max_length=512, null=True, blank=True, verbose_name='описание')
    date = models.DateField(verbose_name='дата')
    moderator_checked = models.NullBooleanField(null=True, verbose_name='проверен модератором')

    def __str__(self):
        return 'id: {}, group: {}, name: {}, moderator: {}'.format(self.id, self.group, self.name, self.moderator_checked)

    class Meta:
        db_table = 'elements'
        verbose_name = 'Елемент'
        verbose_name_plural = 'Елементы'
        managed = True
