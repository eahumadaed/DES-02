from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    resultado = []
    for tarea in tareas:
        subtareas = SubTarea.objects.filter(tarea=tarea)
        resultado.append({
            'tarea': tarea,
            'subtareas': list(subtareas)
        })
    return resultado

def crear_nueva_tarea(descripcion, eliminada):
    tarea = Tarea.objects.create(descripcion=descripcion, eliminada=eliminada)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, eliminada):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, eliminada=eliminada)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for item in tareas_y_subtareas:
        tarea = item['tarea']
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in item['subtareas']:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
