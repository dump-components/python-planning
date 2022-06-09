from jobs.jobs import jobs
from repository.models.task_model import TaskModel

class DefinedTaskToJob:

    @staticmethod
    def by_type_task(task: TaskModel):
        job = jobs
        job = job.get(task.type, "job não encontrado")
        return  job(task)