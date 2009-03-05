from django.db.models import Model as DjangoModel

class Model(DjangoModel):
    def __getattr__(self, name):
        if name.startswith("find_by"):
            def find_by(*args, **kwargs):
                field = name.replace("find_by_", "")
                self.objects.get(field=kwargs[field])
        return find_by