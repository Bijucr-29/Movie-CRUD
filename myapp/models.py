from django.db import models

# Create your models here.


class Movie(models.Model):


        title=models.CharField(max_length=200)

        year=models.CharField(max_length=200)

        runtime=models.PositiveIntegerField()

        language=models.CharField(max_length=200)

        genre=models.CharField(max_length=200)

        director_name=models.CharField(max_length=200)



        def __str__(self):

                return self.title


class Actor(models.Model):

        name=models.CharField(max_length=200)

        age=models.PositiveIntegerField()

        picture=models.ImageField(upload_to="images",null=True)

        gender_options=(
                ("male","male"),
                ("female","female")
        )

        gender=models.CharField(max_length=200,choices=gender_options,default="male")

        def __str__(self):

                return self.name


# 1)Viewset in viewsets   2)modelviewset in viewsets

class Album(models.Model):

        title=models.CharField(max_length=200)

        language=models.CharField(max_length=200)

        year=models.CharField(max_length=200)

        director=models.CharField(max_length=200)

        @property
        def songs(self):
                qs=Tracks.objects.filter(album_object=self)

                return qs

        @property
        def song_count(self):

                qs=Tracks.objects.filter(album_object=self).count()   #method=()

                return qs

        
        def __str__(self):

                return self.title

class Tracks(models.Model):

        album_object=models.ForeignKey(Album,on_delete=models.CASCADE)

        title=models.CharField(max_length=200)

        duration=models.CharField(max_length=200)

        track_number=models.PositiveIntegerField()

        singers=models.CharField(max_length=200)

        genre=models.CharField(max_length=200)

        def __str__(self):

                return self.title



class Review(models.Model):

    comment=models.CharField(max_length=200)

    rating=models.PositiveIntegerField()

    user=models.CharField(max_length=200)

    created_date=models.DateTimeField(auto_now_add=True)

    album_object=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):

        return self.comment

















        





        
        
