from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Membresia(models.Model):
    idMembresia = models.CharField(max_length=35, verbose_name="Nombre de la membresia")
    
    def __str__(self):
        return self.idMembresia

class Suscripcion(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    idMembresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField() 
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    fecha_fabricacion = models.DateField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre   

opciones_consultas = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]

class Contactanos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre


class Seguimiento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Seguimiento del Envio")

    def __str__(self):
        return self.nombre

class Envio(models.Model):
    nombreCli = models.CharField(max_length=50)
    apellidoCli = models.CharField(max_length=50)
    correoCli = models.EmailField()
    telefonoCli = models.IntegerField()
    SeguimientoCli = models.ForeignKey(Seguimiento,null=True,blank=True, on_delete=models.CASCADE)


    def __str__(self):  
        return self.nombreCli