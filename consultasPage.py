
import flet as ft
import ddbbErci

def main(page : ft.Page):
    page.title = "Consultas"

    #metodo para consultar y cargar todos los arboles
    def consultar_arboles():
        arboles = ddbbErci.consultar_arboles() #estos son los datos
        cargar_tabla(arboles)
        page.update()

    #datos de la lista de arboles
    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(fila[0]))), #ID
                ft.DataCell(ft.Text(fila[1])), #NOMBRE
                ft.DataCell(ft.Text(fila[2])), #TIPO
                ft.DataCell(ft.Text(str(fila[3]))), #ALTURA
                ft.DataCell(ft.Text(str(fila[4]))), #FECHA
            ]))
    def buscar_arboles(e):
        lista_arboles = ddbbErci.buscar_arboles_por_nombre(nombre_tf.value)
        cargar_tabla(lista_arboles)
        page.update()

    def volver(e):
        page.go("/formularios")

    #OBJETOS
    nombre_tf = ft.TextField(label="Nombre", width=300)
    buscar_btn = ft.ElevatedButton("Buscar", on_click=buscar_arboles, width=300)
    volver_btn = ft.ElevatedButton(text="Volver", on_click=volver)
    tabla = ft.DataTable(bgcolor="pink",
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Altura")),
            ft.DataColumn(ft.Text("Fecha")),
        ]
    )

    columna_datos = ft.Column(
        controls=[
            ft.Text("CONSULTAS",size=40),
            nombre_tf,
            buscar_btn,
            tabla,
            volver_btn,
        ]
    )

    #page.add(columna_datos)
    consultar_arboles()

    return columna_datos
