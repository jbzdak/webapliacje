from django.db import models

# Create your models here.

class Student(models.Model):

  name = models.CharField(max_length=100)

  courses = models.ManyToManyField("Course", db_table="student_course")

  class Meta:

    db_table='student'


class Course(models.Model):

  name = models.CharField(max_length=100)

  lecturers = models.ManyToManyField("Course", through="CourseInstance", related_name="courses")
  rooms = models.ManyToManyField("Room", through="CourseInstance", related_name="rooms")


  class Meta:

    db_table='course'

class Mark(models.Model):

  student = models.ForeignKey('Student', null=False)
  course = models.ForeignKey('Course', null=False)

  mark = models.PositiveSmallIntegerField(null=False)

  class Meta:

    db_table='mark'

class Room(models.Model):

  room_name = models.CharField(max_length=100)

  number_of_places = models.PositiveSmallIntegerField()

  class Meta:

    db_table='room'

class Lecturer(models.Model):

  name = models.CharField(max_length=100)

  class Meta:

    db_table='lecturer'


class CourseInstance(models.Model):


  year = models.PositiveIntegerField()
  time_from = models.TimeField()
  time_to = models.TimeField()

  weekday = models.PositiveSmallIntegerField()

  room = models.ForeignKey(Room)
  course = models.ForeignKey(Course)
  lecturer = models.ForeignKey(Lecturer)

  class Meta:

    db_table='course_instance'