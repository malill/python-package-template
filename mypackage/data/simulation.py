class Simulation:
    def __init__(self, name: str = "my_simulation", seed: int = 42) -> None:
        """Create an instance of a simulation object.

        Args:
            name (str, optional): The name of the simulation object, can be used for versioning.
            seed (int, optional): The seed for the random number generator.
        """
        pass

    def generate_data(self, n: int = 1000) -> None:
        """Generate data for the simulation.

        Args:
            n (int, optional): The number of observations to generate.

        Returns:
            pd.DataFrame: The generated data.
        """
        pass
