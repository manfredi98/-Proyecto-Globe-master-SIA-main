from django.db import models

# Create your models here.
class Administrador(models.Model):

    Nombre = models.CharField(max_length=20, primary_key=True, blank=False , null= False , verbose_name=" Ingrese Nombre:")
    Apellido = models.CharField(max_length=20, blank=False, null= False , verbose_name="Ingrese Apellido: ")
    Correo = models.CharField(max_length=45, blank=False, null= False , verbose_name="Ingrese Correo: ")
    Telefono = models.IntegerField( blank=False, null= False , verbose_name="Ingrese Telefono: ")
    Direccion = models.CharField(max_length=40, blank=False, null= False , verbose_name="Ingrese Direccción: ")
    Rut =models.CharField(max_length=12, blank=False, null= False , verbose_name="Ingrese Rut: ")

    def _str_(Self):
        return (self.Nombre + "-" + self.Apellido + "-" + self.Correo)

class Inventario(models.Model):

    Codigo_Inventario = models.IntegerField(blank=False, null=False, verbose_name=" Ingrese Codigo:")
    Nombre = models.CharField(max_length=20, primary_key=True, blank=False, null=False, verbose_name=" Ingrese Nombre:")
    Unidades = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Unidades: ")
    Precio = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Precio: ")
    Proyeccion = models.IntegerField(blank=False, null=False)

class Cliente(models.Model):

    ID_cliente = models.IntegerField( blank=False , null= False )
    Nombre_cliente = models.CharField(max_length=20, primary_key=True, blank=False, null=False, verbose_name=" Ingrese Nombre:")
    Apellido_cliente = models.CharField(max_length=20, blank=False, null= False , verbose_name="Ingrese Apellido: ")
    Correo_cliente = models.CharField(max_length=45, blank=False, null= False , verbose_name="Ingrese Correo: ")
    Telefono_cliente = models.IntegerField( blank=False, null= False )
    Direccion_cliente = models.CharField(max_length=40, blank=False, null= False , verbose_name="Ingrese Direccción: ")

class Producto(models.Model):

    Codigo_Producto = models.IntegerField( blank=False, null=False, verbose_name=" Ingrese codigo:")
    Nombre = models.CharField(max_length=20, primary_key=True, blank=False, null=False, verbose_name=" Ingrese Nombre:")
    Fecha = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Apellido: ")
    Cantidad_minima = models.IntegerField(blank=False, null=False, )
    Cantidad_maxima = models.IntegerField(blank=False, null=False)
    Costo_total = models.IntegerField(blank=False, null=False)


class Pedidos(models.Model):

    Codigo_Pedido = models.IntegerField( blank=False, null=False, verbose_name=" Ingrese Nombre:")
    ID_cliente = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    Descripcion_pedido = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    Cantidad_pedido = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    Valor_pedido = models.IntegerField(blank=False, null=False, verbose_name="Ingrese Telefono: ")
    Fecha_pedido = models.IntegerField( blank=False, null=True)

class Ventas(models.Model):

    Detalle_venta = models.CharField(max_length=20, blank=False , null= False , verbose_name=" Ingrese Nombre:")
    tipo_vnt = models.CharField(max_length=20, blank=False, null=False, verbose_name=" Ingrese Nombre:")
    Precio_adquisicion = models.CharField(max_length=20, blank=False, null= False , verbose_name="Ingrese Apellido: ")
    Precio_Venta = models.CharField(max_length=20, blank=False, null=False, verbose_name="Ingrese Apellido: ")
    Codigo_Pedido = models.CharField(max_length=25, blank=False, null= False , verbose_name="Ingrese Correo: ")
    Cantidad_pedido = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    Inventario_fisico = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    Fecha_venta = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Apellido: ")

class Comprobante_ventas(models.Model):

    Detalle_venta = models.CharField(max_length=20, blank=False , null= False , verbose_name=" Ingrese Nombre:")
    Precio_Venta = models.CharField(max_length=20, blank=False, null=False, verbose_name="Ingrese Apellido: ")
    Precio_adquisicion = models.CharField(max_length=20, blank=False, null= False , verbose_name="Ingrese Apellido: ")
    Precio_Venta = models.CharField(max_length=20, blank=False, null=False, verbose_name="Ingrese Apellido: ")
    Total_pedido = models.IntegerField(blank=False, null=False, verbose_name="Ingrese Correo: ")
    Fecha_venta = models.IntegerField(blank=False, null=False, verbose_name="Ingrese Apellido: ")

class Gastos(models.Model):

    Codigo_Gasto = models.CharField(max_length=25, blank=False, null=False, verbose_name="Ingrese Correo: ")
    Fecha_Gasto = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Apellido: ")
    Descripcion_Gasto = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")
    monto_Gasto = models.IntegerField( blank=False, null=False, verbose_name="Ingrese Correo: ")

class Estado_de_Resultados(models.Model):

    Ingreso_Total = models.IntegerField( blank=False, null=False )
    Costo_Total = models.IntegerField( blank=False, null=False )
    Resultado_total = models.IntegerField( blank=False, null=False )
    Existencias_eerr = models.IntegerField( blank=False, null=False )
    Margen_perdida = models.IntegerField( blank=False, null=False )
    Resultado_final = models.IntegerField( blank=False, null=False )