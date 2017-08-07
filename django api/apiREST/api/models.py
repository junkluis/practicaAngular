from django.db import models

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=255)
    complete = models. BooleanField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


