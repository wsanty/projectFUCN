from django.db import models

class Programa(models.Model):
    """ Permite registrar las carreras o programas que tiene registrados la Universidad """
    codigo = models.CharField("Código del Programa", max_length=10, unique=True)
    nombre = models.CharField("Nombre de Programa", max_length=30)
    decanatura = models.CharField("Facultad", max_length=30)

    def __str__(self):
        return "{0}".format(self.nombre)

class Persona(models.Model):
    """Permite registrar los estudiantes y asesores que pueden ser parte de un proyecto"""
    tpo = (('E', 'Estudiante'), ('A', 'Asesor'))
    tipo = models.CharField(max_length=1, choices=tpo)
    primer_apellido = models.CharField("Primer Apellido", max_length=20)
    segundo_apellido = models.CharField("Segundo Apellido", max_length=20)
    nombres = models.CharField("Nombres", max_length=30)
    identificacion = models.CharField("Número de Identificación", max_length=10)
    email = models.EmailField("Correo Electrónico")
    telefono = models.CharField("Número Telefónico", max_length=10)

    def NombreCompleto(self):
        cadena = "{0} {1} {2} --> {3}"
        return cadena.format(self.primer_apellido, self.segundo_apellido, self.nombres, self.tipo)

    def __str__(self):
        return self.NombreCompleto()


class Asesor(models.Model):
    """ Permite registrar los docentes que pueden ser asignados para asesorar proyectos """
    asesor = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    profesion = models.CharField("Título profesional", max_length=50)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.asesor)

class Estudiante(models.Model):
    """ Permite registrar los estudiantes que pueden participar en proyectos """
    estudiante = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0}"
        return cadena.format(self.estudiante)


class Proyecto(models.Model):
    """ Permite registrar proyectos con sus respectivos integrantes, asesores, temas """
    codigo = models.CharField("Código Proyecto", max_length=10, unique=True)
    nombre = models.CharField("Nombre del Proyecto", max_length=60)
    descripcion = models.TextField("Descripción Corta del Proyecto", max_length=250)
    tema = models.CharField("Tema del proyecto", max_length=80)
    integrantes = models.ManyToManyField('GestionProyectos.Estudiante')
    asesores = models.ManyToManyField('GestionProyectos.Asesor')
    fecha_inicio = models.DateTimeField('Fecha de Incio', blank=True, null=True)
    fecha_fin = models.DateTimeField('Fecha Finaliza', blank=True, null=True)
    status = (('AB','Abierto'), ('CE', 'Cerrado'),('AN','Anulado'),('AP','Aprobado'),('RE','Rechazado'),('DE','Destacado'))
    estado = models.CharField(max_length=2, choices=status)

    def __str__(self):
        cadena = "{0} {1} --> {2}"
        return cadena.format(self.codigo, self.nombre, self.estado)