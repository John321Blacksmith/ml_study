from typing import Optional


class Sample:
    """
    This class represents a basic instance
    of the iris with the main attributes.
    """
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: Optional[str] = None
    ):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None
        
    
    def __repr__(self):
        if self.species is None:
            known_unknown = 'UnknownSample'
        else:
            known_unknown = 'KnownSample'
        
        if self.classification is None:
            classification = ''
        else:
            classification = f', {self.classification}'
    
        return (
            f'{known_unknown} object\n'
            f'Species: {self.species}\n'
            f'{self.sepal_length}\n'
            f'{self.sepal_width}\n'
            f'{self.petal_length}\n'
            f'{self.petal_width}\n'
            f'Classified as {classification}'
        )