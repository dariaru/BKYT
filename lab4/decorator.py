class Service():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """

    def operation(self) -> str:
        pass


class Service(Service):
    """
    Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
    быть несколько вариаций этих классов.
    """

    def operation(self) -> str:
        return "Service"


class Decorator(Service):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: Service = None

    def __init__(self, component: Service) -> None:
        self._component = component

    @property
    def component(self) -> str:
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class CoffeeService(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции вместо того,
        чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает расширение классов декораторов.
        """
        return f"CoffeeService({self.component.operation()})"


class TeaService(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self) -> str:
        return f"TeaService({self.component.operation()})"


def client_code(component: Service) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с которыми работает.
    """
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    simple = Service()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...так и декорированные.
    # декораторы могут обёртывать не только простые компоненты, но и другие декораторы.
    decorator1 = CoffeeService(simple)
    decorator2 = TeaService(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)