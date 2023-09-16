class Singleton:
    """
    A simple singleton pattern implementation in Python.
    """

    instance = None   

    def __init__(self, version) -> None:
        self.version = version
    
    @staticmethod
    def getInstance(version):
        """
        Returns the singleton instance.
        """
        if not Singleton.instance:
            Singleton.instance = Singleton(version)
        return Singleton.instance
    

def appSingleton():
    """
    Creates a new singleton instance.
    """
    singleton1 = Singleton.getInstance("version-1")
    singleton2 = Singleton.getInstance("version-2")

    print(singleton1 == singleton2)


appSingleton()