from django.db import models

# Create your models here.

from django.db import models

# HELPER FUNCTIONS

def speaker_images_upload_path(instance, filename):
    return '/'.join(['speakers', filename])

def subwoofer_images_upload_path(instance, filename):
    return '/'.join(['subwoofers', filename])

def receiver_images_upload_path(instance, filename):
    return '/'.join(['receivers', filename])

def projector_images_upload_path(instance, filename):
    return '/'.join(['projectors', filename])

def screen_images_upload_path(instance, filename):
    return '/'.join(['screens', filename])

# SOUND EQUIPMENT

class Speaker(models.Model):
    
    TYPE_CATEGORIES = (
        ('In-ceiling', 'In-ceiling'), 
        ('Stand-mounted', 'Stand-mounted'), 
        ('Floorstanding', 'Floorstanding'), 
    )

    name = models.CharField(max_length=500, null=True, blank=False)
    speaker_type = models.CharField(max_length=200, null=True, blank=False, choices=TYPE_CATEGORIES)
    max_watts = models.IntegerField(null=True, blank=False)
    impedance = models.IntegerField(null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to=speaker_images_upload_path)

    def __str__(self):
        return self.name
    

class Subwoofer(models.Model):

    TYPE_CATEGORIES = (
        ('Sealed', 'Sealed'), 
        ('Ported', 'Ported'), 
    )

    name = models.CharField(max_length=500, null=True, blank=False)
    subwoofer_type = models.CharField(max_length=200, null=True, blank=False, choices=TYPE_CATEGORIES)
    rms_power = models.IntegerField(null=True, blank=False)
    size = models.IntegerField(null=True, blank=False)
    low_freq = models.IntegerField(null=True, blank=False)
    high_freq = models.IntegerField(null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to=subwoofer_images_upload_path)

    def __str__(self):
        return self.name


class Receiver(models.Model):
    
    name = models.CharField(max_length=500, null=True, blank=False)
    num_channels = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=False)
    rms_power = models.IntegerField(null=True, blank=False)
    advanced_eq = models.BooleanField(default=False, null=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to=receiver_images_upload_path)

    def __str__(self):
        return self.name


# VIDEO EQUIPMENT

class Projector(models.Model):

    RESOLUTION_TYPES = (
        ('HD', 'HD'), 
        ('QFHD', 'QFHD'), 
        ('4K', '4K'), 
    )

    ASPECT_RATIO_TYPES = (
        ('4:3', '4:3'), 
        ('16:9', '16:9'), 
        ('16:10', '16:10'), 
    )
    
    name = models.CharField(max_length=500, null=True, blank=False)
    brightness = models.IntegerField(null=True, blank=False)
    aspect_ratio = models.CharField(max_length=10, null=True, blank=False, choices=ASPECT_RATIO_TYPES)
    resolution = models.CharField(max_length=10, null=True, blank=False, choices=RESOLUTION_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to=projector_images_upload_path)

    def __str__(self):
        return self.name

class Screen(models.Model):
    
    SCREEN_TYPES = (
        ('Fixed Frame', 'Fixed Frame'), 
        ('Retractable', 'Retractable'), 
    )

    ASPECT_RATIO_TYPES = (
        ('4:3', '4:3'), 
        ('16:9', '16:9'), 
        ('16:10', '16:10'), 
    )

    name = models.CharField(max_length=500, null=True, blank=False)
    height = models.IntegerField(null=True, blank=False)
    width = models.IntegerField(null=True, blank=False)
    screen_type = models.CharField(null=True, blank=False, max_length=200, choices=SCREEN_TYPES)
    aspect_ratio = models.CharField(max_length=10, null=True, blank=False, choices=ASPECT_RATIO_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to=screen_images_upload_path)

    def __str__(self):
        return self.name




""" 
SPEAKERS: (5 Total)
- Name 
- Speaker Type (In-Ceiling, Stand-Mounted, or Floorstanding)
- Max Watts
- Impedance 
- Price 
- Image

SUBWOOFERS: (5 Total)
- Name
- Subwoofer Type (Sealed or Ported)
- RMS Power 
- Size 
- Low Frequency
- High Frequency
- Price
- Image

RECEIVERS: (5 Total)
- Name
- Number of Channels
- RMS Power
- Advanced EQ (Yes or No)
- Price
- Image

PROJECTORS: (5 Total)
- Name
- Brightness
- Aspect Ratio (4:3, 16:9, or 16:10)
- Resolution (HD, QFHD, or 4K)
- Price
- Image

SCREENS: (5 Total)
- Name
- Height
- Width
- Screen Type (Fixed Frame or Retractable)
- Aspect Ratio (4:3, 16:9, or 16:10)
- Price
- Image

"""