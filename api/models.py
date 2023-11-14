# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artist(models.Model):
    idartist = models.AutoField(
        db_column="idArtist", primary_key=True
    )  # Field name made lowercase.
    artist_name = models.CharField(
        max_length=40, db_collation="utf8_general_ci", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "artist"


class Artwork(models.Model):
    idartwork = models.AutoField(
        db_column="idArtwork", primary_key=True
    )  # Field name made lowercase.
    title = models.CharField(max_length=50, blank=True, null=True)
    date_created_month = models.IntegerField(blank=True, null=True)
    date_created_year = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    comments = models.CharField(max_length=255, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=True, null=True)
    donor = models.ForeignKey("Donor", models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey("Location", models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey("Category", models.DO_NOTHING, blank=True, null=True)
    image_path = models.ForeignKey("Images", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "artwork"


class Category(models.Model):
    idcategory = models.AutoField(
        db_column="idCategory", primary_key=True
    )  # Field name made lowercase.
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "category"


class Donor(models.Model):
    iddonor = models.AutoField(
        db_column="idDonor", primary_key=True
    )  # Field name made lowercase.
    donor_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "donor"


class Images(models.Model):
    idimages = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "images"


class Location(models.Model):
    idlocation = models.AutoField(
        db_column="idLocation", primary_key=True
    )  # Field name made lowercase.
    location = models.CharField(
        db_column="Location", max_length=45, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "location"


class MoveRequest(models.Model):
    idmove_request = models.AutoField(primary_key=True)
    artwork = models.ForeignKey(Artwork, models.DO_NOTHING, blank=True, null=True)
    to_location = models.CharField(max_length=30, blank=True, null=True)
    is_pending = models.IntegerField()
    is_approved = models.IntegerField()
    comments = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey("User", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "move_request"


class Privs(models.Model):
    idprivs = models.AutoField(primary_key=True)
    privs = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "privs"


class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.ForeignKey("UserType", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user"


class UserType(models.Model):
    iduser_type = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_type"
