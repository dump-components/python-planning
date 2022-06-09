from repository.task_repository import TaskRepository
from connection.nivy.search_content import SearchContent
from validate.task_validation import TaskValidation
from mock.payload import Payload


class SearchTask:
    
    
    def __init__(self) -> None:
        self.__repository = TaskRepository()
        self.__task = self.__contains_valid_task_in_repository()

    def __contains_valid_task_in_repository(self):
        mock = Payload().get
        if mock:
            task_valid = TaskValidation(mock).get
            self.__repository.save(task_valid)
        task = self.__repository.get()
        if task:
            return task
        new_task = self.__new_task()
        return new_task
    
    def __new_task(self):
        task = SearchContent().content
        task_valid = TaskValidation(task).get
        self.__repository.save(task_valid)
        return self.__repository.get()

    @property
    def get(self):
        return self.__task