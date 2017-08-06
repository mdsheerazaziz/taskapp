from django.core.exceptions import ObjectDoesNotExist

from sodingassignment.taskapp.models import Task


def get_all_task(user):
    all_task = []
    tasks = Task.objects.filter(user=user)
    for task in tasks:
        all_task.append({"id": task.id, "name": task.task, "description": task.task_description})
    return all_task


def get_task(task_id, user):
    try:
        task = Task.objects.get(id=task_id, user=user)
        return {"id": task.id, "name": task.task, "description": task.task_description}
    except ObjectDoesNotExist:
        return None


def new_task(task, user):
    task = Task(user=user,
                task=task.get('task_name'),
                task_description=task.get('task_description'))

    return task.save()


def save_modified_task(modified_task, user):
    try:
        task = Task.objects.get(id=modified_task.get("id"), user=user)
        task.name = modified_task.get("task_name")
        task.task_description = modified_task.get("task_description")
        return task.save()
    except ObjectDoesNotExist:
        return None


def remove_task(task_id, user):
    return Task.objects.filter(id=task_id, user=user).delete()
